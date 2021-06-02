import store from ".";
import callApi from "../api/callApi";

export default {
  namespaced: true,
  state: {
    searchHistory: {},
  },
  getters: {},
  mutations: {
    setSearchHistory(state, searchHistory) {
      state.searchHistory = searchHistory;
    },
    addSearchHistory(state, searchHistory) {
      state.searchHistory.unshift(searchHistory);
    },
    removeSearchHistory(state, pk) {
      for (let i = 0; i < state.searchHistory.length; i++) {
        if (state.searchHistory[i].id === pk) {
          state.searchHistory.splice(i, 1);
        }
      }
    },
  },
  actions: {
    getSearchHistory({ commit }) {
      callApi("get", "/search/history/", null, store.state.auth.token)
        .then((response) => {
          if (response.status === 200) {
            commit("setSearchHistory", response.data);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    createSearchHistory({ commit }, searchTerm) {
      callApi(
        "post",
        "/search/history/",
        { search_term: searchTerm },
        store.state.auth.token
      )
        .then((response) => {
          if (response.status === 201) {
            commit("addSearchHistory", response.data);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    removeSearchHistory({ commit }, pk) {
      callApi("delete", `/search/history/${pk}`, null, store.state.auth.token)
        .then((response) => {
          if (response.status === 200) {
            commit("removeSearchHistory", pk);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
