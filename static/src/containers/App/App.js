import React, {Component} from 'react';
import {Link} from "react-router";
import {perform_scanning, stop_scanner} from "../../utils/http_functions";

class App extends Component {

    constructor(props) {
        super(props);
        this.state = {
            matches: [],
            counter: 0,
        };
    }

    onScan = () => {
        perform_scanning().then(({data}) => {
            this.setState(prevState => ({matches: data, counter: prevState.counter + 1}))
        })
    }

    onStopScanner = () => {
        stop_scanner();
    }

    render() {
        return (
            <div>
                <h1>Bet Scanner by HackerMen team</h1>
                <Link to="bookmakers">Check out bookmakers</Link>
                <button onClick={this.onScan}>Scan</button>
                <button onClick={this.onStopScanner}>Stop scanner</button>
                scanned {this.state.counter} times
                <br/>
                <textarea readOnly={true}
                          name="matches"
                          id="matches"
                          cols="80"
                          rows="20"
                          value={JSON.stringify(this.state.matches)}/>
            </div>
        );
    }
}

export {App};
