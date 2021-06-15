<template>
  <v-card rounded="lg" elevation="1" height="600" class="pa-3" max-width="600">
    <v-btn @click="dialog = true" color="pink" fab dark small absolute top left>
      <v-icon>mdi-plus</v-icon>
    </v-btn>
    <v-row>
      <v-col cols="6" :key="i" v-for="i in 3">
        <v-card height="230px"
          ><v-img
            lazy-src="https://picsum.photos/id/11/10/6"
            height="230"
            max-width="248.25"
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
        <tiptap-vuetify
          v-model="content"
          :extensions="extensions"
          :toolbar-attributes="{ color: 'brown lighten-3' }"
          placeholder="Write something …"
          @keydown="onkeydown"
        />
        <v-row justify="end">
          <v-btn text color="primary" @click="dialog = false">
            Submit
          </v-btn>
        </v-row>
      </v-card>
    </v-dialog>
  </v-card>
</template>
<script>
import {
  TiptapVuetify,
  Heading,
  Bold,
  Italic,
  Strike,
  Underline,
  Code,
  Paragraph,
  BulletList,
  OrderedList,
  ListItem,
  Link,
  Blockquote,
  HardBreak,
  HorizontalRule,
  History,
  Image
} from "tiptap-vuetify";
import FileSelector from "./FileSelector.vue";
export default {
  components: { TiptapVuetify },
  data() {
    return {
      extensions: [
        History,
        Blockquote,
        [
          Link,
          {
            renderIn: "bubbleMenu"
          }
        ],
        [
          Underline,
          {
            renderIn: "bubbleMenu"
          }
        ],
        [
          Strike,
          {
            renderIn: "bubbleMenu"
          }
        ],
        [
          Bold,
          {
            renderIn: "bubbleMenu",
            // extension's options
            options: {
              levels: [1, 2, 3]
            }
          }
        ],
        Italic,
        ListItem,
        BulletList,
        OrderedList,
        [
          Heading,
          {
            options: {
              levels: [1, 2, 3]
            }
          }
        ],
        Code,
        HorizontalRule,
        Paragraph,
        HardBreak,
        [
          Image,
          {
            options: {
              imageSources: [{ component: FileSelector, name: "File Selector" }]
            }
          }
        ]
      ],
      // starting editor's content
      content: `
      <h1>Yay Headlines!</h1>
      <p>All these <strong>cool tags</strong> are working now.</p>
    `,
      dialog: false
    };
  },
  methods: {
    onkeydown(event) {
      console.log("event", event.key, this.content);
    }
  }
};
</script>
