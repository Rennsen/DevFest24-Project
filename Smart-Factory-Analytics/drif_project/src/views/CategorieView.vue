<script setup>
import { ref } from 'vue';
import { useRoute } from 'vue-router';
import { RouterLink } from 'vue-router';
const route = useRoute();
const ctg = ref(route.params.ctg);
const machines = ref([
    {
        machine_id : 100,
        last_updated : "20-4-2005"
    },
    {
        machine_id : 101,
        last_updated : "20-4-2005"
    },
])
</script>
<template>
    <div class="py-4">
        <div class="myContainer d-flex flex-column text-white">
            <div class="fs-1 fw-bold mb-3">
                {{ 
                    ctg == 'avg' 
                    ? "AVG's"
                    : ctg == 'pm'
                    ? "Painting Machines"
                    : ctg == 'wr' 
                    ? "Welding Robots"
                    : ctg == 'ltm' 
                    ? "Leak Test Machine"
                    : ctg == 'cnc' 
                    ? "CNC Machines"
                    : 'Stamping Press'
                }}
            </div>
            <div class="grid gap-2">
                <div class="col-12 md-col-8 lg-col-8">
                    <div class="bg-night rounded-3 p-3 d-flex flex-column gap-2">
                        <div v-if="!machines.length" class="text-danger fw-bold text-center">
                            There is No Machines Yet
                        </div>
                        <div v-else class="d-flex flex-column gap-2">
                            <div class="d-flex flex-row align-items-center justify-content-between">
                                <div class="fw-bold fs-4">Machine Id</div>
                                <div class="fw-bold fs-4">Last Updated</div>
                            </div>
                            <!-- separator -->
                            <div v-for="machine in machines" :key="machine.machine_id" class="d-flex flex-column">
                                <div class="d-flex flex-row align-items-center justify-content-between">
                                    <RouterLink class="fw-bold fs-4" :to="`/categories/${ctg}/${machine.machine_id}`">{{ machine.machine_id }}</RouterLink>
                                    <div class="fw-bold fs-4">{{ machine.last_updated }}</div>
                                </div>
                                <hr style="height: 0.5px;">
                            </div>
                        </div>
                        <RouterLink class="align-self-center button-blue bg-secondary text-uppercase" :to="`/categories/${ctg}/add`">add a machine</RouterLink>
                    </div>
                </div>
                <div class="col-12 md-col-4 lg-col-4">
                    <div class="rounded-3 bg-night p-3 d-flex flex-column gap-2">
                        <div class="fs-4 fw-bold">Category Description</div>
                        <div class="lh-18">Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellendus ad sapiente dolorum sed architecto quas beatae blanditiis deserunt iure, est quam magnam illum accusantium totam tempora, veritatis enim illo corporis!</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<style lang="scss" scoped>
.lh-18{
    line-height: 1.8;
}
</style>