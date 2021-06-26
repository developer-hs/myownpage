import store from "../store";
import axios from "axios";
export default {
  namespaced: true,
  state: {
    weatherCondition: { weather: [{ main: "Sun" }] },
    responseCompletion: false
  },
  getters: {},
  mutations: {
    setWeather(state, weather) {
      state.weatherCondition = weather;
      state.responseCompletion = true;
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
    getGeoWeather({ commit, dispatch }, geo) {
      console.log("GeoGeoGeoGeoGeoGeoGeoGeoGeoGeoGeoGeoGeoGeo");
      console.log(geo);
      axios["get"](
        `https://api.openweathermap.org/data/2.5/weather?lat=${geo.lat}&lon=${geo.lon}&units=metric&appid=eba302c9974e0f1906f4c12247fa990b`
      )
        .then(response => {
          if (response.status === 200) {
            console.log(response.data);
            commit("setWeather", response.data);
          }
        })
        .catch(error => {
          dispatch("getResWeather");
          console.log(error);
        });
    }
  }
};
