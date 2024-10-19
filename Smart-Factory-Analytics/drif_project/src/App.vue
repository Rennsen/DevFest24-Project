<script setup>
import { RouterView } from "vue-router";
import SideBar from "./components/SideBar.vue";
import { state } from "./store";
</script>

<template> 
  <div :class="['background',state.isLoggedIn ? 'd-flex flex-row' : '']">
    <div v-if="state.isLoggedIn" class="side-width">
      <SideBar />
    </div>
    <div :class="[ state.isLoggedIn ? 'content-width' : '']">
      <RouterView />
    </div>
  </div>
</template>

<style lang="scss" scoped>
$width-lg: 170px;
.side-width{
  width: $width-lg;
}
.content-width{
  width: calc(100% - $width-lg);
}
.background {
    background: linear-gradient(135deg, #092b65 0%, #133878 25% , #2c43aa 50%, #1b3882 75%, #132e70 100%);
    background-size: cover;
    min-height: 100vh; /* Adjust this as per the full viewport */
    width: 100%;
    color: white;
    position: relative;
}

/* Optional - Add some lighting effect */
.background::before {
    content: '';
    position: absolute;
    top: -50px;
    left: -50px;
    width: 200px;
    height: 200px;
    background: rgba(255, 255, 255, 0.2);
    border-radius: 50%;
    filter: blur(100px);
    z-index: 0;
}
</style>
