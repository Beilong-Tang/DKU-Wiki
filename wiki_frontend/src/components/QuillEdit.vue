<template>

    <QuillEditor v-if="!edit" theme="bubble"  :readOnly="true" 
    @ready="setContent($event)"
    />
    
    <QuillEditor v-else theme="snow" @ready="setContent($event)" 
    @textChange="emitContent($event)"
    />

</template>

<script>
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css';
import '@vueup/vue-quill/dist/vue-quill.bubble.css';

export default {
    components:{QuillEditor},
    props:["content"],
    data(){
        return{
            contentRaw:this.$props.content,
            contentNew:this.$props.content,
            quillEdit:null,

            edit:false,
        }
    },

    methods:{
        //refs
        updateEdit(){
            this.edit = !this.edit;
        },
        //refs
        getContent(){
            return this.contentNew
        },

        emitContent(event){

            if (this.quillEdit==null){
                return;
            }
            this.contentNew = this.quillEdit.getContents()

        },

        setContent(quill){
            quill.setContents(JSON.parse(this.contentRaw))
            this.quillEdit = quill;
        }
    },

}


</script>