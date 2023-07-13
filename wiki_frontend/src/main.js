import { createApp} from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import axios from 'axios'

// quill

//------
import 'bootstrap/dist/css/bootstrap.css'

import 'bootstrap/dist/js/bootstrap.bundle.min.js'

//v-md-editor
import VMdEditor from '@kangc/v-md-editor';
import '@kangc/v-md-editor/lib/style/base-editor.css';
import githubTheme from '@kangc/v-md-editor/lib/theme/github.js';
import '@kangc/v-md-editor/lib/theme/style/github.css';
import createKatexPlugin from '@kangc/v-md-editor/lib/plugins/katex/cdn';
// highlightjs
import hljs from 'highlight.js';


VMdEditor.use(githubTheme, {
  Hljs: hljs,

});

VMdEditor.use(createKatexPlugin())


// const baseurl = 'http://127.0.0.1:8000'
// const baseurl = 'http://dku-vcm-2630.vm.duke.edu:8001'
// const baseurl = 'http://10.200.20.199:8002'
const baseurl = "http://hun.colab.dukekunshan.edu.cn:8001"


axios.defaults.baseURL = baseurl
axios.defaults.withCredentials = true;

const app1 = createApp(App).use(store).use(router,axios);
app1.config.globalProperties.global={
    baseurl:baseurl
};

app1.use(VMdEditor)
app1.mount("#app")






