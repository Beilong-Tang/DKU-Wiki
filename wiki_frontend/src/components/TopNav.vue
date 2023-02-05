<template>
    <nav class="navbar navbar-expand-xxl navbar-dark bg-dark navbar-expand" aria-label="Seventh navbar example">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Duke Wiki</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarsExampleXxl"
                aria-controls="navbarsExampleXxl" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarsExampleXxl">
                <ul class="navbar-nav me-auto mb-2 mb-xl-0">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Link</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link disabled">Disabled</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" data-bs-toggle="dropdown"
                            aria-expanded="false">Dropdown</a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="#">Action</a></li>
                            <li><a class="dropdown-item" href="#">Another action</a></li>
                            <li><a class="dropdown-item" href="#">Something else here</a></li>
                        </ul>
                    </li>
                </ul>

                <form @submit.prevent="go_search()">
                    <input class="form-control" placeholder="Search" aria-label="Search" v-model="search">
                </form>



                <div class="user authenticated" v-if="username">
                    <div class="flex-shrink-0 dropdown">
                        <a href="#" class="d-block link-dark text-decoration-none dropdown-toggle"
                            data-bs-toggle="dropdown" aria-expanded="false">
                            <img src="https://github.com/mdo.png" alt="mdo" width="32" height="32"
                                class="rounded-circle">
                        </a>
                        <ul class="dropdown-menu text-small shadow">
                            <li><a class="dropdown-item" href="#">New project...</a></li>
                            <li><a class="dropdown-item" href="#">Settings</a></li>
                            <li><a class="dropdown-item" href="#">Profile</a></li>
                            <li>
                                <hr class="dropdown-divider">
                            </li>
                            <li><a class="dropdown-item" href="#" @click="logout()">Sign out</a></li>
                        </ul>
                    </div>
                </div>

                <div class="user unauthenticated" v-else>
                    <router-link :to="{ name: 'LogIn' }">
                        <button type="button" class="btn btn-outline-light me-2">Login</button>
                    </router-link>
                    <!-- <button type="button" class="btn btn-outline-light me-2" @click = "go_login()">Login</button> -->
                    <router-link :to="{ name: 'SignUp' }">
                        <button type="button" class="btn btn-outline-light me-2">Sign-up</button>
                    </router-link>
                </div>



            </div>
        </div>
    </nav>

</template>

<script>
import axios from "axios"

export default {
    name: "TopNav",
    data() {
        return {
            if_authenticated: false,
            avator: "",
            username: "",
            search: "",
        }
    },
    methods: {
        logout() {
            const _this = this;
            axios.get('api/logout/')
                .then(function (res) {
                    console.log("logout success")
                    _this.username = ""

                })
                .catch(function (res) {
                    console.log("logout fail")

                })
        },
        go_search() {
            if (this.search == ""){
                this.search ="all";
            } 
            this.$router.push({name:'Home',params:{search:this.search}});
        },
    },

    created() {
        const _this = this;
        axios.get('api/authentication/')
            .then(function (res) {
                if (res.data.unauthenticated) {
                    console.log("unauthenticated");
                    return;
                }
                _this.username = res.data.username
                _this.if_authenticated = true
            })
            .catch(function (res) {
                console.log(res);
            })
    },

}

</script>

<style>
@import './css/TopNav.css';
</style>
