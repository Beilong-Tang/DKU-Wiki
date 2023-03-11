<!-- See all the posts in home page -->
<template>

    <div>


    </div>

    <div class="container">
        <div v-for="entry in entries" :key="entry.id" class="entry" >
            <div class="row">
                <router-link :to="{ name: 'DetailEntry', params: { id: entry.id } }">
                    <div style="width:40%">Title:{{ entry.title }}</div>
                </router-link>
                <div style="width:10%"></div>
                <div style="width:40%">Creator_ID:{{ entry.client }}</div>
            </div>
            <div class="row">
                <div style="width:40%">
                    <p>Date:{{ entry.create_date }}</p>
                </div>
            </div>

        </div>

        <div v-if="entries == ''" >
            <p> Want to create an entry for <b>{{search}}</b> ? Click 
            <router-link :to ="{name:'CreateEntry',query:{subject:search}}">
                here
            </router-link>
            </p>
        </div>

        

    </div>


</template>

<script>

import Quill from 'quill'

import axios from 'axios'


export default {
    data() {
        return {
            entries: '',
            search:'',
        }
    },

    created() {
        this.nav_show();
        this.search = this.$route.query.search;
        this.get_data();
    },


    methods: {
        
        get_data(){
                   
            const _this = this;
            _this.entries ="";

            if (_this.search ==''){
                axios.get("/entry/entries/",)
                .then(response => {
                    this.entries = response.data
                })
            }



            else {
                axios.get("entry/entries/",
                    {
                        params:{
                            'search': _this.search
                        }
                    }
                )
                .then (res =>{
                    console.log(res);
                    this.entries = res.data;
                })
                .catch(res=>{
                    console.log("catching error");
                    })
                }
        }
    },

    name: 'EntryList',
    inject: ['nav_show'],

    watch:{

        // inspect the router

        $route(to,from){
            console.log(from);
            console.log(to);
            if (from.name==='EntryList' && to.name=='EntryList'){
                console.log("fetching data")
                this.search = this.$route.query.search;
                this.get_data();
                return;
            }

        },

    },

}
</script>

<style>
.entry {
    margin-top: 20px;
    margin-bottom: 20px;
}
</style>
