Vue.config.delimiters = ['[[',']]']

new Vue({
	el:'#app',
	delimiters:['[[',']]'],
	data:{
		message:'Hello World!'
	}
})


var login = new Vue({
	delimiters:['[[',']]'],
	el:'#LoginForm',
	data:{
		form:{
			email:'',
			password:''
		}
	},

	methods:{
		loginUser: function(){
			console.log(this.form)
			this.$http.post('/login', {data:this.form})
			.then(response => {
				if (response.data.status == true ){
					window.location.href = '/home'
				}
			},
			})
		}
	}
})


var registerUser = new Vue({
	delimiters:['[[',']]'],
	el:'#RegistrationForm',
	data:{
		form:{
			username:'',
			password:'',
            email:''
		}
	},

	methods:{
		registerUser: function(){
			this.$http.post('/register', {data:this.form})
			.then(response => {
				if (response.data.code == 200 && response.data.status == true){
					window.location.href = '/'
				}
				else{
					this.form.has_error = "has-error";
				}
			}, response => {
				console.log("error >>> ")
			})
		}
	}


})
