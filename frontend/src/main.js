import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'


const app = createApp(App)
const BACKEND_URL = "http://127.0.0.1:8000";

axios.defaults.baseURL = BACKEND_URL;
app.use(router, axios)

app.mount('#app')

/* import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

const app = createApp(App);

app.use(router);
app.mount('#app'); */
