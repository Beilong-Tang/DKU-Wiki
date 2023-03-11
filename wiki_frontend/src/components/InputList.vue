<template>
    <!-- {{ InputUpdated }} -->

    <div class="form-check" v-for="_input in InputUpdated" :key="_input">
        <input class="form-check-input tagcheck" type="checkbox" :value="_input" v-model = "input"  id="flexCheckDefault">
        <label class="form-check-label" for="flexCheckDefault">
            {{ _input }}
        </label>
    </div>

    <div class="input-group" v-if="isTyping">
        <input v-model="input_value" type="text" class="form-control" :placeholder="input_placeholder"
            aria-label="Recipient's username with two button addons">
        <button class="btn btn-outline-secondary" type="button" @click="confirm()">√</button>
        <button class="btn btn-outline-secondary" type="button" @click="cancel()">X</button>
    </div>

    <div class="mt-2 text-start">
    <button v-if="!isTyping" type="button" class="btn btn-primary add" @click="addInput()">{{ message }}</button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            input_value: "",

            input: this.$props.inputlist,

            isTyping: false, // check if the client is currently typing.

        }
    },
    props:['message', "input_placeholder","inputlist"],
    emits: ["updateInput"],
    methods: {
        // confirm the input
        confirm() {

            const _this = this;

            _this.input.push(_this.input_value)

            // _this.tag_new_temp.push(_this.input_value)
            this.input_value = ""
            this.isTyping = false;
        },

        //cancel the input 
        cancel() {

            this.isTyping = false;
            this.input_value = "";

        },

        addInput() {

            this.isTyping = true;

        },

        reverseChange(data){
            this.input = data;
        },
    },
    
    computed:{
        InputUpdated(){

            this.$emit("updateInput", this.input)

            return this.input
        }
    }


}


</script>

<style>
.add{
    font-size:12px;
}

</style>