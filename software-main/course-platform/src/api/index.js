import { createApp } from 'vue'
import App from '../App.vue'
import Axios from 'axios'

const app = createApp(App)

const axios = Axios.create({
    withCredentials: true
})

axios.defaults.baseURL = 'http://localhost:8000'

axios.interceptors.request.use((config) => {
    config.headers['X-Requested-With'] = 'XMLHttpRequest'
    const regex = /.*csrftoken=([^;.]*).*$/
    config.headers['X-CSRFToken'] = document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1]
    return config
})

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