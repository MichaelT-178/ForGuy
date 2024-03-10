<template>
    <table>
      <thead>
        <tr>
          <th>Shortcut</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in shortcuts" :key="item.id">
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
  
  <style>
  /* Add your styles here */
  table {
    width: 100%;
    border-collapse: collapse;
  }
  
  th, td {
    border: 1px solid #ddd;
    padding: 8px;
  }
  
  th {
    background-color: #f4f4f4;
  }
  </style>
  