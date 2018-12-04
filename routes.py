import os
import secrets
from flask import render_template,url_for,flash,redirect,abort,request
from sqlalchemy.sql.functions import current_user
from reservation import app, db
from reservation.models import Reservation
from reservation.form import reservationForm
from datetime import datetime


@app.route('/history')
def history():
    reservations = Reservation.query.all()
    return render_template('history.html', reservations=reservations)

@app.route('/')
def index():
	reservations = Reservation.query.all()
	return render_template('index.html', reservations=reservations)



@app.route('/reservation/new', methods=['GET', 'POST'])
def new_reservation():
    form = reservationForm()
    if form.validate_on_submit():
        if form.date.data < datetime.now().date():
            flash("You cannot book dates in the past")
            return redirect('new_reservation')
        reservation = Reservation(package=form.package.data, date=form.date.data, location=form.location.data, occasion=form.occasion.data, addons=form.addons.data)
        if form.date.data == form.date.data:
            flash("That date is taken!")
            return redirect(url_for('new_reservation'))
        if reservation:
            db.session.add(reservation)
            db.session.commit()
            flash("Reservation created!")
            return redirect(url_for('index'))
    return render_template('reservation.html', title="Make Reservation", form=form)




#@app.route("/reservation/new", methods=['GET','POST'])
#def new_reservation():

#  form = reservationForm()
#  if form.validate_on_submit():
 #    reservation = Reservation(package=form.package.data, date=form.date.data, location=form.location.data, occasion=form.occasion.data, addons=form.addons.data)
 #    db.session.add(reservation)
 #    db.session.commit()
 #    flash('Your post has been created!', 'success')
 #    return redirect(url_for('index'))
#  return render_template('reservation.html',  form=form)


@app.route("/reservation/<int:id>")
def reservation(id):
    reservation = Reservation.query.filter_by(id=id).first_or_404()
    return render_template('view.html',  reservation=reservation)


@app.route("/reservation/update/<int:id>", methods=['GET', 'POST'])
def update_reservation(id):
    reservation = Reservation.query.filter_by(id=id).first_or_404()
    form = reservationForm(obj=reservation)
    if form.validate_on_submit():
        if form.date.data < datetime.now().date():
            flash("You cannot book dates in the past")
            return redirect(url_for('update_reservation',id=id))
        reservation = Reservation(package=form.package.data, date=form.date.data, location=form.location.data, occasion=form.occasion.data, addons=form.addons.data)
        if form.date.data == form.id.data:
            flash("That date is taken!")
            return redirect(url_for('update_reservation',id=id))
        else:
          reservation.package = form.package.data
          reservation.date = form.date.data
          reservation.location = form.location.data
          reservation.occasion = form.occasion.data
          reservation.addons = form.addons.data
        db.session.commit()
        flash("reservation is updated")
        return redirect(url_for('index',id=id))
    elif request.method == 'GET':
        form.package.data = reservation.package
        form.date.data = reservation.date
        form.location.data=reservation.location
        form.occasion.data=reservation.occasion
        form.addons.data=reservation.addons
    return render_template('update.html', form=form)


@app.route("/post/delete/<int:id>", methods=['POST'])
def delete_reservation(id):
    reservation = Reservation.query.filter_by(id=id).first_or_404()
    db.session.delete(reservation)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('index'))
