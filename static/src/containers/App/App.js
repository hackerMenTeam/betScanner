import React, {Component} from 'react';
import {Link} from "react-router";

class App extends Component {

    render() {
        return (
            <div>
                <h1>Bet Scanner by HackerMen team</h1>
                <Link to="bookmakers">Check out bookmakers</Link>
            </div>
        );
    }
}

export {App};
