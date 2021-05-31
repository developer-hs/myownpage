<template>
  <v-col sm="10" offset-sm="5">
    <v-card class="mx-auto mt-12" max-width="600">
      <v-system-bar color="grey lighten-1"></v-system-bar>

      <v-toolbar flat color="transparent">
        <v-btn icon>
          <v-icon>mdi-arrow-left</v-icon>
        </v-btn>

        <v-text-field
          append-icon="mdi-magnify"
          label="Search News"
          single-line
        ></v-text-field>
      </v-toolbar>

      <v-list three-line>
        <v-list-item
          v-for="(item, index) in notepad"
          :key="index"
          ripple
          @click="() => {}"
        >
          <v-list-item-content>
            <span
              class="text-uppercase font-weight-light caption"
              v-text="item.datetime_created"
            ></span>

            <div class="pt-2" v-text="item.memo" />
            <div class="d-flex justify-end">
              <v-btn
                @click="removeMemo(notepad[index].id)"
                class="mr-3"
                x-small
                fab
                depressed
                color="white"
                ><v-icon color="red">mdi-delete-empty</v-icon></v-btn
              >
              <v-btn class="mr-3" x-small fab depressed color="white"
                ><v-icon color="">mdi-pencil-plus</v-icon></v-btn
              >
            </div>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <div class="pr-3 pl-3">
        <v-text-field
          label="Memo input"
          v-model="memo"
          @keypress.enter="onMemoHandler"
        ></v-text-field>
      </div>
    </v-card>
  </v-col>
</template>
<script>
import { mapActions } from "vuex";
export default {
  data() {
    return {
      memo: "",
      notepad: this.$store.state.notepads.notepad,
    };
  },
  computed: {},
  methods: {
    ...mapActions("notepads", ["removeMemo"]),
    onMemoHandler() {
      this.$store.dispatch("notepads/createMemo", { memo: this.memo });
      this.memo = "";
    },
  },
};
</script>
