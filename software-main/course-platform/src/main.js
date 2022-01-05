import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import installElementPlus from './plugins/element'
import * as ElIconModules from '@element-plus/icons'
import dayjs from 'dayjs'
import 'vditor/dist/index.css';
import VueVditor from 'vue-vditor';

const app = createApp(App)
installElementPlus(app)
for (let iconName in ElIconModules) {
  app.component(iconName, ElIconModules[iconName])
}
app.config.globalProperties.$dayjs = dayjs
app.use(VueVditor)
app.use(store).use(router)
app.mount('#app')