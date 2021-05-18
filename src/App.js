import logo from "./logo.svg";
import "./App.css";
import { Provider } from "react-redux";
import store, { persistor } from "./redux/store";
import { Route, BrowserRouter } from "react-router-dom";
import { PersistGate } from "redux-persist/integration/react";

function App() {
  return (
    <BrowserRouter>
      <Provider store={store}>
        <PersistGate persistor={persistor}>
          <Route path="/user/login/" exact={true} component={SignInContainer} />
        </PersistGate>
      </Provider>
    </BrowserRouter>
  );
}

export default App;
