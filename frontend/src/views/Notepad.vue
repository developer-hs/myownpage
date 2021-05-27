<template>
  <v-col sm="10" offset-sm="4">
    <v-card class="mx-auto mt-12" max-width="600">
      <v-system-bar></v-system-bar>

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
              class="text-uppercase font-weight-regular caption"
              v-text="item.datetime_created"
            ></span>

            <div v-text="item.memo" />
            <div class="d-flex justify-end">
              <v-btn
                @click="removeMemo(index)"
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
          v-model="memo"
          @keyup.enter="onMemoHandler"
        ></v-text-field>
      </div>
    </v-card>
  </v-col>
</template>
<script>
import { mapState } from "vuex";
export default {
  data() {
    return {
      memo: "",
      item: [{ header: "Memo" }],
    };
  },
  computed: {
    ...mapState({
      notepad: (state) => state.notepads.notepad,
    }),
  },
  methods: {
    onMemoHandler() {
      this.items.push({
        memo: this.memo,
        datetime_created: new Date(),
      });
    },
    removeMemo(index) {
      console.log(index);
      this.items.splice(index, 1);
    },
  },
  beforeMount() {
    this.items = this.notepad;
  },
};
</script>
