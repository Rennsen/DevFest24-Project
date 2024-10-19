import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import CategorieView from '@/views/CategorieView.vue';
import NotFoundView from '@/views/NotFoundView.vue';
import MachineView from '@/views/MachineView.vue';
import Login from '@/views/Login.vue';
import AddUser from '@/views/AddUser.vue';
const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: { requiresAuth: true }
    },
    {
      path: '/categories/:ctg(cnc|sp|ltm|avg|pm|wr)',
      name: 'categories',
      component: CategorieView,
      meta: { requiresAuth: true }
    },
    {
      path: '/categories/:ctg(cnc|sp|ltm|avg|pm|wr)/:id(\\d+)',
      name: 'machines',
      component: MachineView,
      meta: { requiresAuth: true }
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
    {
      path: '/users/add',
      name: 'add-user',
      component: AddUser,
    },
    {
      path : '/:catchAll(.*)',
      name : 'not_found',
      component : NotFoundView,
    }
  ]
})

router.beforeEach((to, from, next) => {
  const isLoggedIn = !!localStorage.getItem('token'); // Check if user is logged in

  if (to.matched.some(record => record.meta.requiresAuth) && !isLoggedIn) {
    next('/login');
  } else {
    next();
  }
});

export default router;