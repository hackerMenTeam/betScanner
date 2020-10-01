/* eslint camelcase: 0 */

import axios from 'axios';

export function list_bookmakers() {
    return axios.get('/api/list_bookmakers');
}
