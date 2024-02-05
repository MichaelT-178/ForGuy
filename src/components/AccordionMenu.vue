<template>
  <div class="accordion-menu">
    <div class="accordion-title" @click="toggleAccordion">
        <h2>{{ item.DisplayTitle }}</h2>
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
  const excludedKeys = ['DisplayTitle'];
  return !excludedKeys.includes(key);
}

const hyperlinkText = (text) => {
  const urlPattern = /(\b(https?|ftp|file):\/\/[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|])/ig;
  return text.replace(urlPattern, (url) => 
    {
      return `<a href="${url}" target="_blank" 
                style="color: #007AFF;" 
                onmouseover="this.style.color='blue'" 
                onmouseout="this.style.color='#007AFF'"
              >
              ${url}</a>`;
    }
  );
}

const filteredEntries = computed(() => {
  return Object.entries(item.value)
          .filter(([key, value]) => value && shouldDisplay(key))
          .map(([key, value]) => {
            if (typeof value === 'string' && (value.includes('http://') || value.includes('https://'))) {
              return [key, hyperlinkText(value)];
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




  