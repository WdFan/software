import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    redirect: '/home'
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/signup',
    name: 'signup',
    component: () => import('../views/Signup.vue')
  },
  {
    path: '/home',
    name: 'home',
    component: () => import('../views/Home/index.vue'),
    children: [
      {
        path: '/home/index',
        name: 'index',
        component: () => import("../views/Home/index/index.vue")
      }
    ]
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const isLogin = sessionStorage.getItem('is_login');
  if (isLogin) {
    if (to.path !== '/Login')
      next();
    else
      next('/home')
  } else {
    if (to.path !== '/Login' && to.path !== '/signup')
      next('/Login');
    else
      next();
  }
});

export default router
