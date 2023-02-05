import { createRouter, createWebHistory } from 'vue-router'
// import LogIn from '../views/LogIn.vue'
// import SignUp from '../views/SignUp.vue'
import Home from '../views/Home.vue'
// import DetailEntry from '../views/DetailEntry.vue'

const routes = [
  {
    path: '/LogIn',
    name: 'LogIn',
    component:()=>import('../views/LogIn.vue')
  },
  {
    path: '/SignUp',
    name: 'SignUp',
    component:()=>import('../views/SignUp.vue')
  },
  {
    path: '/Home/search=:search',
    name: 'Home',
    component: Home
  },
  {
    path: '/Home/:id',
    name: 'DetailEntry',
    component:()=>import('../views/DetailEntry.vue')
  },
  {
    path: '/CreateEntry',
    name: 'CreateEntry',
    component:()=>import('../views/CreateEntry.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
