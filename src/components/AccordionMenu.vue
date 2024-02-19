<template>
  <div class="accordion-menu">
    <div class="accordion-title" @click="toggleAccordion">
        <h2>{{ item.Name }}</h2>
        <span v-if="!isOpen"><span class="material-icons" id="open">add_circle</span></span>
        <span v-else><span class="material-icons" id="close">cancel</span></span>
    </div>
    <div class="accordion-content" v-if="isOpen">
      <ul>
        <li v-for="(entry, index) in filteredEntries" :key="index">
          <b> <u>{{ entry[0] }}</u>:</b> <span v-html="entry[1]"></span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watchEffect, toRefs } from 'vue';
import router from '../router/index.js'

const props = defineProps({
  item: Object,
  isOpen: Boolean
});

const { item, isOpen: isOpenProp } = toRefs(props);
const isOpen = ref(isOpenProp.value);

watchEffect(() => {
  isOpen.value = isOpenProp.value;
});

const toggleAccordion = () => {
  isOpen.value = !isOpen.value;
}

const shouldDisplay = (key) => {
  const excludedKeys = ['Name'];
  return !excludedKeys.includes(key);
}

const hyperlinkText = (text) => {
  const urlPattern = /(\b(https?|ftp|file):\/\/[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|])/ig;
  return text.replace(urlPattern, (url) => 
    {
      return `<a href="${url}" target="_blank" 
                style="color: #007AFF; text-decoration: none;" 
                onmouseover="this.style.color='blue'; this.style.textDecoration='underline';" 
                onmouseout="this.style.color='#007AFF'; this.style.textDecoration='none';"
              >
              ${url}</a>`;
    }
  );
}

//[The link](https://www.target.com/)
const markdownLinkToHyperlink = (text) => {
  const markdownLinkPattern = /\[([^\]]+)\]\((https?:\/\/[^\s]+)\)/g;
  return text.replace(markdownLinkPattern, (match, label, url) => 
      `<a href="${url}" target="_blank">${label}</a>`
  );
}


//(Router link)[/linkedin/LinkedinTips]
const customLinkToVueRouterLink = (text) => {
  const customLinkPattern = /\(([^\)]+)\)\[([^\s]+)\]/g;
  return text.replace(customLinkPattern, (match, label, path) => {
    // Instead of converting to <router-link>, return a standard <a> tag
    // with an onclick event that uses Vue Router to navigate
    return `<a href="javascript:void(0);" onclick="navigateToPath('${path}')">${label}</a>`;
  });
}

// You'll need to define the navigateToPath function in your component or globally
// If globally, make sure to attach it to window or a similar global scope accessible from the template
window.navigateToPath = (path) => {
  // Assuming you have access to your Vue Router instance here, use it to programmatically navigate
  // For example, if your router instance is available globally or injected into the window object
  router.push(path);
}


//
//@Image View@[{ 'name': 'ImageView', 'params': { 'Name': 'NSA Pic', 'Description': 'This is the NSA pic', 'Pic': 'seahawk.png'} }]
const markdownToJsonRouterLink = (text) => {
  const markdownPattern = /@([^@]+)@\[\s*({.*?})\s*\]/g;

  return text.replace(markdownPattern, (match, label, jsonString) => {
    let toProp;

    try {
      jsonString = jsonString.replace(/'/g, '"');
      toProp = JSON.parse(jsonString);
    } catch (e) {
      console.error('Error parsing JSON string:', e);
      return match; 
    }

    return `<a href="javascript:void(0);" onclick="navigateToVuePath('${JSON.stringify(toProp).replace(/"/g, "&quot;")}')">${label}</a>`;
  });
}

window.navigateToVuePath = (toPropString) => {
  const toProp = JSON.parse(toPropString.replace(/&quot;/g, "\""));
  router.push(toProp);
}

const filteredEntries = computed(() => {
  return Object.entries(item.value)
          .filter(([key, value]) => value && shouldDisplay(key))
          .map(([key, value]) => {
            if (typeof value === 'string') {
              // Process the string for HTTP links first
              if (value.includes(' http://') || value.includes(' https://')) {
                value = hyperlinkText(value);
              }
              // Convert markdown links to hyperlinks
              value = markdownLinkToHyperlink(value);
              // Convert custom links to Vue router-link components
              value = customLinkToVueRouterLink(value);
              // Convert custom markdown to JSON for router links into Vue router-link components
              value = markdownToJsonRouterLink(value);
            }
            return [key, value];
          });
});


// const formatKey = (key) => {
//   return key.replace(/([A-Z])/g, ' $1').trim().replace(/^./, str => str.toUpperCase());
// }

</script>

<style scoped>
.accordion-menu {
  border: 1px solid #ccc;
  border-radius: 5px;
  margin: 10px auto;
  padding: 10px; 
  background-color: #f0f0f0;
  width: 80%; 
  max-width: none; 
}

.accordion-title h2 {
  cursor: pointer;
  margin: 0;
  display: inline-block;
  font-size: 22px; 
}

.accordion-title span {
  vertical-align: middle;
  float: right;
  font-weight: bold;
}

.accordion-content {
  margin-top: 20px;
}

.accordion-content ul {
  padding: 0;
  list-style-type: none;
}

.accordion-content li {
  margin-bottom: 13px;
}

#open, #close {
  vertical-align: middle;
  color: teal;
  font-size: 28px;
}

</style>




  