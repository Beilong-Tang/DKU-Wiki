<template>

    <div v-if="!send_email">
        <section class="vh-100" style="background-color: #eee;">
            <div class="container h-100">
                <div class="row d-flex justify-content-center align-items-center h-100">
                    <div class="col-lg-12 col-xl-11">
                        <div class="card text-black" style="border-radius: 25px;">
                            <div class="card-body p-md-5">
                                <div class="row justify-content-center">
                                    <div class="col-md-10 col-lg-6 col-xl-5 order-2 order-lg-1">

                                        <p class="text-center h1 fw-bold mb-5 mx-1 mx-md-4 mt-4">Sign up</p>

                                        <form class="mx-1 mx-md-4" @submit.prevent="submit_form()">

                                            <div class="d-flex flex-row align-items-center mb-4">
                                                <i class="fas fa-user fa-lg me-3 fa-fw"></i>
                                                <div class="form-outline flex-fill mb-0">
                                                    <input type="text" id="form3Example1c" class="form-control"
                                                        v-model="username" v-on:blur="check_duplicate({username})" />
                                                    <label class="form-label" for="form3Example1c">Your Name</label>
                                                </div>
                                            </div>

                                            <div class="message" v-if="username_error">
                                                <p>{{ username_error}}</p>
                                            </div>


                                            <div class="d-flex flex-row align-items-center mb-4">
                                                <i class="fas fa-envelope fa-lg me-3 fa-fw"></i>
                                                <div class="form-outline flex-fill mb-0">
                                                    <input type="email" id="form3Example3c" class="form-control"
                                                        v-model="email" placeholder="xxx@duke.edu" v-on:blur="check_duplicate({email})"/>
                                                    <label class="form-label" for="form3Example3c">Your Email</label>
                                                </div>
                                            </div>

                                            <div class="message" v-if="email_error">
                                                <p>{{ email_error}}</p>
                                            </div>

                                            <div class="d-flex flex-row align-items-center mb-4">
                                                <i class="fas fa-lock fa-lg me-3 fa-fw"></i>
                                                <div class="form-outline flex-fill mb-0">
                                                    <input type="password" id="form3Example4c" class="form-control"
                                                        v-model="password" />
                                                    <label class="form-label" for="form3Example4c">Password</label>
                                                </div>
                                            </div>

                                            <div class="d-flex flex-row align-items-center mb-4">
                                                <i class="fas fa-key fa-lg me-3 fa-fw"></i>
                                                <div class="form-outline flex-fill mb-0">
                                                    <input type="password" id="form3Example4cd" class="form-control"
                                                        v-model="password_re" />
                                                    <label class="form-label" for="form3Example4cd">Repeat your
                                                        password</label>
                                                </div>
                                            </div>

                                            <div class="message" v-if="message">
                                                <p>{{ message }}</p>
                                            </div>

                                            <div class="form-check d-flex justify-content-center mb-5">
                                                <input class="form-check-input me-2" type="checkbox" value=""
                                                    id="form2Example3c" />
                                                <label class="form-check-label" for="form2Example3">
                                                    I agree all statements in <a href="#!">Terms of service</a>
                                                </label>
                                            </div>

                                            <div class="d-flex justify-content-center mx-4 mb-3 mb-lg-4">
                                                <button type="submit" class="btn btn-primary btn-lg">Register</button>
                                            </div>

                                        </form>

                                    </div>
                                    <div
                                        class="col-md-10 col-lg-6 col-xl-7 d-flex align-items-center order-1 order-lg-2">

                                        <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-registration/draw1.webp"
                                            class="img-fluid" alt="Sample image">
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>

    <div v-else>
        <section class="vh-100" style="background-color: #eee;">
            <div class="container h-100">
                <div class="row d-flex justify-content-center align-items-center h-100">
                    <div class="col-lg-12 col-xl-11">
                        <div class="card text-black" style="border-radius: 25px;">
                            <div class="card-body p-md-5">
                                <div class="row justify-content-center">
                                    <div class="col-md-10 col-lg-6 col-xl-5 order-2 order-lg-1">

                                        <p class="text-center h1 fw-bold mb-5 mx-1 mx-md-4 mt-4">Email Verification</p>
                                        <p>A email including verification code has been sent to {{ email }}, please
                                            input it here.</p>

                                        <form class="mx-1 mx-md-4" @submit.prevent="register()">
                                            <div class="d-flex flex-row align-items-center mb-4">
                                                <i class="fas fa-user fa-lg me-3 fa-fw"></i>
                                                <div class="form-outline flex-fill mb-0">
                                                    <input type="text" id="form3Example1c" class="form-control"
                                                        v-model="code" placeholder="Verification Code" />
                                                </div>
                                            </div>

                                            <div class="d-flex justify-content-center mx-4 mb-3 mb-lg-4">
                                                <button type="submit" class="btn btn-primary btn-lg">Next</button>
                                            </div>
                                        </form>

                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>

</template>

<script>
import axios from 'axios'
import { register } from 'register-service-worker';
export default {
    data() {
        return {
            username: '',
            email: '',
            password: '',
            password_re: '',
            message: '',
            code:'',
            send_email: false,
            username_error:"",
            email_error:""
        }
    },
    inject: ['nav_show', 'nav_hide'],
    created() {
        this.nav_hide();
    },
    methods: {
        logout() {
            localStorage.setItem('token', '')
            this.username = ''

        },

        check_duplicate(name){
            
            const _this = this;
            if (name.hasOwnProperty("username")){
                _this.username_error="";
            }
            else if (name.hasOwnProperty("email")){
                this.email_error = "";
            }

            // if there is no value in the name
            if (Object.values(name)[0]===''){
                return;
            }

            //check if the email is okay or not.

            const formData = name;
            axios.post(
                'api/duplicate/',
                formData
            )
            .then(res=>{
                console.log(res);
            })
            .catch(res=>{
                console.log(res);
                const info = res.response.data.message[0];
                console.log(name.username)
                switch(Object.keys(name)[0]){
                    case 'username':
                        _this.username_error= info;
                        break;
                    case 'email':
                        _this.email_error = info;
                        break;
                    default:
                        console.log(name);
                }
            })

        },

        submit_form() {
            const _this = this;
            this.message = ''


            // Check Email
            if (!this.email.endsWith("@duke.edu")) {
                this.message = "Please enter the email that ends in '@duke.edu'";
                return;
            }
            if (this.email_error){
                return;
            }

            // Check Username
            if (this.username.length < 5) {
                this.message = 'The length of the username has to be greater or equal than 5.';
                return;
            }
            if (this.username.length > 20) {
                this.message = 'The length of the username has to be smaller or equal than 20.';
                return;
            }

            if (this.username_error){
                return;
            }

            // Check password
            if (this.password.length < 8) {
                this.message = 'The length of the password has to be greater or equal than 8.';
                return;
            }
            if (this.password.length > 26) {
                this.message = 'The length of the password has to be smaller or equal than 26.';
                return;
            }

            if (this.password != this.password_re) {
                this.message = 'Please enter the code with the same value.'
                return;
            }
            axios.post('api/sendemail/',
                {
                    email:this.email
                }
            )
            .then( function(res){
                _this.send_email = true
            })
            .catch (function(res){
                console.log('catching error')
                console.log(res);
            })
        },

        register(){
            const _this = this;
            axios.post('api/signup/',
                {
                    username: this.username,
                    password: this.password,
                    email: this.email,
                    code:this.code
                }
            )
                .then(function (res) {
                    console.log(res);
                    _this.$router.replace({ name: 'EntryList' , query:{search:'all', page_number:1}})
                })
                .catch(function (res) {
                    console.log('catching error');
                    console.log(res);
                })  
        }


    },
    name: 'SignUp',
    beforeCreate() {
        // const token = this.$store.state.token;
        // axios.defaults.headers.common['Authorization'] = 'Token ' + token;

        axios.get('/')
            .then(response => {
                console.log(response)
                this.username = response.data.user
            })
            .catch(response => {
                console.log(response)
            })
    }
}
</script>

<style>
@import './css/SignUp.css';
</style>