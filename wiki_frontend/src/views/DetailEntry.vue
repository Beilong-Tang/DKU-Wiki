<template>
    <div class="container">
        
<!-- 
        <button @click="Edit" v-if="!edit" type="button" class="btn btn-secondary float-end flex">Edit</button>
        <button @click="disableEdit" type="button" class="btn btn-secondary float-end" v-else >Quit Editting</button>
        <button v-if="edit" @click="submit">SUBMIT</button> -->

        <div class="row">
            <div class="col-md-2" >
                <button @click="goBack()" type="button" class="btn btn-secondary" >Back</button>
            </div>
            <div class="col-md-8" > <h1>{{ title }}</h1> </div>
            <div class="col-md-2" > 
                <button @click="Edit" v-if="!edit" type="button" class="btn btn-secondary float-end flex">Edit</button>
                <button @click="disableEdit" type="button" class="btn btn-secondary float-end" v-else >Quit Editting</button>
                <button v-if="edit" @click="submit" type="button" class="btn btn-success" >Submit</button>
            </div>

        </div>

        <div v-if="edit">

            <InputPart v-if="tag_origin" @updateInput='confirmTag' :inputlist=tag :taglist=taglist />
        </div>

        <div v-else>
            <span v-for="item in tag" :key="item" class="badge bg-primary me-1">{{ item }}</span>
        </div>

        <div class="row">

            <div class="col-md-3" >
                <div class="toc">
                    <h4 class="mx-auto item-2">{{ title }}</h4>
                    <li v-for="item in tocData" :key="item.id" :class="`tocitem item-${item.tagName.charAt(1)}`"><a
                            :href="'#' + item.id" @click="anchor(item.id)" :id=a+item.id>{{ item.innerHTML }}</a> </li>
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
            content: null,
            origin_content: null,
            taglist: null,
            value: "## 1 23 \n\n # 456 \n\n $a=1$",
            tocData: null,
            a:"a_", // used to do the toc highlighting
            toctitle:"",
        }
    },

    methods: {

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
                    this.$router.push({ name: "EntryList", params: { search: this.title } })
                })
                .catch(res => {
                    console.log(res);
                })

                ;

        },

        goBack(){
            this.$router.go(-1)
        },

    },
    inject: ['nav_show'],

    created() {
        this.nav_show();


        //get taglist 
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
            })
            .catch(response => {
                console.log(response)
            })
    },

    mounted() {
        const _this = this;
        var tocs = document.querySelectorAll('h1,h2,h3');
        for (var i = 0; i < tocs.length; i++) {
            tocs[i].id = tocs[i].innerHTML
        }
        this.tocData = [].slice.apply(tocs);
        this.tocData = _this.tocData.slice(1)

        window.onscroll = function () {
            var tocs = document.querySelectorAll('h1,h2,h3');
            var e=document.getElementsByClassName("entry")[0]
            // console.log(tocs)
            for (var i = 1; i < tocs.length; i++) {
                var top = tocs[i].offsetTop + e.offsetTop;
                var hl = document.getElementById(_this.a + tocs[i].id)
                if ((top > window.scrollY) && (top < window.scrollY + window.innerHeight)){
                    // tocs[i].className = tocs[i].className + "active "
                
                    if (hl.className.indexOf("active ")==-1){
                    hl.className=hl.className +"active ";}
                }
                else {
                    hl.className = hl.className.replace("active ","")
                }


            }
        }
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

.active{
    color:black
}

.tocitem{
    text-align: left;
}
</style>