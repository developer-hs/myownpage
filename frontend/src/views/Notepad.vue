<template>
  <v-col sm="10" offset="1">
    <v-card class="mx-auto mt-12 rounded-0" max-width="600">
      <v-system-bar color="grey lighten-1"></v-system-bar>

      <v-toolbar flat color="transparent">
        <v-text-field
          append-icon="mdi-magnify"
          label="Search News"
          single-line
        ></v-text-field>
      </v-toolbar>

      <v-list three-line>
        <v-list-item
          v-for="(note, index) in notepad"
          :key="index"
          ripple
          @click="() => {}"
        >
          <v-list-item-content>
            <small
              class="text-uppercase font-weight-light caption"
              v-text="changeDateFormat(note.datetime_created)"
            >
            </small>

            <div class="pt-2" v-text="note.memo" />

            <div class="d-flex justify-end">
              <v-btn
                @click="removeMemo(notepad[index].id)"
                class="mr-3"
                x-small
                icon
                fab
                depressed
                ><v-icon color="red">mdi-delete-empty</v-icon></v-btn
              >
              <v-btn
                class="mr-3"
                icon
                x-small
                fab
                depressed
                @click="
                  dialog = !dialog;
                  updateMemoText = note.memo;
                  updateNote = note;
                "
                ><v-icon color="">mdi-pencil-plus</v-icon>
              </v-btn>
            </div>
          </v-list-item-content>
        </v-list-item>
        <!-- update -->
        <v-dialog v-model="dialog" max-width="70rem">
          <v-card class="pa-6">
            <v-card-text>
              <span>메모수정</span>
              <v-textarea
                auto-grow
                counter
                v-model="updateMemoText"
              ></v-textarea>
            </v-card-text>
          </v-card>
          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn
              text
              color="primary"
              @click="
                dialog = false;
                onUpdateHandler();
              "
            >
              Submit
            </v-btn>
          </v-card-actions>
        </v-dialog>
      </v-list>
      <div class="pr-3 pl-3">
        <v-text-field
          label="Memo input"
          v-model="memoText"
          @keypress.enter="onMemoHandler"
        >
        </v-text-field>
      </div>
    </v-card>
  </v-col>
</template>
<script>
import { mapActions } from "vuex";
export default {
  data() {
    return {
      memoText: "",
      updateMemoText: "",
      updateNote: {},
      notepad: this.$store.state.notepads.notepad,
      dialog: false,
    };
  },
  computed: {},
  methods: {
    ...mapActions("notepads", ["removeMemo"]),
    onMemoHandler() {
      this.$store.dispatch("notepads/createMemo", { memo: this.memoText });
      this.memoText = "";
    },
    onUpdateHandler() {
      this.updateNote.memo = this.updateMemoText;
      this.$store.dispatch("notepads/updateMemo", this.updateNote);
    },
    changeDateFormat(date) {
      const Year = date.slice(2, 4);
      const Month = date.slice(5, 7);
      const Day = date.slice(8, 10);
      const Hours = date.slice(11, 13);
      const Minuit = date.slice(14, 16);
      const Second = date.slice(17, 19);
      return `${Year}/ ${Month}/${Day} ${Hours}:${Minuit}:${Second}`;
    },
  },
};
</script>
