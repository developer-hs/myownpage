import { Provider } from "react-redux";
import store, { persistor } from "./redux/store";
import { Route, BrowserRouter } from "react-router-dom";
import { PersistGate } from "redux-persist/integration/react";
import Home from "./routes/Home";

function App() {
  return (
    <BrowserRouter>
      <Provider store={store}>
        <PersistGate persistor={persistor}>
          <Home />
        </PersistGate>
      </Provider>
    </BrowserRouter>
  );
}

export default App;
