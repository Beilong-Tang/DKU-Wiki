<!-- See all the posts in home page -->
<template>
    <div>


    </div>

    <div class="container">

        <div class="row">
            <div v-if="search && tag_chose.length!=0">
                You are seeing <span class="text-primary">{{ search }}</span> under tag <span class="text-primary">{{ tag_chose[0] }}</span>. 
            </div>

            <div v-else-if="search && tag_chose.length==0">
                You are seeing <span class="text-primary">{{ search }}</span>. 
            </div>

            <div v-else-if="!search && tag_chose.length==0">
                You are seeing all the results.
            </div>

            <div v-else>
                You are seeing all the wiki entries under tag <span class="text-primary">{{ tag_chose[0] }}</span>.
            </div> 

            <br>
            <br>



            <div class="list-group">
                <button class="list-group-item list-group-item-action" aria-current="true" v-for="entry in entries"
                    :key="entry.id" @click="toPost(entry.id)">
                    <!-- <router-link :to="{ name: 'DetailEntry', params: { id: entry.id } }"> -->
                    <div class="d-flex w-100 justify-content-center">
                        <h4 class="mb-1" style="color:#1674A9">{{ entry.title }}</h4>
                    </div>
                    <p class="mb-1 text">{{ entry.content_min }}</p>
                    <div class="d-flex w-100 justify-content-around">
                        <small class="text-muted">Created: {{ entry.create_date }}</small>
                        <small class>{{ entry.client.nickname }}</small>
                        <div><span v-for="item in entry.tag" :key="item" class="badge bg-primary me-1">{{ item }}</span>
                        </div>
                    </div>
                    <!-- </router-link> -->
                </button>
            </div>

            <div v-if="entries == ''">
                <p> No results</p>
            </div>

            <!-- <Pagination @updatePagenumber="test" :page_number="page_number" :total_page_number="page_length" /> -->
            <div>
                <div class="d-inline-block" v-if="entries != '' ">
                    <paginate v-model="page_number" :page-count="page_length" :page-range="3" :margin-pages="2"
                        :click-handler="test" :prev-text="'Prev'" :next-text="'Next'" :container-class="'pagination'"
                        :page-class="'page-item'">
                    </paginate>
                </div>
            </div>


        </div>




    </div>
</template>

<script>

import axios from 'axios'

import { Data } from './utils/Data.js'

import Pagination from '../components/Pagination.vue'

import Paginate from "vuejs-paginate-next";

export default {

    components: { Pagination, Paginate },



    data() {
        return {
            entries: '',
            search: '',
            tag_chose: [],
            page_number: this.$route.query.page_number,
            page_length: null
        }
    },

    created() {
        this.nav_show();
        this.search = this.$route.query.search;
        if (!this.$route.query.tags) {
            this.tag_chose = ""
        }
        else {
            this.tag_chose = this.$route.query.tags
        }
        this.get_data();
    },


    methods: {

        test(page_number) {
            this.page_number = page_number
            // this.get_data()
            this.$router.push({ name: 'EntryList', query: { page_number: page_number, tags: this.tag_chose, search:this.search } });
        },

        toPost(id) {
            this.$router.push({ name: 'DetailEntry', params: { id: id } });
        },

        get_data() {

            const _this = this;
            _this.entries = "";


            axios.get("entry/entries/",
                {
                    params: {
                        'search': _this.search,
                        'tags': _this.tag_chose.toString(),
                        'page': _this.page_number - 1,
                    }
                }
            )
                .then(res => {
                    var length = res.data.pop()
                    _this.page_length = length.length;
                    let data = new Data(res.data)
                    data.change_date()
                    this.entries = res.data

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
                if (!this.$route.query.tags) {
                    this.tag_chose = ""
                }
                else {
                    this.tag_chose = this.$route.query.tags
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

.text {
    overflow: hidden;
    text-overflow: ellipsis;
    -webkit-line-clamp: 2;
}
</style>
