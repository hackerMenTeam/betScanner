import React from 'react';
import {Router, Route ,Redirect} from 'react-router';

import { App } from './containers/App/App';
import Bookmakers from './components/Bookmakers';

export default (
    <Router>
        <Route path="/" component={App} />
        <Route path="/bookmakers" component={Bookmakers} />
    </Router>
);
