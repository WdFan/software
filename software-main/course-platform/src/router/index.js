import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Teacher from '../views/Teacher.vue'
import Student from '../views/Student.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/teacher',
    name: 'Teacher',
    component: Teacher
  },
  {
    path: '/student',
    name: 'Student',
    component: Student
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
