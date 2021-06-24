<template>
  <div>
    <v-btn @click="dialog = true" color="pink" fab dark small absolute top left>
      <v-icon>mdi-plus</v-icon>
    </v-btn>
    <v-row>
      <v-col cols="4" :key="i" v-for="i in 6">
        <v-card height="230px"
          ><v-img
            lazy-src="https://picsum.photos/id/11/10/6"
            height="230"
            src="https://picsum.photos/id/11/500/300"
          >
          </v-img
        ></v-card>
      </v-col>
    </v-row>
    <v-dialog
      v-model="dialog"
      fullscreen
      hide-overlay
      transition="dialog-bottom-transition"
    >
      <v-card class="pa-6">
        <tip-tap-component
          :EditorContent="content"
          @changeContent="setContent"
        />
        <v-container>
          <v-row justify="end">
            <v-btn text @click="dialog = false">Cancel</v-btn>
            <v-btn text color="primary" @click="dialog = false">
              Submit
            </v-btn>
          </v-row>
        </v-container>
      </v-card>
    </v-dialog>
  </div>
</template>
<script>
import TipTapComponent from "../partial/TipTapComponent.vue";
export default {
  components: { TipTapComponent },
  data() {
    return { dialog: false, content: "" };
  },
  methods: {
    setContent(content) {
      this.content = content;
    }
  }
};
</script>
