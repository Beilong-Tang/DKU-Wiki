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
                         <router-link :to="{ name: 'Index'}">
                            <a class="nav-link active" aria-current="page" href="#">Home</a>
                        </router-link>
                    </li>
                </ul>
                
                <form @submit.prevent="go_search()" class="m-auto d-block w-50">
                    <div class="d-flex">
                        <div class="input-group">
                                <input class="form-control" placeholder="Search" aria-label="Search" v-model="search">
                                <div>
                                <button class="btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Tag</button>
                                <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="tagdropdown">
                                    <li><a class="dropdown-item" href="#">Action</a></li>
                                    <li><a class="dropdown-item" href="#">Another action</a></li>
                                    <li><a class="dropdown-item" href="#">Something else here</a></li>
                                    <li><hr class="dropdown-divider"></li>
                                    <li><a class="dropdown-item" href="#">Separated link</a></li>
                                </ul>
                                </div>
                        </div>

                        <button type="submit" class="btn btn-success mx-2">Search</button>
                    </div>
                </form>



                <div class="user authenticated" v-if="username">
                    <div class="flex-shrink-0 dropdown">
                        <a href="#" class="d-block link-dark text-decoration-none dropdown-toggle"
                            data-bs-toggle="dropdown" aria-expanded="false">
                            <img :src= avator alt="mdo" width="32" height="32"
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

import {inject} from 'vue'

export default {
    name: "TopNav",
    data() {
        return {
            if_authenticated: false,
            avator: "",
            username: "",
            search: "",
            baseurl:""
            
        }
    },
    methods: {
        logout() {
            const _this = this;
            axios.get('api/logout/')
                .then(function (res) {
                    console.log("logout success")
                    _this.username = ""
                    
                    _this.$store.commit("Logout");

                })
                .catch(function (res) {
                    console.log("logout fail")

                })
        },
        go_search() {

            this.$router.push({name:'EntryList',query:{search:this.search}});
        },
    },

    created() {
        const _this = this;
        _this.baseurl = _this.global.baseurl;
        console.log("Authenticating......");
        axios.get('api/authentication/')
            .then(function (res) {
                if (res.data.unauthenticated) {
                    console.log("unauthenticated");
                    return;
                }
                const avator = res.data.client.avator;
                _this.avator = _this.baseurl+avator;
                _this.username = res.data.username
                _this.if_authenticated = true
                _this.$store.commit("Login");
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
