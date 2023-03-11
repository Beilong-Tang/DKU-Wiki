import { createRouter, createWebHistory } from 'vue-router'
// import LogIn from '../views/LogIn.vue'
// import SignUp from '../views/SignUp.vue'
import EntryList from '../views/EntryList.vue'
// import DetailEntry from '../views/DetailEntry.vue'
import Index from '../views/Index.vue'

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
  //entry page
  {
    path: '/entry',
    name: 'EntryList',
    component: EntryList
  },

  {
    path:"/tags",
    name:"TagList",
    component:()=>import('../views/TagList.vue')
  },


  // index page
  {
    path: '/index/',
    name: 'Index',
    component: Index
  },
  {
    path: '/entry/:id',
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
