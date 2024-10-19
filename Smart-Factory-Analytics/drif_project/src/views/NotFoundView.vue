<script setup>
import { RouterLink } from 'vue-router';
</script>
<template>
    <div class="py-4">
        <div class="d-flex flex-column align-items-center">
            <div class="fs-0 text-primary mb-2"><i class="fas fa-exclamation-triangle"></i></div>
            <div class="fs-2 fw-bold text-secondary">Not Found Page</div>
            <RouterLink class="button bg-secondary text-white" to="/">Back</RouterLink>
        </div>
    </div>
</template>
<style lang="scss" scoped>
.fs-0{
    font-size: 4rem;
}
</style>