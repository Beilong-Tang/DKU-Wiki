<template>

  <div v-if="show_nav">
    <TopNav />
  </div>
  <nav>
    
  </nav>
  <router-view />

  

</template>

<script>

import TopNav from './components/TopNav.vue'
export default {
  name: 'App',
  components: { TopNav },
  data() {
    return {
      show_nav: true
    }
  },
  // inject:['nav_show'],
  beforecreated() {
    this.nav_show();
    this.$router.replace({name:'Home',params:{search:'all'}});
  },
  provide() {
    return {
      nav_hide: this.nav_hide,
      nav_show: this.nav_show
    }
  },

  methods: {
    nav_hide() {
      this.show_nav = false
    },

    nav_show() {
      this.show_nav = true
    }
  }
}

</script>


<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
