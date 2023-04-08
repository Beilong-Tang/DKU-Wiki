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

    <div class="alert alert-success d-flex align-items-center" role="alert" v-if="msg"
        style="position:absolute; left: 25%;">
        <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Success:">
            <use xlink:href="#check-circle-fill" />
        </svg>
        <div>
            The post has been updated
        </div>
    </div>

    <div class="container">

        <!-- 
        <button @click="Edit" v-if="!edit" type="button" class="btn btn-secondary float-end flex">Edit</button>
        <button @click="disableEdit" type="button" class="btn btn-secondary float-end" v-else >Quit Editting</button>
        <button v-if="edit" @click="submit">SUBMIT</button> -->


        <div class="row">
            <div class="col-md-2">
                <button @click="goBack()" type="button" class="btn btn-secondary" v-if="!edit">Back</button>
            </div>
            <div class="col-md-8">
                <h1>{{ title }}</h1>
            </div>
            <div class="col-md-2">
                <button @click="Edit" v-if="!edit" type="button" class="btn btn-secondary float-end flex">Edit</button>
                <button @click="disableEdit" type="button" class="btn btn-secondary float-end" v-else>Quit Editting</button>
                <button v-if="edit" @click="submit" type="button" class="btn btn-success">Submit</button>
            </div>

        </div>

        <div v-if="edit">

            <InputPart v-if="tag_origin" @updateInput='confirmTag' :inputlist=tag :taglist=taglist />
        </div>

        <div v-else>
            <span v-for="item in tag" :key="item" class="badge bg-primary me-1">{{ item }}</span>
        </div>

        <div class="row">

            <div class="col-md-3">
                <div class="toc">
                    <div v-show="!edit">
                        <h4 class="mx-auto item-2">{{ title }}</h4>
                        <li v-for="item in tocData" :key="item.id" :class="`tocitem item-${item.tagName.charAt(1)}`"><a
                                :href="'#' + item.id" @click.prevent="anchor(item.id)" :id=a + item.id>{{ item.innerHTML
                                }}</a> </li>
                    </div>
                    <button v-if="edit" @click="disableEdit" type="button" class="btn btn-secondary float-end">Quit
                        Editting</button>
                    <button v-if="edit" @click="submit" type="button" class="btn btn-success">Submit</button>
                </div>


            </div>

            <div class="col-md-9">
                <div class="entry">

                    <v-md-editor v-if="!edit" v-model="origin_content" mode="preview"></v-md-editor>

                    <v-md-editor v-else v-model="content" mode="editable"></v-md-editor>

                </div>
            </div>
        </div>


    </div>


    <!-- <p> The Entry id is {{ id }}</p> -->
</template>

<script>


import InputPart from '../components/InputPart.vue'
import EntrySideNav from '../components/EntrySideNav.vue'
import axios from 'axios'
// import Quill from 'quill'
import { getCookie } from './utils/utils'
import { setData } from './utils/utils'

export default {

    components: { InputPart, EntrySideNav },


    name: 'DetailEntry',
    data() {
        return {
            id: this.$route.params.id,
            // entry:null, // id, client <Object>, title, create_date, tag, content 
            edit: false,  // false when it is not editting, true when it is editting

            //entry object
            client: null,
            title: null,
            create_date: null,
            tag: null, //changeable
            tag_origin: null, //the origianl tag
            content: "",
            origin_content: "",
            taglist: null,
            value: "## 1 23 \n\n # 456 \n\n $a=1$",
            tocData: null,
            a: "a_", // used to do the toc highlighting
            toctitle: "",
            msg: false,
            timer: null,
        }
    },

    methods: {

        anchor(id) {
            console.log(id)
            document.getElementById(id).scrollIntoView()
        },

        confirmTag(tag) {
            this.tag = tag;
        },

        Edit() {

            if (this.edit == true) {
                return;
            }

            this.edit = true;


        },

        disableEdit() {
            const _this = this;
            if (this.edit == false) {
                return;
            }

            const conf = confirm("Are you sure you want to quit editting?");

            if (conf) {
                this.edit = false;
                _this.tag = _this.tag_origin;
                _this.content = _this.origin_content;
            }

            this.align_id();

        },

        align_id() {
            this.$nextTick(function () {
                var tocs = document.querySelectorAll('h1,h2,h3');
                for (var i = 0; i < tocs.length; i++) {
                    tocs[i].id = tocs[i].innerHTML
                }
            })
        },

        submit() {

            if (this.content.length === 1) {
                alert("The content cannot be empty!");
                return;
            }

            const formData = {
                title: this.title,
                content: this.content,
                tag: this.tag
            }
            axios.post('/entry/create_entry/', formData,
                {
                    headers: { "X-CSRFTOKEN": getCookie("csrftoken") }
                })
                .then(res => {
                    console.log("post successfully updated")
                    this.msg = true
                    this.origin_content = this.content;
                    this.edit = false

                    this.timer = setTimeout(this.reduce_time, 1000)

                })
                .catch(res => {
                    console.log(res);
                });

        },

        goBack() {
            this.$router.go(-1)
        },

        reduce_time() {
            this.msg = false
        }


    },
    inject: ['nav_show'],

    created() {
        this.nav_show();

        const _this = this;
        axios.get("entry/tags")
            .then(res => {
                _this.taglist = res.data;
            });


        axios.get("/entry/entry/" + this.id)
            .then(response => {
                setData(this, response.data, 'client', 'title', 'create_date', 'tag', 'content')
                this.origin_content = this.content;
                this.tag_origin = this.tag;
                this.$nextTick(function () {
                    var tocs = document.querySelectorAll('h1,h2,h3');
                    for (var i = 0; i < tocs.length; i++) {
                        tocs[i].id = tocs[i].innerHTML
                    }
                    this.tocData = [].slice.apply(tocs);
                    this.tocData = _this.tocData.slice(1);
                })
            })
            .catch(response => {
                console.log(response)
            })

        //get taglist 

    },


    beforeDestroy() {

        window.onscroll = null

    },
}
</script>

<style>
.item-1 {
    font-weight: 700;
    padding-left: 0;
}

.item-2 {
    padding-left: 20px;
}

.item-3 {
    padding-left: 40px;
}

content {
    border: 0px;
}

.scrollbar {
    text-align: left;
}

.toc {
    position: sticky;
    top: 50px
}

.active {
    color: black
}

.tocitem {
    text-align: left;
}</style>