import { createApp } from 'vue'
import App from '@/App.vue'
import Axios from 'axios'

const app = createApp(App)

const axios = Axios.create({
  withCredentials: true
})

axios.defaults.baseURL = 'http://localhost:8000'

axios.interceptors.request.use(
  config => {
    return config
  }, error => {
    return Promise.reject(error)
  }
)

axios.interceptors.response.use(
  response => {
    return response
  },
  error => {
    return Promise.reject(error)
  }
)

app.config.globalProperties.axios = axios

export default axios