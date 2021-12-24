import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import installElementPlus from './plugins/element'
import * as ElIconModules from '@element-plus/icons'

const app = createApp(App)
installElementPlus(app)
for (let iconName in ElIconModules) {
  app.component(iconName, ElIconModules[iconName])
}
app.use(store).use(router).mount('#app')