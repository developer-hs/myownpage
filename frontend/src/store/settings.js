export default {
  namespaced: true,
  state: {
    footer: {
      inset: false,
    },
    drawers: ["Default (no property)", "Permanent", "Temporary"],
    primaryDrawer: {
      model: null,
      type: "default (no property)",
      clipped: true,
      floating: false,
      mini: false,
    },
  },
  getters: {},
  mutations: {},
  actions: {},
};
