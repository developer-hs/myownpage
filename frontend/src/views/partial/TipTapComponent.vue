<template>
  <tiptap-vuetify
    v-model="content"
    :extensions="extensions"
    :toolbar-attributes="{ color: 'brown lighten-3' }"
    placeholder="Write something …"
    @keydown="onkeydown"
  />
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
  History
} from "tiptap-vuetify";
export default {
  props: {
    body: {
      type: String
    }
  },
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
        HardBreak
      ],
      // starting editor's content
      content: ""
    };
  },
  computed: {
    storeContent() {
      return this.$store.state.tiptap.content;
    }
  },
  watch: {
    storeContent(val) {
      this.content = val;
    }
  },
  methods: {
    onkeydown() {
      this.$emit("changeContent", this.content);
    }
  }
};
</script>
