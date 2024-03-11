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
})
</script>

<style scoped>
/* Base table styles */
table {
  width: 70%;
  border-collapse: separate; /* Use separate to handle individual border settings */
  border-spacing: 0; /* Eliminate spacing between cells */
  border: 1px solid black; /* Add a black border around the table */
}

th, td {
  border-top: 1px solid #ddd; /* Keep top border */
  border-bottom: 1px solid #ddd; /* Keep bottom border */
  padding: 8px;
  border-left: none; /* Remove left border */
  border-right: none; /* Remove right border */
  text-align: left; /* Ensure text is aligned to the left */
}

th {
  background-color: #000080; /* Apply a dark blue background for headers */
  color: #ffffff; /* Use white text for contrast */
  border-top: none; /* Remove top border for a cleaner header look */
}

/* Alternating row colors utilizing Vue dynamic class assignment */
.row-odd {
  background-color: #ffffff; /* Assign white background to odd rows */
}

.row-even {
  background-color: #f2f2f2; /* Assign light grey background to even rows */
}
</style>
