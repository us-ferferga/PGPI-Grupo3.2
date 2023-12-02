<template>
  <div class="q-pa-md">
    <q-table
      flat bordered
      :rows="rows"
      :columns="columns"
      row-key="name"
      :selected-rows-label="getSelectedString"
      selection="multiple"
      v-model:selected="selected"
    />

    <div class="q-mt-md">
      Selected: {{ JSON.stringify(selected) }}
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const selected = ref([])

const columns = [
  
  { name: 'dia', align: 'center', label: 'Día', field: 'dia', sortable: true }
  ,
  { name: 'hora', align: 'center', label: 'Hora', field: 'hora', sortable: true }
]

const rows = [
  {
    dia: 'Lunes',
    hora: '10:30'
  },
  {
    dia: 'Martes',
    hora: '10:30'
  },
  {
    dia: 'Martes',
    hora: '18:30'
  },
  {
    dia: 'Jueves',
    hora: '10:30'
  },
  {
    dia: 'Viernes',
    hora: '10:30'
  },

]

function getSelectedString () {
        return selected.value.length === 0 ? '' : `${selected.value.length} record${selected.value.length > 1 ? 's' : ''} selected of ${rows.length}`
  
}
</script>
