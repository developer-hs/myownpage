import { createSlice } from "@reduxjs/toolkit/";
import api from "../api";

const userSlice = createSlice({
  name: "users",
  initialState: {
    isLoggedIn: false,
    token: null,
  },
  reducers: {
    logIn(state, action) {
      state.isLoggedIn = true;
      state.token = action.payload.token;
      state.id = action.payload.id;
      state.point = action.payload.point;
      state.free_point = action.payload.free_point;
    },
    logOut(state, action) {
      state.isLoggedIn = false;
      state.token = null;
      state.id = null;
      state.point = null;
      state.free_point = null;
    },
  },
});

export const { logIn, logOut } = userSlice.actions;

export const userLogin = (form) => async (dispatch) => {
  try {
    const {
      data: { id, token },
    } = await api.login(form);
    if (id && token) {
      dispatch(logIn({ token, id }));
    }
  } catch (e) {
    console.log(e);
    alert("Wrong user/password");
  }
};

export default userSlice.reducer;
