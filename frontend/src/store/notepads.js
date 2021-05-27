import store from ".";
import callApi from "../api/callApi";
export default {
  namespaced: true,
  state: {
    notepad: {},
  },
  getters: {},
  mutations: {
    setNotepad(state, notepad) {
      state.notepad = notepad;
    },
  },
  actions: {
    getNotepad({ commit }) {
      callApi("get", "/notepad/info", null, store.state.auth.token)
        .then((response) => {
          commit("setNotepad", response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
