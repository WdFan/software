import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    redirect: '/home/index'
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
    redirect: '/home/index',
    component: () => import('../views/Home/Home.vue'),
    children: [
      {
        path: '/home/index',
        name: 'index',
        component: () => import("../views/Home/index/index.vue")
      },
      {
        path: '/home/personal',
        name: 'personal',
        component: () => import("../views/Home/index/personal.vue")
      },
      {
        path: '/home/studentLog',
        name: 'studentLog',
        component: () => import("../views/Home/index/studentLog.vue")
      },
      {
        path: '/home/teacherLog',
        name: 'teacherLog',
        component: () => import("../views/Home/index/teacherLog.vue")
      }
    ]
  },
  {
    path: '/:pathMatch(.*)*',
    name: '404',
    component: () => import("../views/ErrorPage.vue")
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const isLogin = localStorage.getItem('is_login');
  if (isLogin) {
    if (to.path == '/login' || to.path == '/signup')
      next('/home/index');
    else
      next();
  } else {
    if (to.path == '/login' || to.path == '/signup')
      next();
    else
      next('/login');
  }
});

export default router
