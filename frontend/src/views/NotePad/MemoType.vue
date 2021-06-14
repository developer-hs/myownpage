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
    <v-dialog v-model="dialog" max-width="70rem">
      <v-card class="pa-6">
        <tiptap-vuetify
          v-model="content"
          :extensions="extensions"
          placeholder="Write something …"
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

export default {
  components: { TiptapVuetify },
  data() {
    return {
      extensions: [
        History,
        Blockquote,
        Link,
        Underline,
        Strike,
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
        Bold,
        Code,
        HorizontalRule,
        Paragraph,
        HardBreak,
        Image
      ],
      // starting editor's content
      content: `
      <h1>Yay Headlines!</h1>
      <p>All these <strong>cool tags</strong> are working now.</p>
    `,
      dialog: false
    };
  }
};
</script>
