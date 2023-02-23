<template>

    

    <div class="container">

        <!-- <div class="alert alert-warning alert-dismissible fade show" role="alert" style="position:absolute">
  <strong>Holy guacamole!</strong> You should check in on some of those fields below.
  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
</div> -->

        <h1>{{ subject }}</h1>

        <button @click="submit()"> Submit </button>

    <div id="editor" style="min-height:500px">

    </div>

    </div>
    
    

</template>

<script>

import axios from 'axios';
import Quill from 'quill'
import {getCookie} from './utils/utils'

export default {

    data() {
        return {
            subject: this.$route.query.subject,
            id:this.$route.query.id,
            content:"",
            quill:null,
        }
    },

    mounted() {

        // check if it is modifying or creating 

        if (this.id === undefined){

            this.quill = new Quill('#editor', {
                theme: 'snow',
            });

            return;
        }
        

    },

    methods:{
        submit(){

            const content = JSON.stringify(this.quill.getContents());
            
            var length = this.quill.getLength();
            
            if (length === 1 ){
                alert("The content cannot be empty!");
                return;
            }

            const formData={
                title:this.subject,
                content:content
            }
            axios.post('/entry/create_entry/' , formData,
            {
                headers:{"X-CSRFTOKEN": getCookie("csrftoken")}
            })
                .then(res=>{
                    console.log("post successfully created")
                    this.$router.push({name:"Home", params:{search:this.subject}})
                })
                .catch(res=>{
                    console.log(res);
                })

            
            ;
        }
    },
    watch:{

        // inspect the router

        $route(to,from){
            console.log('creating entry')
        }
    },
}

</script>

<style>
/* .ql-toolbar{
    display:none
} */
</style>