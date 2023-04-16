<template>
    <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
        <symbol id="check-circle-fill" fill="currentColor" viewBox="0 0 16 16">
            <path
                d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z" />
        </symbol>
        <symbol id="info-fill" fill="currentColor" viewBox="0 0 16 16">
            <path
                d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16zm.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2z" />
        </symbol>
        <symbol id="exclamation-triangle-fill" fill="currentColor" viewBox="0 0 16 16">
            <path
                d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z" />
        </symbol>
    </svg>

    <div class="alert alert-success d-flex align-items-center" role="alert" v-if="msg" style="position:fixed; left: 25%;">
        <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Success:">
            <use xlink:href="#check-circle-fill" />
        </svg>
        <div>
            The profile has been updated
        </div>
    </div>


    <div class="container rounded bg-white mt-5 mb-5">
        <div class="row">
            <div class="col-md-3 border-right">
                <div class="d-flex flex-column align-items-center text-center p-3 py-5"><img class="rounded-circle mt-5"
                        style="width:150px" :src="avator" />

                        <a href="#" @click.prevent="changeAvator()">Change Avator</a>
                        <span class="font-weight-bold">{{ username }}</span>
                        <span class="text-black-50">{{ username }}@duke.edu</span></div>
            </div>
            <div class="col-md-5 border-right">
                <div class="p-3 py-5">
                    <div class="d-flex justify-content-between align-items-center mb-3">
                        <h4 class="text-right">Profile Settings</h4>
                    </div>
                    <div class="row mt-3">
                        <div class="col-md-12"><label class="labels">Nickname</label><input type="text" class="form-control"
                                placeholder="enter phone number" v-model="nickname"></div>
                    </div>
                    <div class="mt-5 text-center"><button class="btn btn-primary profile-button" type="button"
                            @click="submit()">Save
                            Profile</button></div>
                </div>
            </div>
            <div class="col-md-4">
                
            </div>

            <VueAvatarUpload  @error="handleError"  :url="url" :avatar="avator" 
            :headers="headers" lang ='en' v-show="change_avator" @close="change_avator=false"
             @success="handleSuccess" :withCredentials="true"/>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { getCookie } from './utils/utils'
import VueAvatarUpload from 'vue-avatar-upload';
import 'vue-avatar-upload/lib/style.css';

export default {
    components: { VueAvatarUpload },

    data() {
        return {
            username: "",
            avator: "",
            nickname: "",
            msg: false,
            url:'http://127.0.0.1:8000/api/uploadavator/',
            headers:{ "X-CSRFTOKEN": getCookie("csrftoken") },
            change_avator:false
        }
    },

    computed:{
        get_avator(){
            console.log(this.ava)
            return this.ava
        }
    },

    methods: {

        changeAvator(){
            this.change_avator = true
        },

        handleSuccess(e){
            this.change_avator = false
            console.log(e)
        },

        handleError(e){
            console.log(e)
        },

        submit() {
            const _this = this;
            const formData = {
                nickname: this.nickname
            }

            axios.put('api/userinfo/', formData, {
                headers: { "X-CSRFTOKEN": getCookie("csrftoken") }
            })
                .then(function (res) {
                    console.log(res)
                    _this.msg = true
                    setTimeout(function () {
                        _this.msg = false
                    }, 2000)

                })
                .catch(function (res) {
                    console.log(res)

                })


        },
    },

    created() {

        if (!this.$store.getters.get_auth_info) {
            const _this = this;
            _this.baseurl = _this.global.baseurl;
            console.log("Authenticating......");
            axios.get('api/authentication/')
                .then(function (res) {
                    console.log(res)
                    if (res.data.unauthenticated) {
                        console.log("unauthenticated");
                        return;
                    }
                    const avator = res.data.client.avator;
                    _this.avator = _this.baseurl + avator;
                    _this.username = res.data.username
                    _this.if_authenticated = true
                    _this.$store.commit("Login", res.data);
                    _this.ready = true
                    _this.nickname = res.data.client.nickname
                })
                .catch(function (res) {
                    console.log(res);
                })
        }
        else {
            this.username = this.$store.getters.get_auth_info.username
            this.avator = this.global.baseurl + this.$store.getters.get_auth_info.client.avator
            this.nickname = this.$store.getters.get_auth_info.client.nickname
        }
    }

}



</script>

<style>
body {
    background: rgb(99, 39, 120)
}

.form-control:focus {
    box-shadow: none;
    border-color: #BA68C8
}

.profile-button {
    background: rgb(99, 39, 120);
    box-shadow: none;
    border: none
}

.profile-button:hover {
    background: #682773
}

.profile-button:focus {
    background: #682773;
    box-shadow: none
}

.profile-button:active {
    background: #682773;
    box-shadow: none
}

.back:hover {
    color: #682773;
    cursor: pointer
}

.labels {
    font-size: 11px
}

.add-experience:hover {
    background: #BA68C8;
    color: #fff;
    cursor: pointer;
    border: solid 1px #BA68C8
}
</style>