<script setup>

import axios from 'axios';
import { ref } from 'vue';
import { useRouter , RouterLink} from 'vue-router';
import { login as storeLogin, baseUrl , state } from '@/store';
import { jwtDecode } from 'jwt-decode';
import { useToast } from 'vue-toastification';

const toast = useToast()
const router = useRouter();

const username = ref('');
const password = ref('');
const show = ref(false);
const login = async () => {
  try {
    const response = await axios.post(`${baseUrl}/api/user/login`, {
      username: username.value.trim(),
      password: password.value.trim(),
    });
    console.log(response);
    const token = response.data[0].data.token;
    const user = jwtDecode(token);
    if (user) {
        if(user.is_blocked){
          toast.error('you are blocked!');
        }else{
          storeLogin(token);
          router.push('/')  // Store the token
        }
    } else {
      toast.error('invalid User');
    }
  
  } catch (error) {
    console.error('error when login:', error);
    toast.error('invalid user');
  }
};

</script>

<template>
    <div class="py-4">
        <div v-if="!state.isLoggedIn" class="myContainer mt-4 d-flex flex-column">
            <div class="text-white fw-bold fs-1 text-center mb-3">Login Page</div>
            <form @submit.prevent="login" class="p-2 rounded-3 bg-night d-flex flex-column gap-2">
                <div class="d-flex flex-column gap-2">
                    <label for="username" class="fw-bold">Username<span class="text-danger">*</span></label>
                    <input v-model="username" type="text" name="username" id="username" class="form-control" required>
                </div>
                <div class="d-flex flex-column gap-2">
                    <label for="password" class="fw-bold">Password<span class="text-danger">*</span></label>
                    <div class="position-relative">
                    <input v-model="password" :type="show ? 'text' : 'password'" name="password" id="password" class="form-control" required>
                    <div @click="show = !show" class="text-secondary cursor-pointer eye-icon">
                        <i v-if="show" class="fa-solid fa-eye"></i>
                        <i v-else class="fa-solid fa-eye-slash"></i>
                    </div>
                    </div>
                </div>
                <div class="d-flex flex-row gap-1 align-items-center align-self-end">
                    <button type="submit" class="btn btn-outline-primary">Log In</button>
                    <RouterLink class="btn btn-dark" to="/users/add">Sign Up</RouterLink>
                </div>
            </form>
        </div>
        <div v-else class="d-flex flex-column align-items-center gap-2">
            <div class="text-warning fs-1"><i class="fa-solid fa-triangle-exclamation"></i></div>
            <div class="fs-1 fw-bold">You are Aleardy logged in !!</div>
            <RouterLink class="btn btn-warning fs-4" to="/">Back</RouterLink>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.eye-icon{
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
}
</style>