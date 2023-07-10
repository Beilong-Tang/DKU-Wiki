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
      data.client.avator = data.client.avator
      state.auth_info=data
    },

    Logout(state){
      console.log("state logout")
      state.isLogin = false;
    },

    change_tag(state,tag){
      state.tag = tag;
    },

    change_search(state,search){
      state.search = search 
    },

    change_vator(state,url){
      console.log(url)
    },
    
    
  },
  actions: {
  },
  modules: {
  }
})
