import axios from './index'

const api = {
  getUser: () => { return axios.get('/api/loginUser/') },
  login: (user_info) => { return axios.post('/api/login/', user_info) },
  signup: (user_info) => { return axios.post('/api/register/', user_info) },
  getTeachClass: (username) => { return axios.post('/api/getbanjiList/', {'username': username}) },
}

export default api;