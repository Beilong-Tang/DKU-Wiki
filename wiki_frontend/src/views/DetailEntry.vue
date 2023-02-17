<template>

    <div class="container">
        <h1>{{ title }}</h1>
        <div id="content"> </div>
    </div>
    <!-- <p> The Entry id is {{ id }}</p> -->
    

</template>

<script>
import axios from 'axios'
import Quill from 'quill'
import {setContent} from './utils/utils'

export default {
    name:'DetailEntry',
    data(){
        return {
            id:this.$route.params.id,
            content:'',
            title:''
        }
    },
    inject:['nav_show'],

    created(){
        this.nav_show();

        axios.get("/entry/entry/"+this.id)
            .then(response=>{
                this.content = response.data.entry;
                this.title = response.data.title;
                setContent("content",this.content);

            })
            .catch(response=>{
                console.log(response)
            })
    },
    
}
</script>

<style>
/* Make sure the toolbox is not showing */
/* .ql-toolbar{
    display: none;
} */

</style>