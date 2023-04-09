import { createStore } from 'vuex'

export default createStore({
  state: {
    isLogin:false,
    //authentication
    auth_info : null

  },
  getters: {

    get_auth_info(state){
      return state.auth_info
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
