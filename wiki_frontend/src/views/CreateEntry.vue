<template>

    <div><p>{{ subject }}</p></div>

    <div id="editor" style="height:500px">

    </div>
    
    <button @click="submit()"> Submit </button>

</template>

<script>

import axios from 'axios';
import Quill from 'quill'

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
        console.log(this.id);
        if (this.id === undefined){

            this.quill = new Quill('#editor', {
                theme: 'snow'
            });

            return;
        }
        //axios.get('')

        //var quill = new Quill('#editor', {
        //    theme: 'snow'
        //});
    },

    methods:{
        submit(){

            const content = this.quill.getContents();
            
            var length = this.quill.getLength();
            //const contents = this.content;
            if (length === 1 ){
                console.log("The content cannot be empty!");
                return;
            }
            console.log(content)
        }
    }
}

</script>

<style>

</style>