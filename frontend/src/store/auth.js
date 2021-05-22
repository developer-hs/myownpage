export default {
  namespaced: true,
  state: {
    token: localStorage.getItem("access_token"),
  },
  mutations: {
    setToken(state, token) {
      state.token = token;
      localStorage.setItem("access_token", token);
    },
  },
  actions: {},
};
