import store from ".";
import callApi from "../api/callApi";
export default {
  namespaced: true,
  state: {
    notepad: {},
    totalMemoCount: "",
    nextPage: "",
    prevPage: "",
    pageSize: 1,
    doneCount: 0
  },
  getters: {
    getTotalCount(state) {
      return state.totalMemoCount;
    }
  },
  mutations: {
    setNotepad(state, paginator) {
      state.notepad = paginator.results;
      state.nextPage = paginator.links.next;
      state.totalMemoCount = paginator.count;
      state.pageSize = paginator.page_size;
      state.doneCount = paginator.done_count;
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
    createMemo({ dispatch }, memo) {
      callApi("post", "/notepad/memo", memo, store.state.auth.token)
        .then(response => {
          if (response.status == 201) {
            dispatch("getNotepad");
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    removeMemo({ dispatch }, pk) {
      callApi("delete", `/notepad/memo/${pk}/`, null, store.state.auth.token)
        .then(response => {
          if (response.status === 204) {
            dispatch("getNotepad");
          }
        })
        .catch(error => {
          console.log(console.log(error));
        });
    },
    updateMemo({ dispatch }, obj) {
      callApi(
        "put",
        `/notepad/memo/${obj.updateNote.id}/`,
        obj.updateNote,
        store.state.auth.token
      )
        .then(response => {
          if (response.status === 200) {
            dispatch("getNotepad", obj.page);
          }
        })
        .catch(error => console.log(error));
    }
  }
};
