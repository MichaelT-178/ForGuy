<template>
    <div class="container">
        <h1 class="gh-header">{{ text[0].title }}</h1>
        <p class="description">{{ text[0].desc }}</p>

        <img src="../../assets/React.png" alt="React" class="react-pic"/>

        <!-- Display Links -->
        <h2 class="gh-header-two" style="margin-top: -3px;">{{ text[1].title }}</h2>
        <p class="description-two">{{ text[1].desc }}</p>
        <div v-for="link in displayLinks" :key="link.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ link.id }}</span>
                <span :class="{ 'display-link': currentSection !== link.ref, 'active-link': currentSection === link.ref }" 
                      @click="toggleSection(link.ref)">
                    {{ link.name }}
                </span>
            </p>
        </div>
        
        <p class="scroll-down" ref="scrollToRef">INVISIBLE SCROLL DOWN</p>

        <!-- Setup Node.js -->
        <div v-if="currentSection === 'node'">
            <h2 class="gh-header-two">{{ text[2].title }}</h2>
            <p class="description-two">{{ text[2].desc }}</p>
            <div v-for="point in setupNode" :key="point.id">
                <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}</span><span v-html="highlightLinkText(point.instruction)" v-bind="point.ref ? { ref : point.ref } : {}"></span></p>
                <span v-if="point.Code"><CodeBlock :codeInfo="point.Code" style="margin-bottom: 20px;"></CodeBlock></span>
            </div>
        </div>


        <!-- Setup Vue -->
        <div v-if="currentSection === 'vue'">
            <h2 class="gh-header-two" ref="vueRef">{{ text[3].title }}</h2>
            <p class="description-two">{{ text[3].desc }}</p>
            <div v-for="point in setupVue" :key="point.id">
                <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}</span><span v-html="point.instruction" v-bind="point.ref ? { ref : point.ref } : {}"></span></p>
                <span v-if="point.Code"><CodeBlock :codeInfo="point.Code" style="margin-bottom: 20px;"></CodeBlock></span>
            </div>
        </div>

        <!-- Setup React -->
        <div v-if="currentSection === 'react'">
            <h2 class="gh-header-two">{{ text[4].title }}</h2>
            <p class="description-two">{{ text[4].desc }}</p>
            <div v-for="point in setupReact" :key="point.id">
                <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}</span><span v-html="createHyperLink(point.instruction)" v-bind="point.ref ? { ref : point.ref } : {}"></span></p>
                <span v-if="point.Code"><CodeBlock :codeInfo="point.Code" style="margin-bottom: 20px;"></CodeBlock></span>
            </div>
        </div>

    </div>
</template>


<script setup>
import { ref } from 'vue';
import AllData from '../../data/CompSci/SetupProjects.json';
import { createHyperLink, highlightLinkText } from "../../utils/Markdown.vue";
import CodeBlock from '../../components/Code/CodeBlock.vue';

const jsonData = ref(AllData);

const text = jsonData.value["Text"];
const displayLinks = jsonData.value["DisplayLinks"];
const setupNode = jsonData.value["SetupNode"];
const setupVue = jsonData.value["SetupVue"];
const setupReact = jsonData.value["SetupReact"];

const currentSection = ref('node');
const scrollToRef = ref(null);

const toggleSection = (section) => {
    currentSection.value = section;

    if (scrollToRef.value) {
        scrollToRef.value.scrollIntoView({ behavior: 'smooth' });
    }
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

.react-pic {
    width: 690px;
    height: 280px;
    margin-top: -5px;
    margin-bottom: 20px;
}

.description {
    margin-top: -8px;
    font-size: 19px;
    width: 690px;
}

.scroll-down {
    margin-bottom: -20px;
    visibility: hidden;
    user-select: none;
}

.display-link {
    text-decoration: none;
    color: blue;
    cursor: pointer;
}

.display-link:hover {
    text-decoration: underline;
    color: darkblue;
}

.active-link {
    text-decoration: underline;
    color: darkblue;
}

.gh-header-two {
    text-align: left;
    width: 690px;
}

.description-two {
    margin-top: -15px;
    font-size: 19px;
    width: 690px;
    margin-bottom: 27px;
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

@media (max-width: 700px) {
    .gh-header {
        width: 490px;
    }
    
    .description {
        width: 490px;
    }

    .react-pic {
        width: 490px;
        height: 200px;
    }
    
    .cmd-table {
        width: 490px;
    }

    .gh-header-two {
        width: 490px;
    }

    .description-two {
        width: 490px;
    }

    .bullet-pt {
        width: 490px;
    }
}

</style>