<template>
  <div class="table-container">
    <h2>{{ tableName }}</h2>
    <table>
      <thead>
        <tr>
          <th v-if="hasCommandProperty">Command</th>
          <th v-if="hasPropertyProperty">Property</th>
          <th>Description</th>
          <th>Example</th>
          <th>Copy</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in filteredItems" :key="index">
          <td v-if="hasCommandProperty">{{ item.Command }}</td>
          <td v-if="hasPropertyProperty">{{ item.Property}}</td>
          <td id="description-column">{{ item.Description }}</td>
          <td>{{ item.Example }}</td>
          <td>
            <button 
              :class="{'copied': item.copied}" 
              @click="copyToClipboard(item, index)">
              {{ item.copied ? 'Copied' : 'Copy' }}
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>


<script setup>
import { computed } from 'vue';

const props = defineProps({
  tableName: String,
  items: Array
});

props.items.forEach(item => {
  item.copied = false;
});

// If the object contains the table name do
// NOT include it in the table
const filteredItems = computed(() => {
  if (props.items[0]?.tableName) {
    return props.items.slice(1);
  }
  
  return props.items;
});

const hasCommandProperty = computed(() => filteredItems.value.some(item => 'Command' in item));
const hasPropertyProperty = computed(() => filteredItems.value.some(item => 'Property' in item));

const copyToClipboard = (item, index) => {
  navigator.clipboard.writeText(item.Example)
    .then(() => {
      props.items[index].copied = true; 
      
      setTimeout(() => {
        props.items[index].copied = false; 
      }, 900); 

    })
    .catch((err) => {
      console.error('Failed to copy: ', err);
    });
};

</script>


<style scoped>

.table-container {
  width: 80%;
  overflow: hidden; 
}

h2 {
  margin-bottom: 12px;
  margin-left: 2px;
}

table {
  width: 100%;
  border-collapse: collapse;
  border: 1px solid black; 
  border-radius: 8px;
}

th, td {
  padding: 8px;
  text-align: left;
  border-bottom: 1px solid black; 
  font-size: 16px;
}

th {
  font-size: 17px;
}

thead tr {
  background-color: white;
}

tbody td {
  background-color: #FFF6E8;
}

th, td {
  border-left: none;
  border-right: none;
}

thead tr:first-child th {
  border-top: none;
}

button {
  background-color: #007AFF;
  color: white;
  cursor: pointer;
  border: none;
  padding: 5px 10px;
  width: 65px;
  text-align: center;
  display: inline-block;
  font-size: 14px;
}

button:hover {
  background-color: #0000D7;
}

button.copied {
  background-color: #26B952;
  color: white;
}

#description-column { 
  max-width: 215px; 
  word-wrap: break-word; 
}

</style>


