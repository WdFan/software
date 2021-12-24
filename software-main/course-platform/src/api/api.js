import axios from './index'

export const getUser = () => { return axios.get('/api/loginUser/') }

export const login = (user_info) => { return axios.post('/api/login/', user_info) }

export const signup = (user_info) => { return axios.post('/api/register/', user_info)}