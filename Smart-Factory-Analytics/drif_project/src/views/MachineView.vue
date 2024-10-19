<script setup>
import { ref } from 'vue';
import { useRoute } from 'vue-router';
const route = useRoute();
const ctg = ref(route.params.ctg);
const id = ref(route.params.id);
</script>
<template>
    <div class="myContainer mt-4 text-white d-flex flex-column">
        <div class="d-flex flex-row justify-content-between mb-3">
            <div class="fs-1 fw-bold">
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
            <div class="fs-1 fw-bold">Machine Id : {{ id }}</div>
        </div>
        <div class="bg-night rounded-3 p-3 d-flex flex-column">
            <div class="fs-4 d-flex flex-row align-items-center gap-1 mb-2">
                <div class="fw-bold flex-grow-1">Sensor Data</div>
                <div class="fw-bold">Status</div>
                <div>|</div>
                <div class="fw-bold">Unit</div>
            </div>

            <div class="d-flex flex-column mb-2">
                <div class="d-flex flex-column">
                    <div class="d-flex flex-row align-items-center gap-1 fw-bold">
                        <div class="flex-grow-1">Spindle Speed</div>
                        <div>12000</div>
                        <div>RPM</div>
                    </div> 
                    <hr style="height: 0.5px;">
                </div>
                <div class="d-flex flex-column">
                    <div class="d-flex flex-row align-items-center gap-1 fw-bold">
                        <div class="flex-grow-1">Tool Wear Level</div>
                        <div>35</div>
                        <div>%</div>
                    </div> 
                    <hr style="height: 0.5px;">
                </div>
                <div class="d-flex flex-column">
                    <div class="d-flex flex-row align-items-center gap-1 fw-bold">
                        <div class="flex-grow-1">Cut Depth</div>
                        <div>5</div>
                        <div>mm</div>
                    </div> 
                    <hr style="height: 0.5px;">
                </div>
            </div>

            <div class="text-success fw-bold text-center">Time stamp bull shit</div>
        </div>
    </div>
</template>