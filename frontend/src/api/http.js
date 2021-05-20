import store from "../store";
import axios from "axios";

const instance = axios.create({
  baseURL: process.env.VUE_APP_API,
});

instance.interceptors.request.use(function(config) {
  if (store.state.auth.token !== null) {
    config["headers"] = {
      Authorization: `Bearer ${store.state.auth.token}`,
    };
  }

  return config;
});
