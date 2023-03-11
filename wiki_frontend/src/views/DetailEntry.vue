<template>

    <div class="container">
        <button @click="Edit" v-if="!edit">Edit</button>
        <button @click="disableEdit" v-else>Quit Editting</button>
        <button @click="submit">SUBMIT</button>


        <div v-if="edit">

        <InputPart v-if="tag_origin" @updateInput='confirmTag'  :inputlist=tag :taglist=taglist />
        </div>

        <div v-else>
            {{ tag }}
        </div>

        <h1>{{ title }}</h1>

            <div class="entry">
                <div id="content"> </div>
            </div>
    </div>
    <!-- <p> The Entry id is {{ id }}</p> -->
    

</template>

<script>
import InputPart from '../components/InputPart.vue'
import axios from 'axios'
// import Quill from 'quill'
import {setContent} from './utils/utils'
import {getCookie} from './utils/utils'
import {changeStyle} from './utils/utils'
import {setData} from './utils/utils'


export default {

    components:{InputPart},

    name:'DetailEntry',
    data(){
        return {
            id:this.$route.params.id,
            // entry:null, // id, client <Object>, title, create_date, tag, content 
            edit:false,  // false when it is not editting, true when it is editting

            //entry object
            quill:null,
            client:null,
            title:null,
            create_date:null,
            tag:null, //changeable
            tag_origin:null , //the origianl tag
            content:null,
            taglist:null,

        }
    },

    methods:{
        confirmTag(tag){
            this.tag = tag;
        },

        Edit(){
            
            if (this.edit ==true){
                return;
            }

            this.edit=true;
            
            changeStyle(this.edit);


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
                _this.tag = _this.tag_origin;
                changeStyle(this.edit);
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
                title:this.entry.title,
                content:content
            }
            axios.post('/entry/create_entry/' , formData,
            {
                headers:{"X-CSRFTOKEN": getCookie("csrftoken")}
            })
                .then(res=>{
                    console.log("post successfully updated")
                    this.$router.push({name:"EntryList", params:{search:this.title}})
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


        //get taglist 
        const _this = this;
        axios.get("entry/tags")
            .then(res => {
                _this.taglist = res.data;
            });


        axios.get("/entry/entry/"+this.id)
            .then(response=>{
                setData(this, response.data,'client' ,'title', 'create_date','tag','content')
                this.tag_origin = this.tag;
                this.content = JSON.parse(this.content)
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