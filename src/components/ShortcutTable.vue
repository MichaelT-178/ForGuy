<template>
  <table>
    <thead>
      <tr>
        <th>Shortcut</th>
        <th>Description</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(item, index) in shortcuts" 
          :key="item.id" :class="{'row-odd': index % 2 === 0, 'row-even': index % 2 !== 0}">
        <td>{{ item.Shortcut }}</td>
        <td>{{ item.Action }}</td>
      </tr>
    </tbody>
  </table>
</template>


<script setup>
const props = defineProps({
  shortcuts: {
    type: Array,
    default: () => []
  }
});

</script>


<style scoped>

table {
  width: 70%;
  border-collapse: separate; 
  border-spacing: 0;
  border: 1px solid black;
}

th, td {
  border-top: 1px solid #ddd;
  border-bottom: 1px solid #ddd;
  padding: 8px;
  border-left: none;
  border-right: none;
  text-align: left;
}

th {
  background-color: #000080;
  color: #ffffff;
  border-top: none;
}

.row-odd {
  background-color: #ffffff;
}

.row-even {
  background-color: #f2f2f2;
}

tbody tr:first-of-type td {
  border-top: none;
}

</style>

