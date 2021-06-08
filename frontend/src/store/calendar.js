import callApi from "../api/callApi";
import store from "../store";
export default {
  namespaced: true,
  state: {
    schedule: {},
  },
  mutations: {
    setSchedule(state, schedule) {
      for (let i = 0; i < schedule.length; i++) {
        schedule[i].start = new Date(schedule[i].start);
        schedule[i].end = new Date(schedule[i].end);
      }
      console.log(schedule);
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
    createSchedule({ dispatch }, schedule) {
      callApi("post", "/schedule/", schedule, store.state.auth.token)
        .then((response) => {
          if (response.status === 201) {
            dispatch("getSchedule");
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
    updateSchedule({ dispatch }, schedule) {
      console.log(schedule);
      callApi(
        "put",
        `/schedule/${schedule.id}/`,
        schedule,
        store.state.auth.token
      )
        .then((response) => {
          if (response.status === 200) {
            dispatch("getSchedule");
          }
        })
        .catch((error) => console.log(error));
    },
  },
};
