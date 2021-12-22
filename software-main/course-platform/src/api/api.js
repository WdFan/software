import axios from './index'

export const getUser=() => {return axios.get('http://localhost:8000/api/loginUser/')}