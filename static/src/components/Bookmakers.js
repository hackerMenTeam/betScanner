import React, {Component} from 'react';
import {list_bookmakers} from "../utils/http_functions";

class Bookmakers extends Component {

    constructor(props) {
        super(props);
        this.state = {
            bookmakers: [],
        }
    }

    componentDidMount() {
        list_bookmakers().then(({data}) => {
            this.setState({bookmakers: data});
        })
    }

    render() {
        return <ul>
            {this.state.bookmakers.map(bookmaker => <li key={bookmaker}>{bookmaker}</li>)}
            </ul>;
    }
}

export default Bookmakers;
