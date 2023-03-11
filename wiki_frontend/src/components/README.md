## InputList

Users can input as many inputs as they want. By clicking + sign to add a new tag. (bootstrap required)

to use that, an event listener should be written in the backend 

```vue
<InputList ref="inputTags" @updateInput='addNewTag' message="Add New Tags"
    input_placeholder="Input a new tag" />
```

must have an @updateInput in the parent component 

```vue
<script>
export default {
    data(){
        return {
            tag_new_temp:[]
        }
    },

    methods:{
        addNewTag(tag){
            this.tag_new_temp=tag;
        },
    }
}
</script>