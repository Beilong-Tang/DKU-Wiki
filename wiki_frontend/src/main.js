import { createApp} from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import axios from 'axios'

import 'bootstrap/dist/css/bootstrap.css'
// import 'jquery/dist/jquery.js'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'
import 'bootstrap/dist/js/bootstrap.bundle.js'
import 'bootstrap/dist/js/bootstrap.min.js'

import 'quill/dist/quill.core.css' // 引入样式
import 'quill/dist/quill.snow.css' // snow theme
import 'quill/dist/quill.bubble.css' // bubble theme

const baseurl = 'http://127.0.0.1:8000'


axios.defaults.baseURL = 'http://127.0.0.1:8000'
axios.defaults.withCredentials = true;

const app1 = createApp(App).use(store).use(router,axios);
app1.config.globalProperties.global={
    baseurl:baseurl
};

app1.mount("#app")





