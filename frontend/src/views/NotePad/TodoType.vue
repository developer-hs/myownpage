<template>
  <div>
    <v-system-bar absolute window color="#ced6e0">
      <v-row class="pa-2  ">
        <v-col cols="auto">
          <div class="d-inline-flex">
            <v-icon color="red" small>mdi-book-open-outline</v-icon>
            <span
              class="text-body-1 red--text"
              :key="`tasks-${notePad.length}`"
            >
              {{ memoCount }}
            </span>
          </div>
        </v-col>
        <v-col cols="auto">
          <div class="d-inline-flex">
            <v-icon color="success" small>mdi-checkbox-marked-outline</v-icon>
            <span class="text-body-1 success--text">{{ DoneCount }} </span>
          </div>
        </v-col>
      </v-row>
      <v-spacer></v-spacer>
      <v-progress-circular
        size="24"
        :value="progress"
        class="mr-2"
      ></v-progress-circular>
    </v-system-bar>
    <v-row align="center" justify="center">
      <v-col cols="12">
        <v-text-field
          class="pt-12"
          dense
          v-model="memoText"
          label="할 일을 등록해 주세요"
          @keypress.enter="createMemo"
        >
        </v-text-field>
      </v-col>
    </v-row>
    <v-col v-if="notePad.length > 0">
      <v-card flat height="400">
        <v-scroll-y-reverse-transition hide-on-leave group>
          <template v-for="(note, index) in notePad">
            <v-divider v-if="index !== 0" :key="`${index}-divider`"></v-divider>

            <v-list-item :key="`${index}-${note.memo}`">
              <v-list-item-action>
                <v-checkbox
                  @click="updateMemo({ updateNote: note, page })"
                  v-model="note.done"
                  color="info darken-3"
                >
                  <div
                    slot="label"
                    :class="(note.done && 'grey--text') || 'text--primary'"
                    class="text-subtitle-2 ml-2"
                    v-text="note.memo"
                  ></div>
                </v-checkbox>
              </v-list-item-action>

              <v-spacer></v-spacer>
              <v-col cols="auto">
                <v-scroll-x-transition>
                  <div v-if="!note.done">
                    <v-btn
                      @click="removeMemo(note.id)"
                      x-small
                      icon
                      fab
                      depressed
                      ><v-icon color="red">mdi-delete-empty</v-icon></v-btn
                    >
                    <v-btn
                      icon
                      x-small
                      fab
                      depressed
                      @click="
                        dialog = !dialog;
                        updateNote = note;
                      "
                      ><v-icon color="">mdi-pencil-plus</v-icon>
                    </v-btn>
                  </div>
                  <v-icon v-if="note.done" color="success">
                    mdi-check
                  </v-icon>
                </v-scroll-x-transition>
              </v-col>
            </v-list-item>
          </template>
        </v-scroll-y-reverse-transition>
      </v-card>

      <div class="text-center">
        <v-pagination v-model="page" :length="pageSize" circle></v-pagination>
      </div>
    </v-col>

    <v-container v-else>
      <v-col cols="12" class="text-center grey--text text-body-1">
        Todo is Empty !!
      </v-col>
    </v-container>

    <!-- update -->
    <v-dialog v-model="dialog" max-width="70rem">
      <v-card class="pa-6">
        <v-card-text>
          <span>메모수정</span>
          <v-textarea auto-grow counter v-model="updateNote.memo"></v-textarea>
        </v-card-text>
        <v-row justify="end">
          <v-btn
            text
            color="primary"
            @click="
              dialog = false;
              UpdateMemo();
            "
          >
            Submit
          </v-btn>
        </v-row>
      </v-card>
    </v-dialog>
  </div>
</template>
<script>
import { mapActions } from "vuex";

export default {
  data() {
    return {
      tasks: [
        {
          done: false,
          text: "Foobar"
        },
        {
          done: false,
          text: "Fizzbuzz"
        }
      ],
      page: 1,
      task: null,
      group: true,
      memoText: "",
      updateNote: {},
      dialog: false
    };
  },
  computed: {
    memoCount() {
      return this.$store.state.notepads.totalMemoCount;
    },
    notePad() {
      return this.$store.state.notepads.notepad;
    },
    pageSize() {
      return this.$store.state.notepads.pageSize;
    },
    DoneCount() {
      return this.$store.state.notepads.doneCount;
    },
    progress() {
      return (this.DoneCount / this.memoCount) * 100;
    },
    remainingTasks() {
      return this.memoCount - this.DoneCount;
    }
  },
  watch: {
    page(val) {
      this.$store.dispatch("notepads/getNotepad", val);
    }
  },
  methods: {
    ...mapActions("notepads", ["removeMemo", "updateMemo"]),
    getNotePad(page = 1) {
      this.$store.dispatch("notepads/getNotepad", page);
    },
    createMemo() {
      this.$store.dispatch("notepads/createMemo", { memo: this.memoText });
      this.memoText = "";
    },
    UpdateMemo() {
      this.$store.dispatch("notepads/updateMemo", {
        updateNote: this.updateNote,
        page: this.page
      });
    },
    changeDateFormat(date) {
      const Year = date.slice(2, 4);
      const Month = date.slice(5, 7);
      const Day = date.slice(8, 10);
      const Hours = date.slice(11, 13);
      const Minuit = date.slice(14, 16);
      const Second = date.slice(17, 19);
      return `${Year}/ ${Month}/${Day} ${Hours}:${Minuit}:${Second}`;
    }
  }
};
</script>
