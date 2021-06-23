import store from "../store";
import axios from "axios";
export default {
  namespaced: true,
  state: {
    schedule: {}
  },
  getters: {},
  mutations: {},
  actions: {
    getWeather() {
      const residence = store.state.auth.userInfo.residence;
      console.log(residence);
      axios["get"](
        `https://api.openweathermap.org/data/2.5/weather?id=${residence}&units=metric&appid=eba302c9974e0f1906f4c12247fa990b`
      )
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
