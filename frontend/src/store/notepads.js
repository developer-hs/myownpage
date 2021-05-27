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
    appendMemo(state, memo) {
      const fullMemo = { memo, datetime_created: new Date() };
      state.notepad.unshift(fullMemo);
    },
    removeMemo(state, memo) {
      for (let i = 0; i < state.notepad.length; i++) {
        if (state.notepad[i].memo === memo) {
          state.notepad.splice(i, 1);
        }
      }
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
    createMemo({ commit }, memo) {
      callApi("post", "/notepad/memo", memo, store.state.auth.token)
        .then((response) => {
          if (response.status == 201) {
            commit("appendMemo", memo.memo);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    removeMemo({ commit }, memo) {
      callApi(
        "post",
        `/notepad/memo/delete`,
        { memo: memo },
        store.state.auth.token
      )
        .then((response) => {
          if (response.status === 200) {
            commit("removeMemo", memo);
          }
        })
        .catch((error) => {
          console.log(console.log(error));
        });
    },
  },
};
