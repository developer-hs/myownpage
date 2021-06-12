import store from ".";
import callApi from "../api/callApi";
export default {
  namespaced: true,
  state: {
    notepad: {},
    totalMemoCount : "",
    next_page : "",
    prev_page : ""
  },
  getters: {},
  mutations: {
    setNotepad(state, paginator) {
      console.log(paginator.count)
      state.notepad = paginator.results;
      state.next_page = paginator.links.next
      state.totalMemoCount = paginator.count
      console.log(state.totalMemoCount)
    },
    appendMemo(state, memo) {
      state.notepad.unshift(memo);
    },
    removeMemo(state, pk) {
      for (let i = 0; i < state.notepad.length; i++) {
        if (state.notepad[i].id === pk) {
          state.notepad.splice(i, 1);
        }
      }
    }
  },
  actions: {
    getNotepad({ commit }, page = 1) {
      callApi("get", `/notepad/memo?page=${page}`, null, store.state.auth.token)
        .then(response => {
          commit("setNotepad", response.data);
        })
        .catch(error => {
          console.log(error);
        });
    },
    createMemo({ commit }, memo) {
      callApi("post", "/notepad/memo", memo, store.state.auth.token)
        .then(response => {
          if (response.status == 201) {
            commit("appendMemo", response.data);
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    removeMemo({ commit }, pk) {
      callApi("delete", `/notepad/memo/${pk}/`, null, store.state.auth.token)
        .then(response => {
          if (response.status === 200) {
            commit("removeMemo", pk);
          }
        })
        .catch(error => {
          console.log(console.log(error));
        });
    },
    updateMemo(state, memo) {
      callApi("put", `/notepad/memo/${memo.id}/`, memo, store.state.auth.token)
        .then(response => {
          if (response.status === 200) {
            console.log(response);
          }
        })
        .catch(error => console.log(error));
    }
  }
};
