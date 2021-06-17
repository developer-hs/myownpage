import { Mark } from "tiptap-extensions";
export default class Paragraph extends Mark {
  get schema() {
    return {
      attrs: {},
      inclusive: false,
      parseDOM: [
        {
          tag: "a[href]"
        }
      ],
      toDOM: node => [
        "p",
        {
          ...node.attrs
        },
        0
      ]
    };
  }
}
