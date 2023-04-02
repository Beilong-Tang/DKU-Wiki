<template>
    <div class="container">

        <div class="input-group mb-3">
            <div class="input-group-prepend">
                <span class="input-group-text" id="basic-addon1">Title</span>
            </div>
            <input type="text" class="form-control" placeholder="Put your title here" aria-label="Username"
                aria-describedby="basic-addon1" v-model="subject">
        </div>

        <button type="button" class="btn btn-primary mb-1" @click="submit()">Submit</button>

        <br>

        <InputPart v-if="taglist" @updateInput='confirmTag' :inputlist=tags :taglist=taglist />
        <!-- <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#tags">Tags</button> -->

        <v-md-editor v-model="content" mode="editable"></v-md-editor>

    </div>
</template>

<script>

import axios from 'axios';
import Quill from 'quill'
import { getCookie } from './utils/utils'
import InputList from '../components/InputList.vue'
import InputPart from '../components/InputPart.vue'

export default {
    data() {
        return {
            subject: "",
            id: this.$route.query.id,
            content: "",
            quill: null,
            tags: [], //the tag value that to be submitted
            taglist: null //all the existing tags
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
                console.log(_this.taglist);
            });
    },
    methods: {

        confirmTag(tag) {
            this.tags = tag
        },

        submit() {
            const length = this.content;
            if (length === 1) {
                alert("The content cannot be empty!");
                return;
            }
            const formData = {
                title: this.subject,
                content: this.content,
                tag: this.tags
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
    components: { InputList, InputPart }
}

</script>

<style>
/* .ql-toolbar{
    display:none
} */</style>