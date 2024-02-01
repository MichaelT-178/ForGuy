<template>
  <div>
    <div class="bar">
      <button @click="downloadJson" ref="downloadButton">Download JSON</button>
      <button @click="copyJson" ref="copyButton">Copy JSON</button>
    </div>
    <div class="json-container">
      <pre>{{ settings }}</pre>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { settings } from '../data/settings.vue';

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
  setTimeout(() => downloadButton.value.innerText = "Download JSON", 2000); 
}

</script>


<style>

.bar {
  background-color: gray;
  padding: 10px;
  display: flex;
  justify-content: flex-end; 
  gap: 10px;
  margin: 20px auto 0 auto; 
  max-width: 80%; 
  box-sizing: border-box; 
}
  
.json-container {
  margin: 0 auto; 
  max-width: 80%; 
  box-sizing: border-box; 
}

button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}

pre {
  background-color: #f4f4f4;
  padding: 10px;
  border-radius: 5px;
  margin-top: 0; 
  box-sizing: border-box; 
}

</style>
  
