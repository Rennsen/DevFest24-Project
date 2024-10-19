<script setup>
import { useRoute ,useRouter } from 'vue-router';
import { logout } from '@/store';
import { useToast } from 'vue-toastification';
import ConfirmLogout from './ConfirmLogout.vue';
const route = useRoute(); // call useRoute once
const router = useRouter();
const toast = useToast();
const activeLink = (routerPath) => {
  return route.path === routerPath; // use the route variable
};
const logoutUser = () => {
  logout();
  router.push('/login')
}

const confirmLogout = () => {
  toast(
    {
      component: ConfirmLogout,
      listeners: {
        confirm: () => {
          logoutUser();
          toast.dismiss(); // Close the toast after confirming
        },
        cancel: () => {
          toast.info('تم إلغاء تسجيل الخروج.');
          toast.dismiss(); // Close the toast after cancelling
        },
      },
    },
    {
      type: 'default',
      timeout: false, // Keeps the toast open until an action is taken
      closeOnClick: true,
      draggable: false,
    }
  );
};
</script>

<template>
    <div class="my-height d-flex flex-column p-3 p-lg-4 pt-4 pb-3 bg-hard-night shape">
        <div class="username pb-2 fw-white text-center mb-4 fs-4 position-relative">SOA</div>
        <!-- separator -->
        <div class="routes d-flex flex-column gap-2 mb-4">
            <RouterLink class="d-block link cursor-pointer d-flex flex-row gap-2 align-items-center" to="/">
                <div class="p-2 flex-center bg-dark small text-primary rounded-circle"><i class="fa-solid fa-house"></i></div>
                <div :class="['small', 'fw-bold', 'text-capitalize', activeLink('/') ? 'text-primary' : '']">Dashboard</div>
            </RouterLink>
            <!-- separator -->
            <RouterLink class="link cursor-pointer d-flex flex-row gap-2 align-items-center" to="/tasks">
                <div class="p-2 flex-center bg-dark small text-primary rounded-circle"><i class="fas fa-tasks"></i></div>
                <div :class="['small fw-bold text-capitalize', activeLink('/tasks') ? 'text-primary' : '']">Task schedule</div>
            </RouterLink>
            <!-- separator -->
            <RouterLink class="link cursor-pointer d-flex flex-row gap-2 align-items-center" to="/alerts">
                <div class="p-2 flex-center bg-dark small text-primary rounded-circle"><i class="fa-solid fa-bell"></i></div>
                <div :class="['small fw-bold text-capitalize', activeLink('/alerts') ? 'text-primary' : '']">Alerts</div>
            </RouterLink>
        </div>
        <!-- separator -->
        <div class="routes d-flex flex-column gap-2 mb-4">
            <div class="text-white small fw-light">This is user pages</div>
            <RouterLink class="link cursor-pointer d-flex flex-row gap-2 align-items-center" to="/profile">
                <div class="p-2 flex-center bg-dark small text-primary rounded-circle"><i class="fa-solid fa-user"></i></div>
                <div :class="['small fw-bold text-capitalize', activeLink('/profile') ? 'text-primary' : '']">Profile</div>
            </RouterLink>
            <!-- separator -->
            <a @click="confirmLogout()" class="link cursor-pointer d-flex flex-row gap-2 align-items-center" to="/sign-in">
                <div class="p-2 flex-center bg-dark small text-primary rounded-circle"><i class="fas fa-sign-in"></i></div>
                <div :class="['small fw-bold text-capitalize']">Log Out</div>
            </a>
            <!-- separator -->
            <RouterLink class="link cursor-pointer d-flex flex-row gap-2 align-items-center" to="/sign-up">
                <div class="p-2 flex-center bg-dark small text-primary rounded-circle"><i class="fa-solid fa-user-plus"></i></div>
                <div :class="['small fw-bold text-capitalize', activeLink('/users/add') ? 'text-primary' : '']">Add User</div>
            </RouterLink>
        </div>
        <!-- separator -->
    </div>
</template>

<style lang="scss" scoped>
// .routes > .link:hover > div:last-child {
//     color: #0d6efd;
// }
.small {
    font-size: 0.775rem;
}
.my-height {
    min-height: calc(100vh - 10%);
}
.username {
    &::before {
        content: "";
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 0.5px;
        background: linear-gradient(to right, rgba(255, 255, 255, 0.2), white 50%, rgba(255, 255, 255, 0.2));
    }
}
</style>
