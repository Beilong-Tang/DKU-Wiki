<template>

    <!-- <div v-for="tag in taglist" >{{ tag }}</div> -->

     <main  class="container">
    <div class="my-3 p-3 bg-body rounded shadow-sm text-start">
    <h6 class="border-bottom pb-2 mb-0">All the tags</h6>

    <div class="d-flex text-muted pt-3" v-for = "tag in taglist">
      <svg class="bd-placeholder-img flex-shrink-0 me-2 rounded" width="32" height="32" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: 32x32" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="#007bff"/><text x="50%" y="50%" fill="#007bff" dy=".3em">32x32</text></svg>
      <p class="pb-3 mb-0 small lh-sm border-bottom">
        <strong class="d-block text-gray-dark">
          <a href="#" @click.prevent="gotoTag(tag)">
          {{tag.name}}
          </a>
        </strong>
        Total Entries: {{ tag.number }} ; Last Update: {{ tag.update_date }}
      </p>

    </div>
  </div>
    </main>

</template>


<script>
import axios from 'axios';

export default {

    data(){
        return {
            taglist:[]
        }
    },
    inject:['nav_show'],
    created(){
        this.nav_show();
        
        const _this = this;

        axios.get(
            'entry/tags'
        )
        .then(res=>{
            console.log(res);
            _this.taglist = res.data
        })
        .catch(res=>{
            console.log("tag fetching error");
            console.log(res);
        })

    },

    methods:{
      gotoTag(tag){
        this.$router.push({name:"EntryList", query:{tags:[tag.name], page_number:1, search:""}})
      }
    }


}

</script>

<style>


</style>