<template>

    <!-- <form @submit.prevent="submitForm">
        <input type="text" name="username" v-model="username">
        <input type="password" name="password" v-model="password">
        <button type="submit"> Log In</button>
        
    </form> -->
    <div class="container">
        <main class="form-signin w-100 m-auto">

            <form @submit.prevent="submitForm">
                <!-- <img class="mb-4" src="../assets/brand/bootstrap-logo.svg" alt="" width="72" height="57"> -->
                <h1 class="h3 mb-3 fw-normal">Duke Wiki Signin</h1>

                <div class="form-floating">
                    <input input type="text" name="username" v-model="username" class="form-control" id="floatingInput" placeholder="name@example.com">
                    <label for="floatingInput">Username</label>
                </div>
                <div class="form-floating">
                    <input type="password" name="password" v-model="password" class="form-control" id="floatingPassword" placeholder="Password">
                    <label for="floatingPassword">Password</label>
                </div>

                <div class="checkbox mb-3">
                    <label>
                        <input type="checkbox" value="remember-me"> Remember me
                    </label>
                    <div class='message' v-if="message">
                        {{message}}
                    </div>
                </div>
                <button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
                <p class="mt-5 mb-3 text-muted">&copy; 2017–2022</p>
            </form>
        </main>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: "LogIn",
    data() {
        return {
            username: '',
            password: '',
            message:''
        }
    },
    created() {
        this.nav_hide()
    },
    inject: ['nav_hide'],

    methods: {

        submitForm(e) {
            const _this = this;
            const formData = {
                username: this.username,
                password: this.password
            }
            console.log(formData)

            axios
                .post('/api/login/', formData)
                .then(function (response) {

                    _this.$router.replace({'name':'Home', params: { search: 'all' }})
                })
                .catch(error => {
                    this.message="Bad Credentials, please try again."
                })
        }
    }
}

</script>

<style>

.form-signin {
max-width: 330px;
padding: 15px;
}

.message{
    color:red
}

</style>
