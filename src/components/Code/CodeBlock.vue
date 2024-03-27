<template>
  <div class="container">
    <div class="text-container">
      <h2 class="code-name">{{ codeInfo.Name }}</h2>
      <p class="description">{{ codeInfo.Description }}</p>
    </div>
    <div class="code-block">
      <div class="copy-bar">
        <span class="language-name">{{ codeInfo.Language ?? "Command"}}</span>
        <span class="material-icons copy-icon" 
             :class="{'icon-done': copyIcon === 'done'}" 
             :style="{ color: copyIcon === 'done' ? '#00FF4D' : getLanguageColor }"
             @click="copyCode"
         >{{ copyIcon }}</span>
      </div>
      <pre><code v-html="highlightedCode"></code></pre>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import Prism from 'prismjs';
import 'prismjs/components/prism-python';
import 'prismjs/components/prism-java';
import 'prismjs/components/prism-javascript';
import 'prismjs/components/prism-swift';
import 'prismjs/components/prism-json';
import 'prismjs/themes/prism-coy.css';
import './custom.css';

const props = defineProps({
  codeInfo: {
    type: Object,
    default: () => ({
      Name: "",
      Description: "",
      Language: "",
      FormatCode: "",
      CopyCode :""
    }),
    required: true,
  },
});

const copyIcon = ref('content_copy');

const copyCode = () => {
  navigator.clipboard.writeText(props.codeInfo.CopyCode)
    .then(() => {
      copyIcon.value = 'done';
      setTimeout(() => copyIcon.value = 'content_copy', 2000);
    })
    .catch(err => {
      console.error("Failed to copy code to clipboard! ", err)
    });
};

const highlightedCode = computed(() => {
  if (props.codeInfo.Language === null) {
    return `<span style="color: #C1C1C1;">${props.codeInfo.FormatCode}</span>`;
  }

  const language = props.codeInfo.Language.toLowerCase();
  const prismLanguage = Prism.languages[language] || Prism.languages.plain;
  return Prism.highlight(props.codeInfo.FormatCode, prismLanguage, language);
});


const getLanguageColor = computed(() => {

  //I prefer this approach over a switch statement
  const colors = {
    python: '#3572A5',
    java: '#C6821E',
    javascript: '#f1e05a',
    typescript: '#3178c6',
    swift: '#F05138',
    ruby: '#701516',
    vue: '#41b883',
    json: '#FF9A00'
  }

  if (props.codeInfo.Language === null) return "#DFC200";

  const color = props.codeInfo.Language.toLowerCase().trim();

  return colors[color]

});

</script>


<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.text-container {
  max-width: 700px; 
}

.code-name {
  margin-left: 4px;
  font-size: 23px;
}

.description {
  margin-top: -15px;
  margin-left: 4px;
  font-size: 17px;
}

.code-block {
  width: 700px;
  margin: 20px 0;
  border: 1px solid #ddd;
  border-radius: 5px;
  background-color: #282C34;
  color: white;
  margin-top: -5px;
}

.language-name {
  color: #D5D5D5;
  font-size: 10px;
}

.copy-icon {
  cursor: pointer;
  font-size: 22px;
}

.copy-icon:hover {
  filter: brightness(80%);
}

.icon-done {
  color: #00FF4D;
}

.icon-done:hover {
  color: #00FF4D;
}

.copy-bar {
  display: flex;
  justify-content: space-between;
  background-color: gray;
  padding: 5px;
}

.language-name {
  flex-grow: 1;
  font-size: 20px;
  margin-left: 6px;
}

code {
  background-color: #282C34;
  border-radius: 3px;
  font-size: 14px;
  margin-left: 16px;
  line-height: 20px;
}

</style>
