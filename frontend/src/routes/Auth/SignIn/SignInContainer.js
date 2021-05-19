import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { logOut, userLogin } from "../../../redux/userSlice";
import "../../../style/scss/SignIn.sass";
export default (props) => {
  const { isLoggedIn } = useSelector((state) => state.usersReducer);
  const dispatch = useDispatch();
  const [email, setEmail] = useState(props?.email || "");
  const [password, setPassword] = useState(props?.password | "");
  const onChangeEmail = (e) => {
    setEmail(e.target.value);
  };
  const onChangePassword = (e) => {
    setPassword(e.target.value);
  };
  const handleSubmit = async () => {
    await dispatch(
      userLogin({
        username: email,
        password,
      })
    );
    document.location = "http://localhost:3000/";
  };
  const handleLogOut = async () => {
    dispatch(logOut());
  };
  return isLoggedIn ? (
    <div>
      <button onClick={handleLogOut}>LogOut</button>
    </div>
  ) : (
    <div>
      <div>
        <div>
          <h1>LogIn</h1>
          <input
            className="login-email"
            type="email"
            value={email}
            onChange={onChangeEmail}
            placeholder="Email"
          />
          <input
            className="login-password"
            type="password"
            value={password}
            onChange={onChangePassword}
            placeholder="Password"
          />
          <button onClick={handleSubmit}>Login</button>
        </div>
      </div>
    </div>
  );
};
