import axios from './index'

export const getUser = () => { return axios.get('/api/loginUser/') }

export const login = (username, password) => { return axios.post('/api/login/', { 'username': username, 'password': password }) }