import callApi from "../api/callApi";
import store from "../store";
export default {
  namespaced: true,
  state: {
    schedule: {},
  },
  mutations: {
    setSchedule(state, schedule) {
      state.schedule = schedule;
    },
  },
  actions: {
    getSchedule({ commit }) {
      callApi("get", "/schedule/", null, store.state.auth.token)
        .then((response) => {
          if (response.status === 200) {
            commit("setSchedule", response.data);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
