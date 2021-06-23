import callApi from "../api/callApi";
import store from "../store";
export default {
  namespaced: true,
  state: {
    dialog: false,
    sites: {}
  },
  getters: {
    settingDialog(state) {
      return state.dialog;
    }
  },
  mutations: {
    setSites(state, allSite) {
      for (let i = 0; i < allSite.length; i++) {
        state.sites[allSite[i].name] = false;
      }
      const userSites = store.state.bookmark.bookmark.sites;
      for (let i = 0; i < userSites.length; i++) {
        state.sites[userSites[i].name] = true;
      }
    },
    dialogToggle(state, bool) {
      state.dialog = bool;
      console.log(state.dialog);
    }
  },
  actions: {
    getSites({ commit }) {
      callApi("get", "/bookmark/sites/", null, store.state.auth.token)
        .then(response => {
          commit("setSites", response.data);
        })
        .catch(error => {
          console.log(error);
        });
    },
    bookmarkSetting({ state }) {
      callApi("put", "/bookmark/", state.sites, store.state.auth.token);
    }
  }
};
