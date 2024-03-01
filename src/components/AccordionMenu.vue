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
          <b style="margin-right: 3px;"><u>{{ entry[0] }}</u>{{ typeof entry[1] === 'string' ? ':' : ""}}</b>
          <span v-if="typeof entry[1] === 'string'" v-html="entry[1]"></span>
          <ul class="menu-attribute" v-else>
            <li v-for="(item, idx) in entry[1]" :key="`item-${idx}`" v-html="formatEntry(item)" class="menu-items"></li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</template>


<script setup>
import { ref, computed, watchEffect, toRefs } from 'vue';
import router from '../router/index.js';

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
};

const shouldDisplay = (key) => {
  const excludedKeys = ['Name'];
  return !excludedKeys.includes(key);
};

//Ex: https://www.target.com/
const highlightLinkText = (text) => {
  const urlPattern = /(\b(https?|ftp|file):\/\/|www\.)[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|]/ig;

  return text.replace(urlPattern, (url) => 
    {
      const realURL = !url.startsWith("http") ? `https://${url}` : url;

      return `<a href="${realURL}" target="_blank" 
                style="color: #007AFF; text-decoration: none;" 
                onmouseover="this.style.color='blue'; this.style.textDecoration='underline';" 
                onmouseout="this.style.color='#007AFF'; this.style.textDecoration='none';"
              >${url}</a>`;
    }
  );
};

//[The link](https://www.target.com/)
const createHyperLink = (text) => {
  const markdownLinkPattern = /\[([^\]]+)\]\((https?:\/\/[^\s]+)\)/g;
  return text.replace(markdownLinkPattern, (match, label, url) => 
    `<a href="${url}" target="_blank"
        style="color: #007AFF; text-decoration: none;" 
        onmouseover="this.style.color='blue'; this.style.textDecoration='underline';" 
        onmouseout="this.style.color='#007AFF'; this.style.textDecoration='none';"
      >
      ${label}</a>`
  );
};

//(Router link)[/linkedin/LinkedinTips]. Note the seemingly unused "match" parameter is necessary.
const createRouterLink = (text) => {
  const customLinkPattern = /\(([^\)]+)\)\[([^\s]+)\]/g;
  return text.replace(customLinkPattern, (match, label, path) => {
    return `<a href="javascript:void(0);" onclick="navigateToPath('${path}')"
               style="color: #007AFF; text-decoration: none;" 
               onmouseover="this.style.color='blue'; this.style.textDecoration='underline';" 
               onmouseout="this.style.color='#007AFF'; this.style.textDecoration='none';"
            >${label}</a>`;
  });
};

window.navigateToPath = (path) => {
  router.push(path);
};

//@Image View@[{ 'name': 'ImageView', 'params': { 'Name': 'NSA Pic', 'Description': 'This is the NSA pic', 'Pic': 'seahawk.png'} }]
const createRouterLinkWithProps = (text) => {
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
    return `<a href="javascript:void(0);" onclick="navigateToVuePath('${JSON.stringify(toProp).replace(/"/g, "&quot;")}')"
               style="color: #007AFF; text-decoration: none;" 
               onmouseover="this.style.color='blue'; this.style.textDecoration='underline';" 
               onmouseout="this.style.color='#007AFF'; this.style.textDecoration='none';"
            >
            ${label}</a>`;
  });
};

window.navigateToVuePath = (toPropString) => {
  const toProp = JSON.parse(toPropString.replace(/&quot;/g, "\""));
  router.push(toProp);
};

const formatEntry = (value) => {

  if (typeof value === 'string') {

    if ((value.includes('(http://') || value.includes('(https://'))) {
      return createHyperLink(value);
    }

    value = highlightLinkText(value);
    value = createRouterLink(value);
    value = createRouterLinkWithProps(value);
  
  }

  return value;

};

const filteredEntries = computed(() => {
  return Object.entries(item.value)
    .filter(([key, value]) => value && shouldDisplay(key))
    .map(([key, value]) => {

      if (Array.isArray(value)) {
        value = value.map(formatEntry);
      } else {
        value = formatEntry(value);
      }

      return [key, value];

    });
});

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

.menu-attribute {
  margin-top: 10px; /* Changes vertical spacing of menu */
}

.menu-items {
  list-style-type: disc;
  margin-left: 23px;
  margin-top: -4px;
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
