<template>
    <div class="container">
        <h1 class="gh-header">{{ text[0].title }}</h1>
        <p class="description">{{ text[0].desc }}</p>

        <img src="../../assets/React.png" alt="React" class="react-pic"/>

        <!-- Scroll Links -->
        <h2 class="gh-header-two" style="margin-top: -3px;" ref="scrollLinksRef">{{ text[1].title }}</h2>
        <p class="description-two">{{ text[1].desc }}</p>
        <div v-for="link in scrollLinks" :key="link.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ link.id }}
                </span><span v-html="createRefContent(link)"></span></p>
        </div>
        

        <!-- Setup Node.js -->
        <h2 class="gh-header-two" ref="nodeRef">{{ text[2].title }}</h2>
        <p class="description-two">{{ text[2].desc }}</p>

        <div v-for="point in setupNode" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}
                </span><span v-html="highlightLinkText(point.instruction)" v-bind="point.ref ? { ref : point.ref } : {}"></span></p>
            <span v-if="point.Code"><CodeBlock :codeInfo="point.Code" style="margin-bottom: 20px;"></CodeBlock></span>
        </div>



        <!-- Setup Vue -->
        <h2 class="gh-header-two" ref="vueRef">{{ text[3].title }}</h2>
        <p class="description-two">{{ text[3].desc }}</p>

        <div v-for="point in setupVue" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}
                </span><span v-html="point.instruction" v-bind="point.ref ? { ref : point.ref } : {}"></span></p>
            <span v-if="point.Code"><CodeBlock :codeInfo="point.Code" style="margin-bottom: 20px;"></CodeBlock></span>
        </div>

        




    </div>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import AllData from '../../data/CompSci/SetupProjects.json';
import { createHyperLink, highlightLinkText } from "../../utils/Markdown.vue";
import CodeBlock from '../../components/Code/CodeBlock.vue';

const jsonData = ref(AllData);

const text = jsonData.value["Text"];
const scrollLinks = jsonData.value["ScrollLinks"];
const setupNode = jsonData.value["SetupNode"];
const setupVue = jsonData.value["SetupVue"];

const createRefContent = (refVal) => {
    return `<span><span href="#" class="scroll-down" data-ref-name="${refVal.ref}">${refVal.name}</span>.</span>`;
}



const scrollLinksRef = ref(null);
const nodeRef = ref(null);
const vueRef = ref(null);





const scrollToRef = (refName) => {

    const offset = 75;

    const refs = {
        scrollLinksRef,
        nodeRef,
        vueRef
    };

    const targetElement = refs[refName]?.value;

    if (targetElement) {
        const elementPosition = targetElement.getBoundingClientRect().top + window.scrollY;
        const offsetPosition = elementPosition - offset;

        window.scrollTo({
            top: offsetPosition,
            behavior: 'smooth'
        });
    } else {
        console.warn("No target element found for refName:", refName);
    }
}

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
};

onMounted(() => {
    document.querySelectorAll('.scroll-down').forEach(element => {
        element.addEventListener('click', (event) => {
            event.preventDefault();
            const refName = event.target.getAttribute('data-ref-name');
            scrollToRef(refName);
        });
    });
});

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

:deep(.scroll-down) {
    text-decoration: none;
    color: blue;
    cursor: pointer;
}

:deep(.scroll-down:hover) {
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