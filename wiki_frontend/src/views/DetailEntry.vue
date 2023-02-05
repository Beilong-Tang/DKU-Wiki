<template>
    <p> The Entry id is {{ id }}</p>
    <p>{{ detail }}</p>
</template>

<script>
import axios from 'axios'

export default {
    name:'DetailEntry',
    data(){
        return {
            id:this.$route.params.id,
            detail:''
        }
    },
    inject:['nav_show'],
    created(){
        this.nav_show();
    },
    
    mounted(){
        axios.get("/entry/entry/"+this.id)
            .then(response=>{
                this.detail=response.data.entry
                console.log(response.data)
            })
    }
}
</script>

<style>

</style>