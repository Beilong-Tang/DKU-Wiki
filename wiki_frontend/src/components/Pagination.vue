<template>


<div v-if="total_page_number>=3">

    <div v-if="page_number==1">
        <nav aria-label="..." class="d-inline-block">
            <ul class="pagination">
                <li class="page-item disabled">
                    <a class="page-link" href="#" tabindex="-1">Previous</a>
                </li>
                <li class="page-item active"><a class="page-link" >{{ page_number}}</a></li>
                <li class="page-item"><a class="page-link" href="#" @click.prevent = "forwardPageNumber()">{{ page_number+1 }} </a></li>
                <li class="page-item"><a class="page-link" href="#" @click.prevent = "toPageNumber(page_number+2)">{{ page_number + 2 }}</a></li>
                <li class="page-item">
                    <a class="page-link" href="#" @click.prevent = "forwardPageNumber()">Next</a>
                </li>
            </ul>
        </nav>
    </div>

    <div v-else-if="page_number==total_page_number">
        <nav aria-label="..." class="d-inline-block">
            <ul class="pagination">
                <li class="page-item">
                    <a class="page-link" href="#" @click.prevent = "backwardPageNumber()">Previous</a>
                </li>
                <li class="page-item"><a class="page-link" href="#">{{ page_number-2}}</a></li>
                <li class="page-item"><a class="page-link" href="#" @click.prevent = "backwardPageNumber()">{{ page_number-1}} </a></li>
                <li class="page-item active"><a class="page-link" >{{ page_number}}</a></li>
                <li class="page-item disabled">
                    <a class="page-link" href="#" tabindex="-1">Next</a>
                </li>
            </ul>
        </nav>
    </div>

    <div v-else>
        <nav aria-label="..." class="d-inline-block">
            <ul class="pagination">
                <li class="page-item ">
                    <a class="page-link" href="#" @click.prevent = "backwardPageNumber()">Previous</a>
                </li>
                <li class="page-item"><a class="page-link" href="#" @click.prevent = "backwardPageNumber()">{{ page_number-1}}</a></li>
                <li class="page-item active"><a class="page-link" >{{ page_number}} </a></li>
                <li class="page-item"><a class="page-link" href="#" @click.prevent = "forwardPageNumber()">{{ page_number+1}}</a></li>
                <li class="page-item ">
                    <a class="page-link" href="#" @click.prevent = "forwardPageNumber()">Next</a>
                </li>
            </ul>
        </nav>
    </div>

</div>

<div v-else-if="total_page_number==2">

    <div v-if="page_number==1">
        <nav aria-label="..." class="d-inline-block">
            <ul class="pagination">
                <li class="page-item disabled">
                    <a class="page-link" href="#" tabindex="-1">Previous</a>
                </li>
                <li class="page-item active"><a class="page-link" href="#">{{ page_number}}</a></li>
                <li class="page-item"><a class="page-link" href="#" @click.prevent = "forwardPageNumber()">{{ page_number+1 }} </a></li>
                <li class="page-item">
                    <a class="page-link" href="#" @click.prevent = "forwardPageNumber()">Next</a>
                </li>
            </ul>
        </nav>
    </div>

    <div v-else-if="page_number==total_page_number">
        <nav aria-label="..." class="d-inline-block">
            <ul class="pagination">
                <li class="page-item">
                    <a class="page-link" href="#" @click.prevent = "backwardPageNumber()">Previous</a>
                </li>
                <li class="page-item"><a class="page-link" href="#" @click.prevent = "backwardPageNumber()">{{ page_number-1}} </a></li>
                <li class="page-item active"><a class="page-link" href="#">{{ page_number}}</a></li>
                <li class="page-item disabled">
                    <a class="page-link" href="#" tabindex="-1">Next</a>
                </li>
            </ul>
        </nav>
    </div>

    <div v-else>
        <nav aria-label="..." class="d-inline-block">
            <ul class="pagination">
                <li class="page-item ">
                    <a class="page-link" href="#" @click.prevent = "backwardPageNumber()">Previous</a>
                </li>
                <li class="page-item"><a class="page-link" href="#" @click.prevent = "backwardPageNumber()">{{ page_number-1}}</a></li>
                <li class="page-item active"><a class="page-link" href="#">{{ page_number}} </a></li>
                <li class="page-item"><a class="page-link" href="#" @click.prevent = "forwardPageNumber()">{{ page_number+1}}</a></li>
                <li class="page-item ">
                    <a class="page-link" href="#" @click.prevent = "forwardPageNumber()">Next</a>
                </li>
            </ul>
        </nav>
    </div>

</div>



</template>

<script>

export default{

    props:["page_number","total_page_number"],
    emits:["updatePagenumber"],

    methods:{
        forwardPageNumber(){
            var page_number = this.page_number
            page_number +=1
            this.$emit("updatePagenumber", page_number)
       },

        backwardPageNumber(){
            var page_number = this.page_number
            page_number -=1
            this.$emit("updatePagenumber", page_number)
        },

        toPageNumber(page){
            var page_number = this.page_number
            page_number =page
            this.$emit("updatePagenumber", page_number)
        }

    }
}

</script>

<style></style>