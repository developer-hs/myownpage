import store from "../store";
import axios from "axios";
export default {
  namespaced: true,
  state: {
    weatherCondition: { weather: [{ main: "Sun" }] }
  },
  getters: {},
  mutations: {
    setWeather(state, weather) {
      state.weatherCondition = weather;
      console.log(weather);
    }
  },
  actions: {
    getResWeather({ commit }) {
      const residence = store.state.auth.userInfo.residence;
      axios["get"](
        `https://api.openweathermap.org/data/2.5/weather?id=${residence}&units=metric&appid=eba302c9974e0f1906f4c12247fa990b`
      )
        .then(response => {
          if (response.status === 200) {
            commit("setWeather", response.data);
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    getGeoWeather({ commit }) {
      const [lat, lon] = navigator.geolocation.getCurrentPosition(position => {
        return [position.coords.latitude, position.coords.longitude];
      });
      console.log("awjdliawjdlkawjdkla");
      console.log(lat, lon);
      axios["get"](
        `api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&units=metric&appid=eba302c9974e0f1906f4c12247fa990b`
      )
        .then(response => {
          if (response.status === 200) {
            commit("setWeather", response.data);
          }
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
