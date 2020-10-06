/* eslint camelcase: 0 */

import axios from 'axios';

export const list_bookmakers = () => axios.get('/api/list_bookmakers');

export const perform_scanning = () => axios.post('/api/scan');

export const stop_scanner = () => axios.post('/api/stop_scanner');

export const list_forks = () => axios.get('/api/list_forks');
