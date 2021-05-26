import auth from "../store/auth";

const notAuthenticated = (route) => {
  if (auth.state.token) {
    this.$router.push(route);
  }
};

export default notAuthenticated;
