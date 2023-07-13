<template>
    <nav class="navbar navbar-expand-xxl navbar-dark bg-dark navbar-expand" aria-label="Seventh navbar example">
        <div class="container-fluid">
            
            <router-link :to="{ name: 'Index' }">
            <a class="navbar-brand" href="#">DKU Wiki</a>
            </router-link>

            <div class="collapse navbar-collapse" id="navbarsExampleXxl">

                <ul class="navbar-nav mb-2 mb-xl-0 col-md-2">
                    <li class="nav-item">
                        <router-link :to="{ name: 'Index' }">
                            <a class="nav-link active" aria-current="page" href="#">Home</a>
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link :to="{ name: 'CreateEntry'}">
                            <a class="nav-link active" aria-current="page" href="#">Create Entry</a>
                        </router-link>
                    </li>
                </ul>
                
                

                <form class=" d-block col-md-6" @submit.prevent="go_search()" >
                    <div class="d-flex">
                        <div class="input-group">
                            <input class="form-control" placeholder="Search" aria-label="Search" v-model="search">
                            <div>
                                <button class="btn btn-outline-secondary dropdown-toggle" type="button"
                                    data-bs-toggle="dropdown" aria-expanded="false" @click="getTag()">Tag</button>
                                <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="tagdropdown">
                                    <li><button class="dropdown-item btn btn-outline-primary" type="button"
                                        @click="removeTag()"><span class="text-primary"> clear all the tags </span></button></li>
                                    <li v-for="tag in tags"><button class="dropdown-item btn btn-outline-primary" type="button"
                                        @click="addTag(tag.name)">{{ tag.name }}</button></li>
                                </ul>
                            </div>
                        </div>

                        <button type="button" class="btn btn-success mx-2" @click="go_search()">Search</button>
                    </div>
                </form>

                <div class="col-md-2"></div>

                <div v-show="ready">

                            <div class="user authenticated" v-if="username">
                                <div class="flex-shrink-0 dropdown">
                                    <a href="#" class="d-block link-dark text-decoration-none dropdown-toggle" data-bs-toggle="dropdown"
                                        aria-expanded="false">
                                        <img :src=avator alt="mdo" width="32" height="32" class="rounded-circle">
                                    </a>
                                    <ul class="dropdown-menu text-small shadow">
                                        <li>
                                            <router-link :to="{ name: 'My' }">
                                            <a class="dropdown-item" href="#">Profile</a>
                                        </router-link>
                                        </li>
                                        <li>
                                            <hr class="dropdown-divider">
                                        </li>
                                        <li><a class="dropdown-item" href="#" @click.prevent="logout()">Sign out</a></li>
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

        </div>

        
    </nav>
</template>

<script>
import axios from "axios"

export default {
    name: "TopNav",
    data() {
        return {
            ready:false,
            if_authenticated: false,
            avator: "",
            username: "",
            search: "",
            baseurl: "",
            tags: "", // return all the existing tags
            tag_chose:[],
        }
    },
    methods: {
        addTag(tag_name){ 
            var arr =[]
            arr.push(tag_name)
            this.tag_chose = arr
            this.$router.push({name:"EntryList", query: {search:this.search, tags:this.tag_chose, page_number:1}})
        },  

        removeTag(){
            this.tag_chose = []
            this.$router.push({name:"EntryList", query: {search:this.search, tags:[], page_number:1}})
        },

        getTag() {
            if (this.tags){
                return;
            }
            axios.get(
                'entry/tags'
            )
                .then(res => {

                    console.log(res);
                    this.tags = res.data
                })
                .catch(res => {
                    console.log("tag fetching error");
                    console.log(res);
                })
        },

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

        to_profile(){
            this.$router.push({ name: 'My' });
        },
        go_search() {
            this.$router.push({ name: 'EntryList', query: { search: this.search, tags: this.tag_chose, page_number:1 } });
        },




    },


    created() {
        const _this = this;
        _this.baseurl = _this.global.baseurl;
        console.log("Authenticating......");
            axios.get('api/authentication/')
            .then(function (res) {
                _this.$nextTick(function(){
                    this.ready = true
                })
                if (res.data.unauthenticated) {
                    console.log("unauthenticated");
                    return;
                }

                if (!_this.$store.state.isLogin){
                const avator = res.data.client.avator;
                _this.avator = _this.baseurl + avator;
                _this.username = res.data.username
                _this.if_authenticated = true
                _this.$store.commit("Login", res.data);}
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
