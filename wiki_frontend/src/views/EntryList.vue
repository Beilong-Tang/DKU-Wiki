<!-- See all the posts in home page -->
<template>
    <div>


    </div>

    <div class="container">
        
            <div class="row">

            <div class="list-group">
                <button class="list-group-item list-group-item-action" aria-current="true"
                 v-for="entry in entries" :key="entry.id" @click="toPost(entry.id)">
                    <!-- <router-link :to="{ name: 'DetailEntry', params: { id: entry.id } }"> -->
                    <div class="d-flex w-100 justify-content-center">
                        <h4 class="mb-1" style="color:#1674A9">{{ entry.title }}</h4>
                    </div>
                    <p class="mb-1 text">{{ entry.content_min}}</p>
                     <div class="d-flex w-100 justify-content-around">
                        <small class="text-muted">{{ entry.create_date }}</small>
                        <small class>{{ entry.client.nickname }}</small>
                        <div><span v-for="item in entry.tag" :key="item" class="badge bg-primary me-1">{{ item }}</span></div>
                    </div>
                    <!-- </router-link> -->
                </button>
            </div>

        </div>

        <div v-if="entries == ''">
            <!-- <p> Want to create an entry for <b>{{ search }}</b> ? Click
                <router-link :to="{ name: 'CreateEntry', query: { subject: search } }">
                    here
                </router-link>
            </p> -->
            <p> No results</p>
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
            search: '',
            tag_chose:[],
        }
    },

    created() {
        this.nav_show();
        this.search = this.$route.query.search;
        if (!this.$route.query.tags){
            this.tag_chose=""
        }
        else{
            this.tag_chose=this.$route.query.tags
        }
        this.get_data();
    },


    methods: {

        toPost(id){
            this.$router.push({ name: 'DetailEntry', params: { id: id } });
        },

        get_data() {

            const _this = this;
            _this.entries = "";


                axios.get("entry/entries/",
                    {
                        params: {
                            'search': _this.search,
                            'tags':_this.tag_chose.toString(),
                        }
                    }
                )
                    .then(res => {
                        console.log(res);
                        this.entries = res.data;
                    })
                    .catch(res => {
                        console.log("catching error");
                    })
        }
    },

    name: 'EntryList',
    inject: ['nav_show'],

    watch: {

        // inspect the router

        $route(to, from) {
            if (from.name === 'EntryList' && to.name == 'EntryList') {
                console.log("fetching data")
                this.search = this.$route.query.search;
                if (!this.$route.query.tags){
                    this.tag_chose=""
                }
                else{
                    this.tag_chose=this.$route.query.tags
                }
                ;
                console.log(this.tag_chose)
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

.text{
     overflow: hidden;
  text-overflow: ellipsis;
  -webkit-line-clamp: 2;
}
</style>
