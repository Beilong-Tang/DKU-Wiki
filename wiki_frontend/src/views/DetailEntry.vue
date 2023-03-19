<template>
    <div class="container">

        <button @click="Edit" v-if="!edit">Edit</button>
        <button @click="disableEdit" v-else>Quit Editting</button>
        <button @click="submit">SUBMIT</button>


        <div v-if="edit">

            <InputPart v-if="tag_origin" @updateInput='confirmTag' :inputlist=tag :taglist=taglist />
        </div>

        <div v-else>

            tags:
            <span v-for="item in tag" :key="item" class="badge bg-primary me-1">{{item}}</span>
        
        </div>

        <h1>{{ title }}</h1>

        <div class="row">

            <div class="col-md-2">

                 <li v-for="item in tocData" :key="item.id" :class="`item-${item.tagName.charAt(1)}`" ><a href="#Test" @click="anchor(item.id)">{{ item.innerHTML }}</a> </li>

            </div>

            <div class="col-md-10">
                <div class="entry">
                    
                     <v-md-editor v-if="!edit" v-model="origin_content"  mode="preview"></v-md-editor>
                    
                     <v-md-editor v-else v-model="content" mode="editable" ></v-md-editor>
                    
                    </div>
            </div>

           



        </div>


    </div>


    <!-- <p> The Entry id is {{ id }}</p> -->
</template>

<script>


import InputPart from '../components/InputPart.vue'
import QuillEdit from '../components/QuillEdit.vue'
import EntrySideNav from '../components/EntrySideNav.vue'
import axios from 'axios'
// import Quill from 'quill'
import { getCookie } from './utils/utils'
import { setData } from './utils/utils'

export default {

    components: { InputPart, QuillEdit, EntrySideNav },


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
            origin_content:null,
            taglist: null,
            value: "## 1 23 \n\n # 456 \n\n $a=1$",
            tocData: null,
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

            this.edit = false;

            const conf = confirm("Are you sure you want to quit editting?");

            if (conf) {
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

        anchor(id){
            let anchorElement = document.getElementById(id)
            if (anchorElement) {
            anchorElement.scrollIntoView()
            }
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
                this.origin_content=this.content;
                this.tag_origin = this.tag;
            })
            .catch(response => {
                console.log(response)
            })
    },

    mounted() {
        var tocs = document.querySelectorAll('h1,h2,h3');
        for (var i =0;i<tocs.length;i++){
            tocs[i].id = tocs[i].innerHTML
        }
        this.tocData = tocs;

    },







}
</script>

<style>

ul {
  border: 1px solid #000;
}
ul li {
  list-style: none;
}
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
</style>