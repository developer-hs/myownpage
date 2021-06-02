import callApi from "../api/callApi";
import store from "../store";
export default {
  namespaced: true,
  state: {
    bookmark: {},
  },
  getters: {},
  mutations: {
    setBookmark(state, bookmark) {
      state.bookmark = bookmark;
    },
    siteLocked(state, siteName) {
      state.bookmark.locked = siteName;
    },
  },
  actions: {
    getBookmark({ commit }) {
      callApi("get", "/bookmark/", null, store.state.auth.token)
        .then((response) => {
          commit("setBookmark", response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    siteLocked({ commit }, siteName) {
      callApi(
        "put",
        "/bookmark/locked/",
        { locked: siteName },
        store.state.auth.token
      )
        .then((response) => {
          if (response.status === 200) {
            commit("siteLocked", siteName);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
