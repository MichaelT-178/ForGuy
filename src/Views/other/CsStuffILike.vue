<template>
    <div class="container">
        <h1 class="gh-header">CS Stuff I like</h1>
        <p class="description">These are various computer science and programming-related things I like.</p>

        <h2 class="gh-header-two">Comp Sci Stuff I like</h2>
        <p class="description-two">These are various computer science related things I like.</p>

        <div v-for="point in csStuff" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}
                </span><span v-html="createHyperLink(point.description)"></span>
            </p>
        </div>

        <h1 class="header-three">Goated Syntax</h1>
        <p class="description-three">These are code snippets that show syntax and functionality I like.</p>

        <div v-for="code in codeSyntax" :key="code.Name" class="code-blocks">
            <CodeBlock :codeInfo="code"></CodeBlock>
        </div>

        <p class="scroll-up-btn" @click="scrollToTop">Scroll To Top</p>

    </div>
</template>


<script setup>
import { ref } from 'vue';
import AllData from '../../data/Other/CsStuffILike.json';
import CodeBlock from '../../components/Code/CodeBlock.vue';
import { createHyperLink } from "../../components/FormatLinks.vue";

const jsonData = ref(AllData);

const csStuff = jsonData.value["CsStuff"];
const codeSyntax = jsonData.value["Code"];

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
};

</script>

<style scoped>

.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}

.gh-header {
    text-align: left;
    border-bottom: 1.5px solid #d8dee4;
    padding-bottom: 7px;
    width: 690px;
}

.description {
    margin-top: -8px;
    font-size: 19px;
    width: 690px;
}

.bullet-pt {
    display: flex;
    align-items: flex-start;
    margin-top: -10px;
    margin-left: 20px;
    margin-bottom: 24px;
    font-size: 19px;
    width: 690px;
}

.bullet-pt-span {
    background-color: darkblue;
    border-radius: 50%;
    color: white;
    font-size: 15px;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 24px;
    height: 24px;
    min-width: 24px;
    margin-right: 10px;
    user-select: none;
    margin-bottom: 10px;
}

.gh-header-two {
    text-align: left;
    width: 690px;
}

.description-two {
    margin-top: -15px;
    font-size: 19px;
    width: 690px;
}


.header-three {
    margin-top: 40px;
    margin-bottom: -10px;
}

.description-three {
    /* margin-top: -15px; */
    font-size: 21px;
    margin-bottom: 10px;
}

.scroll-up-btn {
    text-align: center; 
    font-size: 23.5px; 
    margin-top: 25px;
    margin-bottom: 75px;
    margin-right: 40px;
    cursor: pointer;
    color: blue;
}

.scroll-up-btn:hover {
    color: darkblue;
    text-decoration: underline;
}

@media (max-width: 700px) {

    .gh-header {
        width: 490px;
    }
    
    .description {
        width: 490px;
    }
    
    .gh-header-two {
        width: 490px;
    }

    .description-two {
        width: 490px;
    }
}

</style>