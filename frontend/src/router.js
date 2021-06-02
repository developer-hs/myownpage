import Vue from "vue";
import VueRouter from "vue-router";
import Login from "@/components/auth/Login";
import Auth from "@/components/auth/Auth";
import store from "./store";
import Setting from "@/components/Setting";
const rejectAuthUser = (to, from, next) => {
  if (store.state.auth.token) {
    next({ name: "home" });
  } else {
    next();
  }
};

const onlyAuthUser = (to, from, next) => {
  if (!store.state.auth.token) {
    next({ name: "login" });
  } else {
    store.dispatch("notepads/getNotepad");
    store.dispatch("auth/getUserInfo");
    store.dispatch("bookmark/getBookmark");
    store.dispatch("search/getSearchHistory");
    store.dispatch("settings/getSites");
    setTimeout(() => {
      next();
    }, 250);
  }
};
Vue.use(VueRouter);
const SignUp = () => import("@/components/auth/SignUp");
const Home = () => import("@/components/Home");

const router = new VueRouter({
  mode: "history",
  routes: [
    { path: "/", component: Home, name: "home", beforeEnter: onlyAuthUser },
    {
      path: "/auth",
      component: Auth,
      name: "auth",
      children: [
        {
          path: "login",
          component: Login,
          name: "login",
          beforeEnter: rejectAuthUser,
        },
        {
          path: "sign-up",
          component: SignUp,
          name: "signup",
          beforeEnter: rejectAuthUser,
        },
      ],
    },
    {
      path: "/setting",
      component: Setting,
      name: "setting",
      beforeEnter: onlyAuthUser,
    },
  ],
});

export default router;
