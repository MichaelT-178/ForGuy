<template>
    <div class="container">
        <h1 class="gh-header">{{ text[1].title }}</h1>
        <p class="description">{{ text[1].desc }}</p>
        <img src="../../assets/React.png" alt="React" class="react-pic"/>

        <!-- Display Links -->
        <div v-for="(group, groupName) in displayLinks" :key="groupName">
            <h2 class="gh-header-two" style="margin-top: -3px;">{{ group.title }}</h2>
            <p class="description-two">{{ group.desc }}</p>
            <div v-for="link in group.links" :key="link.id">
                <p class="bullet-pt"><span class="bullet-pt-span">{{ link.id }}</span>
                    <span :class="{ 'display-link': currentSection !== link.ref, 'active-link': currentSection === link.ref }"
                          @click="toggleSection(link.ref)">
                        {{ link.name }}
                    </span>
                </p>
            </div>
        </div>
        
        <p class="scroll-down" ref="scrollToRef">INVISIBLE SCROLL DOWN</p>

        <div v-for="(set, index) in filteredSets" :key="index">
            <h2 class="gh-header-two">{{ set.Info[0].title }}</h2>
            <p class="description-two" v-html="createHyperLink(set.Info[0].desc)"></p>
            <div v-for="point in set.Instructions" :key="point.id">
                <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}</span>
                    <span v-html="createDownloadLink(createHyperLink(point.instruction))"></span>
                </p>
                <span v-if="point.Code">
                    <CodeBlock :codeInfo="point.Code" style="margin-bottom: 20px;"></CodeBlock>
                </span>
            </div>
        </div>

        <p class="scroll-up-btn" @click="scrollToTop">{{ text[0].scrollToTop }}</p>
    </div>
</template>


<script setup>
import { computed, ref, nextTick, onMounted, watch } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { createHyperLink, highlightLinkText, createDownloadLink } from "../../utils/Markdown.vue";
import CodeBlock from '../../components/Code/CodeBlock.vue';
import AllData from '../../data/CompSci/Instructions/DisplayLinks.json';
import { AllSets } from '../../data/CompSci/Instructions/InstructionSets.vue';


const router = useRouter();
const route = useRoute();

const jsonData = ref(AllData);
const text = jsonData.value["Text"];
const displayLinks = jsonData.value["DisplayLinks"];


const scrollToRef = ref(null);

const currentSection = ref(localStorage.getItem('currentSection') || 'node');

// const filteredSets = computed(() => {

//     if (jsonData.value.MultiSet) {
//         console.log("HERE FOUND ITS HERE");

//         return jsonData.value.MultiSet.filter(set => set.Info[0].ref === currentSection.value);
//     } else {
//         return AllSets.filter(set => set.Info[0].ref === currentSection.value);
//     }
// });

const filteredSets = computed(() => {
    let allFilteredSets = [];

    AllSets.forEach(set => {
        if (set.MultiSet) {
            // Include all sets from MultiSet without filtering by section
            allFilteredSets.push(...set.MultiSet);
        } else {
            // Keep the filtering for regular sets
            if (set.Info[0].ref === currentSection.value) {
                allFilteredSets.push(set);
            }
        }
    });

    return allFilteredSets;
});

// const filteredSets = computed(() => {
//     let allFilteredSets = [];

//     AllSets.forEach(set => {
//         if (set.MultiSet) {
//             const filteredMultiSets = set.MultiSet.filter(set => set.Info[0].ref === currentSection.value);
//             allFilteredSets.push(...filteredMultiSets);
//         } else {

//             if (set.Info[0].ref === currentSection.value) {
//                 allFilteredSets.push(set);
//             }
//         }
//     });

//     return allFilteredSets;
// });


const toggleSection = (section) => {
    currentSection.value = section;
    localStorage.setItem('currentSection', section);

    router.push(`/CompSci/SetupProjects/${section}`);

    nextTick(() => {
        if (scrollToRef.value) {
            scrollToRef.value.scrollIntoView({ behavior: 'smooth' });
        }
    });
};

const scrollToTop = () => {
    window.scrollTo({
        top: 400,
        behavior: 'smooth'
    });
};

//Gets the ref from the end of the link
const getSectionFromLink = (path) => {
    const segments = path.split('/').filter(segment => segment !== '');
    return segments.length > 0 ? segments[segments.length - 1] : '';
}

// Updates if the user is using the SearchBar
watch(() => route.params.section, (newSection, oldSection) => {
    if (newSection != "") {
        toggleSection(newSection);
    }
});

onMounted(() => {
    const navigationEntries = performance.getEntriesByType('navigation');

    const currentLink = route.fullPath;
    const linkSection = (currentLink.includes("SetupProjects/")) ? getSectionFromLink(currentLink) : null;


    if (navigationEntries.length > 0 && navigationEntries[0].type === 'reload') {
        // Page was just refreshed do nothing
    } else {
        // Came from a different route
        const section = linkSection ?? 'node';

        currentSection.value = section;
        localStorage.setItem('currentSection', section);

        if (linkSection != null) {
            nextTick(() => {
                if (scrollToRef.value) {
                    scrollToRef.value.scrollIntoView({ behavior: 'smooth' });

                    setTimeout(() => {
                        window.scrollBy(0, -25);
                    }, 850);
                }
            });
        }
    }
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
    height: 290px;
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
    width: 640px;
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

.scroll-up-btn {
    text-align: center; 
    font-size: 30px; 
    margin-top: 15px;
    margin-right: 40px;
    cursor: pointer;
    color: blue;
    margin-bottom: 70px;
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