<template>
    <div class="input-group mb-3">
            
            <span class="input-group-text">Tags</span>
            <input type="text" class="form-control" aria-label="Text input with dropdown button" :value="tags" readonly>
            <button class="btn btn-primary" type="button" data-bs-toggle="modal"
                aria-expanded="false" data-bs-target="#tags" >Add a Tag</button>
            
        </div>


        <br>



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

</template>


<script>
import InputList from './InputList.vue'
export default {
    components: {InputList},

    props:["inputlist","taglist"],
    emits: ["updateInput"],

    data(){
        return{ 
            taglist:this.$props.taglist, //all the existing taglist 
            tag_temp: [],
            tag_temp_origin:[],
            tag_new_temp: [],
            tag_new_origin: [],
            tags:this.$props.inputlist, // the current input that is passing in 
        }

    },
    methods:{
         addNewTag(tag) {
            this.tag_new_temp = tag;
        },


        // reverse the change of the tag.
        reverseTags() {
            this.tag_temp = this.tag_temp_origin;
            this.tag_new_temp = this.tag_new_origin
            this.$refs.inputTags.reverseChange(this.tag_new_origin)
        },

        //confirm tags
        confirmTags() {
            this.tag_temp_origin = this.tag_temp;
            this.tag_new_origin = this.tag_new_temp;
            this.tags = this.tag_temp.concat(this.tag_new_temp);
            
            this.$emit("updateInput",this.tags)
        },

    },
    created(){
        
    }


}

</script>