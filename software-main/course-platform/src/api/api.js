import axios from './index'

export const getUser = () => { return axios.get('/api/loginUser/') }