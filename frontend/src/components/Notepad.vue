<template>
  <v-container id="notepad_container" class="mt-1">
    <v-row justify="end">
      <v-col cols="4">
        <v-select
          class="text-body-2"
          v-model="type"
          :items="types"
          label="Type"
          dense
          light
        ></v-select>
      </v-col>
    </v-row>
    <v-card rounded="lg" elevation="1" height="600" class="pa-3">
      <todo-type v-if="type == 'Todo'" />
      <memo-type v-if="type == 'Memo'" />
    </v-card>
  </v-container>
</template>
<script>
import MemoType from "../views/NotePad/MemoType.vue";
import TodoType from "../views/NotePad/TodoType.vue";
export default {
  data() {
    return {
      type: localStorage.getItem("NOTEPAD_TYPE"),
      types: ["Todo", "Memo"]
    };
  },
  components: {
    TodoType,
    MemoType
  },
  watch: {
    type(val) {
      console.log(val);
      localStorage.setItem("NOTEPAD_TYPE", val);
    }
  },
  created() {
    const type = localStorage.getItem("NOTEPAD_TYPE");
    if (type === null) {
      localStorage.setItem("NOTEPAD_TYPE", "Todo");
    }
  }
};
</script>
