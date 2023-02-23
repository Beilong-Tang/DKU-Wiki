<template>

    <div class="container">
        <button @click="Edit" v-if="!edit">Edit</button>
        <button @click="disableEdit" v-else>Quit Editting</button>
        <button @click="submit">SUBMIT</button>
        <h1>{{ title }}</h1>

            <div class="entry">
                <div id="content"> </div>
            </div>
    </div>
    <!-- <p> The Entry id is {{ id }}</p> -->
    

</template>

<script>
import axios from 'axios'
// import Quill from 'quill'
import {setContent} from './utils/utils'
import {getCookie} from './utils/utils'

export default {
    name:'DetailEntry',
    data(){
        return {
            id:this.$route.params.id,
            content:"",
            title:'',
            edit:false,  // false when it is not editting, true when it is editting
            quill:null
        }
    },

    methods:{
        Edit(){
            
            if (this.edit ==true){
                return;
            }

            this.edit=true;
            
            var toolbar = document.getElementsByClassName("ql-toolbar")[0];
            toolbar.style.display='block';
            var content = document.getElementById("content");
            content.style.border='1px solid #ccc'
            content.style.borderTop='0px';


            this.quill.enable();
        },

        disableEdit(){
            const _this = this;
            if (this.edit==false){
                return;
            }

            this.edit = false;

            const conf = confirm("Are you sure you want to quit editting?");

            if (conf){
                this.quill.setContents(_this.content);
                this.quill.disable();
                var toolbar = document.getElementsByClassName("ql-toolbar")[0];
                toolbar.style.display='none';
                var content = document.getElementById("content");
                content.style.border='0px';
            }

            else {
                return;
            }

        },  

        submit(){
            const content = JSON.stringify(this.quill.getContents());
            
            var length = this.quill.getLength();
            
            if (length === 1 ){
                alert("The content cannot be empty!");
                return;
            }

            const formData={
                title:this.title,
                content:content
            }
            axios.post('/entry/create_entry/' , formData,
            {
                headers:{"X-CSRFTOKEN": getCookie("csrftoken")}
            })
                .then(res=>{
                    console.log("post successfully updated")
                    this.$router.push({name:"Home", params:{search:this.title}})
                })
                .catch(res=>{
                    console.log(res);
                })

            ;

        }
    },
    inject:['nav_show'],

    created(){
        this.nav_show();

        axios.get("/entry/entry/"+this.id)
            .then(response=>{
                this.content = JSON.parse(response.data.entry);
                this.title = response.data.title;
                setContent("content",this.content,this);
            })
            .catch(response=>{
                console.log(response)
            })
    },

    
    

    
    
}
</script>

<style>

    #content{
        border:0px;
    }

    /* .entry{
        border:1px solid #ccc;
    } */

</style>