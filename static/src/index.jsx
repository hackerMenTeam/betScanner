import React from 'react';
import ReactDOM from 'react-dom';
import App from "./containers/App/App";
import {
    BrowserRouter as Router,
    Switch,
    Route
} from "react-router-dom";
import Bookmakers from "./components/Bookmakers";

ReactDOM.render(
    <Router>
        <Switch>
            <Route path="/bookmakers">
                <Bookmakers/>
            </Route>
            <Route path="/">
                <App/>
            </Route>
        </Switch>
    </Router>,
    document.getElementById('root')
);

if (module.hot) {
    module.hot.accept();
}
