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
    appendSchedule(state, schedule) {
      state.schdule = state.schedule.push(schedule);
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
    createSchedule({ commit }, schdule) {
      callApi("post", "/schedule/", schdule, store.state.auth.token)
        .then((response) => {
          if (response.status === 201) {
            commit("appendSchedule", response.data);
          }
        })
        .catch((error) => console.log(error));
    },
    deleteSchedule({ dispatch }, pk) {
      callApi("delete", `/schedule/${pk}/`, null, store.state.auth.token)
        .then((response) => {
          if (response.status === 200) {
            dispatch("getSchedule");
          }
        })
        .catch((error) => console.log(error));
    },
    updateSchedule({ commit }, schedule) {
      console.log(schedule);
      callApi(
        "put",
        `/schedule/${schedule.id}/`,
        schedule,
        store.state.auth.token
      )
        .then((response) => {
          console.log(response);
          commit;
        })
        .catch((error) => console.log(error));
    },
  },
};
