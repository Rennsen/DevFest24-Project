<script setup>
import { ref } from 'vue';
const base = "src/assets/imgs";
const content = ref([
    {
        src: `${base}/home_1.jpg`,
        info:"AVG's",
        to:'/categories/avg',
    },
    {
        src: `${base}/home_2.jpg`,
        info:"Painting Machines",
        to:'/categories/pm',
    },
    {
        src: `${base}/home_3.jpg`,
        info:"Welding Robots",
        to:'/categories/wr',
    },
    {
        src: `${base}/home_4.jpg`,
        info:"Leak Test Machine",
        to:'/categories/ltm',
    },
    {
        src: `${base}/home_5.jpg`,
        info:"CNC Machines",
        to:'/categories/cnc',
    },
    {
        src: `${base}/home_6.jpg`,
        info:"Stamping Press",
        to:'/categories/sp',
    },
])
</script>
<template>
    <div class="py-4">
        <div class="container d-flex flex-column">
            <div class="d-flex flex-column flex-md-row align-items-center mb-2">
                <div class="d-flex flex-column gap-1 flex-grow-1">
                    <div class="small">
                        <span class="text-muted">Pages/</span>
                        <span class="text-capitalize">Dashboard</span>
                    </div>
                    <div class="fw-bold">Dashboard</div>
                </div>

                <div class="d-flex flex-row gap-2 align-items-center small">
                    <div class="w-fit bg-dark rounded-pill border border-light d-flex align-items-center flex-row gap-2 text-white-50 ps-2">
                        <div><i class="fas fa-search"></i></div>
                        <input type="text" id="search" class="text-white py-2 bg-transparent outline-none border-none" placeholder="Type here..">
                    </div>

                    <RouterLink class="d-flex flex-row gap-1 align-items-center text-white-50 mx-1" to="/sign-in">
                        <div><i class="fa-solid fa-user"></i></div>
                        <div>Sign In</div>
                    </RouterLink>

                    <div class="text-white-50 cursor-pointer"><i class="fa-solid fa-gear"></i></div>

                    <div class="text-white-50 cursor-pointer"><i class="fa-solid fa-bell"></i></div>

                </div>


            </div>


            <div class="myContainer p-2 p-lg-3 bg-night d-flex flex-column gap-3 rounded-3">
                <div class="fs-1 fw-bold text-white">Categories</div>
                <div class="grid gap-3">
                    <div v-for="ele in content" :key="ele.src" class="col-12 md-col-6 lg-col-4">
                        <div class="myCard bg-night rounded-3 py-2 d-flex flex-column align-items-center gap-2">
                            <div class="w-75 flex-center"><img :src="ele.src" alt="" class="img-fluid rounded-img img-height"></div>
                            <div class="fs-5 fw-bold text-capitalize">{{ ele.info }}</div>
                            <RouterLink class="button-blue rounded-pill small" :to="ele.to">View All</RouterLink>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<style lang="scss" scoped>
@import "@/assets/_tools";
.small{
    font-size: 0.775rem;
}
.rounded-img{
    border-radius: 5rem;
}
.img-height{
    height: 100px;
}
.myCard{
    transition: 1s all ease;
    &:hover{
        background-color: $hard-night;
    }
}
</style>