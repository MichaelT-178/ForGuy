<template>
  <div>
    <h1 class="header">My Visual Studio Code Settings</h1>
    <p class="description">This is my settings file for VSCode. Contains mostly keyword coloring. Read comments for details.</p>
    <div class="bar">
      <span class="settings-header">Settings.json</span>
      <button @click="downloadJson" ref="downloadButton">Download JSON</button>
      <button @click="copyJson" ref="copyButton">Copy JSON</button>
    </div>
    <div class="json-container">
      <pre v-html="highlightedJson"></pre>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import Prism from 'prismjs';
import 'prismjs/components/prism-json';
import 'prismjs/themes/prism-coy.css';
import './custom.css';
import { settings } from '../../../data/CompSci/settings.vue';
//import 'prismjs/themes/prism-solarizedlight.css';

const copyButton = ref(null);
const downloadButton = ref(null);

const copyJson = () => {
  navigator.clipboard.writeText(settings)
      .then(() => {
          copyButton.value.innerText = 'Copied!';
          setTimeout(() => copyButton.value.innerText = "Copy JSON", 2000); 
      })
      .catch(err => {
          console.error('Failed to copy JSON: ', err);
      });
};

const downloadJson = () => {
  const blob = new Blob([settings], { type: 'application/json' });
  const link = document.createElement('a');

  link.href = URL.createObjectURL(blob);
  link.download = 'settings.json';

  document.body.appendChild(link);
  link.click();

  document.body.removeChild(link);
  URL.revokeObjectURL(link.href);
    
  downloadButton.value.innerText = 'Downloaded!';

  setTimeout(() => {
    downloadButton.value.innerText = "Download JSON";
  }, 2000); 
}

const highlightedJson = computed(() => {
  return Prism.highlight(settings, Prism.languages.json, 'json');
});

</script>


<style scoped>

.header, .description {
  margin: 0 auto; 
  max-width: 70%; 
  box-sizing: border-box;
}

.header {
  margin-top: 15px;
  padding-left: 1px; 
}

.description {
  font-size: 18.5px;
  padding-left: 2px; 
  margin-top: 6.3px;
}

.bar {
  background-color: gray;
  padding: 10px;
  display: flex;
  justify-content: flex-end; 
  gap: 10px;
  margin: 20px auto 0 auto; 
  max-width: 70%; 
  box-sizing: border-box; 
}
  
.settings-header {
  flex-grow: 1;
  font-size: 34px;
  color: #D5D5D5;
  margin-left: 10px;
  font-weight: 525;
}


.json-container {
  margin: 0 auto; 
  max-width: 70%; 
  box-sizing: border-box; 
}

button {
  background-color: #CDB100;
  color: white;
  padding: 8px 18px;
  font-size: 14.5px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #AF9800;
}

pre {
  background-color: #282C34;
  padding: 10px;
  margin-top: 0; 
  box-sizing: border-box; 
  border: 1.25px solid #000000;
}

</style>
