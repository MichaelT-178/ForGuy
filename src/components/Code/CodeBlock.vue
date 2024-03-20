<template>
  <div>
    <h2>{{ codeInfo.Name }}</h2>
    <p>{{ codeInfo.Description }}</p>
    <div class="code-block">
      <div class="copy-bar">
        <span class="language-name">{{ codeInfo.Language }}</span>
        <span class="material-icons copy-icon" 
             :class="{'icon-done': copyIcon === 'done'}" 
             @click="copyCode"
         >{{ copyIcon }}</span>
      </div>
      <pre><code v-html="highlightedCode"></code></pre>
    </div>
  </div>
</template>

<script setup>
import { defineProps, ref, computed } from 'vue';
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
      Code: ""
    }),
    required: true,
  },
});

const copyIcon = ref('content_copy');

const copyCode = () => {
  navigator.clipboard.writeText(props.codeInfo.Code)
    .then(() => {
      copyIcon.value = 'done';
      setTimeout(() => copyIcon.value = 'content_copy', 2000); // Use the correct delay here
    })
    .catch(err => {
      // Error handling
    });
};

//Custom words
Prism.languages.python = Prism.languages.extend('python', {
  'decorator': {
    pattern: /\bprint\b(?=\()/,
    lookbehind: true,
    alias: 'keyword'
  },
  'comment': {
    pattern: /file/,
    lookbehind: true,
    alias: 'keyword' 
  }
});

const highlightedCode = computed(() => {
  const language = props.codeInfo.Language.toLowerCase();
  const prismLanguage = Prism.languages[language] || Prism.languages.plain;

  return Prism.highlight(props.codeInfo.Code, prismLanguage, language);
});


</script>

<style scoped>
.code-block {
  margin: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
  background-color: #282C34; /* Changed to black */
  color: white; /* Ensures text is white */
  width: 500px;
}

.language-name {
  color: #D5D5D5;
  font-size: 10px;
}

.copy-icon {
  /* color: #868686; */
  color: #CDB100;
  cursor: pointer;
  font-size: 22px;
}

.copy-icon:hover {
  color: #AF9800;
}

.icon-done {
  color: #00FF4D;
}

.icon-done:hover {
  color: #00FF4D; /* Keeps the icon green when hovered over in 'done' state */
}

.copy-bar {
  display: flex;
  justify-content: space-between; /* Adjusted for space-between to align items properly */
  background-color: gray;
  padding: 5px;
}

.language-name {
  flex-grow: 1; /* Ensures language name aligns to the left */
  font-size: 20px;
  margin-left: 6px;
}

code {
  background-color: #282C34; /* Background set to black */
  /* padding: 5px; */
  border-radius: 3px;
  font-size: 13.5px;
  margin-left: 16px;
  line-height: 20px;
}
</style>
