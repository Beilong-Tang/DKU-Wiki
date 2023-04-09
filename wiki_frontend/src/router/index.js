import { createRouter, createWebHashHistory, createWebHistory } from 'vue-router'
import LogIn from '../views/LogIn.vue'
import SignUp from '../views/SignUp.vue'
import EntryList from '../views/EntryList.vue'
import DetailEntry from '../views/DetailEntry.vue'
import CreateEntry from '../views/CreateEntry.vue'
import Index from '../views/Index.vue'
import TagList from '../views/TagList.vue'
import My from '../views/my.vue'

const routes = [
  {
    path: '/LogIn',
    name: 'LogIn',
    component:LogIn
  },
  {
    path: '/SignUp',
    name: 'SignUp',
    component:SignUp
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
    component:TagList
  },


  // index page
  {
    path: '/indexing/',
    name: 'Index',
    component: Index
  },
  {
    path: '/entry/:id',
    name: 'DetailEntry',
    component:DetailEntry
  },
  {
    path: '/CreateEntry',
    name: 'CreateEntry',
    component:CreateEntry
  },
   {
    path: '/My',
    name: 'My',
    component:My
  },
]

const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes
})

export default router
