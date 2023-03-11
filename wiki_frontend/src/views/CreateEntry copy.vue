<template>
    <div class="container">

        <h1>{{ subject }}</h1>

        <button type="button" class="btn btn-primary mb-1" @click="submit()">Submit</button>

        <br>

        <!-- <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#tags">Tags</button> -->

        <div class="input-group mb-3">
            
            <span class="input-group-text">Tags</span>
            <input type="text" class="form-control" aria-label="Text input with dropdown button" :value="tags" readonly>
            <button class="btn btn-primary" type="button" data-bs-toggle="modal"
                aria-expanded="false" data-bs-target="#tags" >Add a Tag</button>
            
        </div>


        <br>

        {{ tags }}


        <div class="modal fade" id="tags" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="form-check" v-for="tag in taglist" key="id">
                            <input class="form-check-input tagcheck" type="checkbox" :value="tag.name" v-model="tag_temp"
                                id="flexCheckDefault">
                            <label class="form-check-label" for="flexCheckDefault">
                                {{ tag.name }}
                            </label>
                        </div>

                        <InputList ref="inputTags" @updateInput='addNewTag' message="Add New Tags"
                            input_placeholder="Input a new tag" :inputlist="tags" />

                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
                            @click="reverseTags">Close</button>
                        <button type="button" class="btn btn-primary" data-bs-dismiss="modal"
                            @click="confirmTags">Confirm</button>
                    </div>
                </div>
            </div>
        </div>

        <div id="editor" style="min-height:500px">

        </div>

    </div>
</template>

<script>

import axios from 'axios';
import Quill from 'quill'
import { getCookie } from './utils/utils'
import InputList from '../components/InputList.vue'

export default {
    data() {
        return {
            subject: this.$route.query.subject,
            id: this.$route.query.id,
            content: "",
            quill: null,
            tags: [], //the tag value that to be submitted
            tag_temp: [],
            tag_new_temp: [],
            tag_new_origin: [],
            taglist: [] //all the existing tags
        };
    },
    mounted() {
        // check if it is modifying or creating 
        if (this.id === undefined) {
            this.quill = new Quill("#editor", {
                theme: "snow",
            });
            return;
        }
    },
    created() {
        //
        const _this = this;
        axios.get("entry/tags")
            .then(res => {
                _this.taglist = res.data;
            });
    },
    methods: {

        addNewTag(tag) {
            this.tag_new_temp = tag;
        },


        // reverse the change of the tag.
        reverseTags() {
            this.$refs.inputTags.reverseChange(this.tag_new_origin)
        },

        //confirm tags
        confirmTags() {
            this.tag_new_origin = this.tag_new_temp;
            this.tags = this.tag_temp.concat(this.tag_new_temp);
        },

        submit() {
            const content = JSON.stringify(this.quill.getContents());
            var length = this.quill.getLength();
            if (length === 1) {
                alert("The content cannot be empty!");
                return;
            }
            const formData = {
                title: this.subject,
                content: content,
                tag:this.tags
            };
            axios.post("/entry/create_entry/", formData, {
                headers: { "X-CSRFTOKEN": getCookie("csrftoken") }
            })
                .then(res => {
                    console.log("post successfully created");
                    this.$router.push({ name: "EntryList", params: { search: this.subject } });
                })
                .catch(res => {
                    console.log(res);
                });
        },
    },
    watch: {
        // inspect the router
        $route(to, from) {
            console.log("creating entry");
        }
    },
    components: { InputList }
}

</script>

<style>/* .ql-toolbar{
    display:none
} */</style>