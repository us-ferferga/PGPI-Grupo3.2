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

<script>
import { ref } from 'vue'

const columns = [
  {
    name: 'dia',
    required: true,
    label: 'Día',
    align: 'left',
    field: row => row.name,
    format: val => `${val}`,
    sortable: true
  },
  { name: 'hora', align: 'center', label: 'Hora', field: 'hora', sortable: true }
]

const rows = [
  {
    name: 'Lunes',
    hora: '10:30'
  },
  {
    name: 'Martes',
    hora: '10:30'
  },
  {
    name: 'Miércoles',
    hora: '18:30'
  },
  {
    name: 'Jueves',
    hora: '10:30'
  },
  {
    name: 'Viernes',
    hora: '10:30'
  },

]

export default {
  setup () {
    const selected = ref([])

    return {
      selected,
      columns,
      rows,

      getSelectedString () {
        return selected.value.length === 0 ? '' : `${selected.value.length} record${selected.value.length > 1 ? 's' : ''} selected of ${rows.length}`
      }
    }
  }
}
</script>
