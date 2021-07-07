import { AccessToken } from "../variable";
import callApi from "../api/callApi";

export default {
  namespaced: true,
  state: {
    // data
    token: localStorage.getItem(AccessToken),
    isLoginError: false,
    userInfo: {}
  },
  getters: {
    // computed
  },
  mutations: {
    setToken(state, token) {
      state.token = token;
      state.isLoginError = false;
      localStorage.setItem(AccessToken, token);
    },
    setUserInfo(state, info) {
      state.userInfo = info;
    },
    loginError(state) {
      state.isLoginError = true;
    },
    logOut() {
      localStorage.removeItem(AccessToken);
      window.location.reload();
    }
  },
  actions: {
    logIn({ commit }, loginObj) {
      callApi("post", "/token/", {
        username: loginObj.username,
        password: loginObj.password
      })
        .then(response => {
          if (response.status === 200) {
            commit("setToken", response.data.token);
            window.location.reload();
          }
        })
        .catch(error => {
          if (error.response.status == 401) {
            commit("loginError");
          }
        });
    },
    logOut({ commit }) {
      commit("logOut");
    },
    tokenVerify({ state, commit }) {
      callApi("post", "/token/verify/", { token: state.token }, null)
        .then(response => console.log(response))
        .catch(error => {
          console.log(error.response.status);
          commit("logOut");
        });
    },
    getUserInfo({ state, commit, dispatch }) {
      dispatch("tokenVerify");
      callApi("post", "/users/user_info", null, state.token)
        .then(response => {
          if (response.status === 200) {
            commit("setUserInfo", response.data);
          }
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
