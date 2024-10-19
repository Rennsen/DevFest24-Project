import './assets/bootstrap.min.css';
import './assets/bootstrap.bundle.min.js';
import './assets/all.min.css';
import './assets/main.css';
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import Toast from 'vue-toastification';
import 'vue-toastification/dist/index.css';



const app = createApp(App);

app.use(router);
app.use(Toast);
app.mount('#app');
