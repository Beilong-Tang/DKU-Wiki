<template>
<div class="container">
    <div class="p-5 mb-4 bg-light rounded-3">
      <div class="container-fluid py-5">
        <h1 class="display-5 fw-bold">BTBlog</h1>
        <!-- <p v-if ="!this.$store.state.isLogin" class=" fs-4">BTBlog</p> -->

        <p>A personal blog developed by Beilong Tang (DKU Student, 2025). This blog covers everything he wants to share. 😀</p>
        
        <button v-if= "!this.$store.state.isLogin" class="btn btn-primary btn-lg" type="button" @click="toLogin">LogIn</button>
      </div>
    </div>

    <div class="row align-items-md-stretch">
      <div class="col-md-6">
        <div class="h-100 p-5 text-white bg-dark rounded-3">
          <h2>Entry</h2>
          <p>Click here to see all the entries</p>
          <router-link :to="{name:'EntryList', query:{page_number:1}}">
          <button class="btn btn-outline-light" type="button">Entries</button>
        
        </router-link>
        </div>
      </div>
      <div class="col-md-6">
        <div class="h-100 p-5 bg-light border rounded-3">
          <h2>Tag</h2>
          <p>Click here to see all the tags</p>
          <router-link :to="{name:'TagList'}">
          <button class="btn btn-outline-secondary" type="button">Tags</button>
          </router-link>
        </div>
      </div>

      <div style="margin-top:20px">
        <img src="http://dku-vcm-2630.vm.duke.edu:8000/media/cat.jpg" style="width:50%">
        <p>Tiger (My cat)</p>

      </div>


    </div>
  </div>

</template>


<script>



export default {
    data(){
        return{

        }
    },

    inject: ['nav_show'],
    created() {
        this.nav_show();
    },

    methods:{
      toLogin(){
        this.$router.push({name:"LogIn"});
        return;
      }
    }


}
</script>

<style>

</style>