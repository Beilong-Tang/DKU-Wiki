import { createStore } from 'vuex'

export default createStore({
  state: {
    isLogin:false,
  },
  getters: {
  },
  mutations: {
    Login(state){
      console.log("state login")
      state.isLogin = true;
    },

    Logout(state){
      console.log("state logout")
      state.isLogin = false;
    }
    

    // initializeStore(state){
    //   if (localStorage.getItem('token')){
    //     state.token=localStorage.getItem('token');
    //     state.isAuthenticated = true;
    //   } else{
    //     state.token= ''
    //     state.isAuthenticated = false;
    //   }
    // },
    // setToken(state,token){
    //   state.token = token
    //   state.isAuthenticated=true
    // },
    // removeToken(state){
    //   state.token=''
    //   state.isAuthenticated=false
    // },  
  },
  actions: {
  },
  modules: {
  }
})
