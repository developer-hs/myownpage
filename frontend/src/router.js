import Vue from "vue";
import VueRouter from "vue-router";
import Home from "./views/Home";
import About from "./views/About";
import Login from "./views/auth/Login";
import SignUp from "./views/auth/SignUp";

Vue.use(VueRouter);

const router = new VueRouter({
  mode: "history",
  routes: [
    { path: "/", component: Home },
    { path: "/login", component: Login },
    { path: "/auth/sign-up", component: SignUp, name: "signup" },
    { path: "/about", component: About },
  ],
});

export default router;
