<template>
  <v-card height="600" class="pt-3 mt-16 rounded-0 pa-3" max-width="600">
    <v-row align="center" justify="center">
      <v-row class="pt-3 pl-5">
        <v-col cols="auto">
          <v-icon color="red" small>mdi-book-open-outline</v-icon>
          <span class="text-body-2 red--text" :key="`tasks-${notepad.length}`">
            {{ remainingTasks }}
          </span>
        </v-col>
        <v-col cols="auto">
          <v-icon color="success" small>mdi-checkbox-marked-outline</v-icon>
          <span class="text-body-2 success--text">{{ completedTasks }} </span>
        </v-col>
        <v-col cols="auto">
          <v-progress-circular
            size="24"
            :value="progress"
            class="mr-2"
          ></v-progress-circular>
        </v-col>
      </v-row>
      <v-col cols="12">
        <v-text-field
          dense
          v-model="memoText"
          label="할 일을 등록해 주세요"
          solo
          @keypress.enter="createMemo"
        >
        </v-text-field>
      </v-col>
    </v-row>
    <v-col v-if="notepad.length > 0" class="justify-space-between">
      <v-card flat height="400">
        <v-scroll-y-reverse-transition hide-on-leave group>
          <template v-for="(note, index) in notepad">
            <v-divider v-if="index !== 0" :key="`${index}-divider`"></v-divider>

            <v-list-item :key="`${index}-${note.memo}`">
              <v-list-item-action>
                <v-checkbox
                  @click="updateMemo(note)"
                  v-model="note.done"
                  color="info darken-3"
                >
                  <div
                    slot="label"
                    :class="(note.done && 'grey--text') || 'text--primary'"
                    class="ml-3 text-subtitle-2"
                    v-text="note.memo"
                  ></div>
                </v-checkbox>
              </v-list-item-action>

              <v-spacer></v-spacer>

              <v-scroll-x-transition>
                <div v-if="!note.done">
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
                <v-icon v-if="note.done" color="success">
                  mdi-check
                </v-icon>
              </v-scroll-x-transition>
            </v-list-item>
          </template>
        </v-scroll-y-reverse-transition>
      </v-card>

      <div class="text-center">
        <v-pagination v-model="page" :length="4" circle></v-pagination>
      </div>
    </v-col>

    <v-container v-else>
      <v-col cols="12" class="text-center grey--text text-body-1">
        Memo is Empty !!
      </v-col>
    </v-container>

    <!-- update -->
    <v-dialog v-model="dialog" max-width="70rem">
      <v-card class="pa-6">
        <v-card-text>
          <span>메모수정</span>
          <v-textarea auto-grow counter v-model="updateMemoText"></v-textarea>
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
  </v-card>
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
      updateMemoText: "",

      updateNote: {},
      notepad: this.$store.state.notepads.notepad,
      dialog: false
    };
  },
  computed: {
    completedTasks() {
      return this.notepad.filter(note => note.done).length;
    },
    progress() {
      return (this.completedTasks / this.notepad.length) * 100;
    },
    remainingTasks() {
      return this.notepad.length - this.completedTasks;
    }
  },
  methods: {
    ...mapActions("notepads", ["removeMemo", "updateMemo"]),
    createMemo() {
      this.$store.dispatch("notepads/createMemo", { memo: this.memoText });
      this.memoText = "";
    },
    UpdateMemo() {
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
    }
  },
  created() {}
};
</script>
