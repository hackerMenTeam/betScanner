import React, { Component } from 'react';
import _ from 'lodash';

class SureBetsTable extends Component {

    constructor(props) {
        super(props);
        this.state = {
            forkToExpandedMap: {},
            betIdToStakeMap: {},
        };
    }

    calculateProfit = () => 0;

    calculateWinning = (bet) => {
        const stake = this.state.betIdToStakeMap[bet.id];
        return stake
            ? bet.odd * stake
            : null;
    }

    toggleForkDetails = (forkId) => this.setState((prevState) => ({
        forkToExpandedMap: {
            ...prevState.forkToExpandedMap,
            [forkId]: !(prevState.forkToExpandedMap[forkId] || false)
        }
    }));

    renderForkDetails = (bets) => <table>
                                <thead>
                                <th>Team\Player</th>
                                <th>Bookmaker</th>
                                <th>Odds</th>
                                <th>Stakes</th>
                                <th>Winnings</th>
                                </thead>
                                <tbody>
                                {bets.map(bet => <tr>
                                    <td>{`${bet.match.title} (${bet.exodus})`}</td>
                                    <td>{bet.bookmaker.name}</td>
                                    <td>{bet.odd}</td>
                                    <td>{this.state.betIdToStakeMap[bet.id]}</td>
                                    <td>{this.calculateWinning(bet)}</td>
                                </tr>)}
                                </tbody>
                            </table>;

    render() {
        return (
            <table>
                <thead>
                <tr>
                    <th>Match (market)</th>
                    <th>Sport</th>
                    <th>Championship</th>
                    <th>Bookmakers</th>
                    <th>Profit</th>
                    <th>Found at</th>
                </tr>
                </thead>
                <tbody>
                {_.map(this.props.forks, (sureBet, key) => <>
                    <tr onClick={() => this.toggleForkDetails(sureBet.id)}>
                        <td>{sureBet.bets[0].match.title}</td>
                        <td>{sureBet.bets[0].match.sport}</td>
                        <td>{sureBet.bets[0].match.championship}</td>
                        <td>{sureBet.bets.map(bet => <span>{bet.bookmaker.name}</span>)}</td>
                        <td>{this.calculateProfit(sureBet)}</td>
                        <td>{sureBet.timestamp}</td>
                    </tr>
                    {this.state.forkToExpandedMap[key] && <tr>
                        <td colSpan={6}>
                            {this.renderForkDetails(sureBet.bets)}
                        </td>
                    </tr>}
                </>)}
                </tbody>
            </table>
        );
    }
}

export default SureBetsTable;
