import { createStore } from 'vuex'

export default createStore({
  state: {
    isLogin:false,
    //authentication
    auth_info : null,
    search:"",
    tags:[],
  },
  getters: {

    get_auth_info(state){
      return state.auth_info
    },

    get_search(state){
      return state.search
    },

    get_tags(state){
      return state.tags
    }

  },
  mutations: {
    Login(state,data){
      console.log("state login")
      state.isLogin = true;
      state.auth_info=data
    },

    Logout(state){
      console.log("state logout")
      state.isLogin = false;
    }
    
  },
  actions: {
  },
  modules: {
  }
})
