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

    formatYesNo = (value) => value ? 'Yes' : 'No';

    render() {
        return <div>
            <h2>We are scanning the following bookmakers at the moment</h2>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Enabled</th>
                        <th>VPN required</th>
                        <th>URL</th>
                    </tr>
                </thead>
                <tbody>
                    {this.state.bookmakers.map(bookmaker => <tr key={bookmaker}>
                        <td>{bookmaker.name}</td>
                        <td>{this.formatYesNo(bookmaker.is_enabled)}</td>
                        <td>{this.formatYesNo(bookmaker.vpn_required)}</td>
                        <td><a href={bookmaker.url} target="_blank">[open]</a></td>
                    </tr>)}
                </tbody>
            </table>
        </div>;
    }
}

export default Bookmakers;
