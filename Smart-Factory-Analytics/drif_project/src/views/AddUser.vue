<script setup>
import axios from 'axios';
import { reactive , computed } from 'vue';
import { baseUrl , token } from '@/store';
import { useToast } from 'vue-toastification';
import { useRouter , useRoute } from 'vue-router';

const router = useRouter();
const toast = useToast();

const newUser = reactive({
    last_name : '',
    first_name : '',
    phone_number : '',
    email : '',
    address : '',
    gender : '',
    birth_date : '',
    study_level : '',
    is_operator : false,
    is_admin : false,
    is_sick: false,
    is_blocked : false,
});


// Validations
function isNameValid(field) {
    const pattern = /^[A-Za-z\u0600-\u06FF]+(\s[A-Za-z\u0600-\u06FF]+)*$/;
    return pattern.test(field);
}


const firstValid = computed(() => isNameValid(newUser.first_name));
const lastValid = computed(() => isNameValid(newUser.last_name));



const roleValid = computed(() => {
    return newUser.is_admin || newUser.is_operator;
}) 

const genderValid = computed(() => {
    return !!newUser.gender;
})


const isFormValid = computed(() => {
    return firstValid.value && lastValid.value && roleValid.value && genderValid.value;
})
// End Validation

const addUser = async () => {
    if (!isFormValid.value){
        toast.error('املأ الحقول المطلوبة بشكل صحيح');
        return;
    }; 
    try {
        const response = await axios.post(`${baseUrl}/api/user/add-user`,newUser);
        toast.success(` تمّ اضافة المستخدم ${newUser.last_name} ${newUser.first_name}`);
        router.push('/')
    } catch (error) {
        console.error('Error adding user:', error);
        toast.error('فشل في اضافة المستخدم');
    }
};
  
</script>


<template>
    <div class="py-4">
        <div class="myContainer d-flex flex-column">
            <div class="fs-1 text-white fw-bold text-center">Add User</div>
            <form @submit.prevent="addUser" class="d-flex flex-column bg-night rounded-3 p-3 gap-2">
                <div :class="['d-flex','flex-column','gap-3']">
                    <div class="fs-3 fw-bold mb-2 text-secondary">Personal Info</div>
                    <div class="d-flex flex-column gap-2">
                        <label for="first_name" class="fw-bold">First Name<span class="text-danger">*</span></label>
                        <input v-model="newUser.first_name" type="text" name="first_name" id="first_name" :class="['form-control',firstValid ? 'is-valid' : 'is-invalid']" required>
                    </div>

                    <!-- separator -->
                    
                    <div class="d-flex flex-column gap-2">
                        <label for="last_name" class="fw-bold">Family Name<span class="text-danger">*</span></label>
                        <input v-model="newUser.last_name" type="text" name="last_name" id="last_name" :class="['form-control',lastValid ? 'is-valid' : 'is-invalid']" required>
                    </div>

                    <!-- separator -->
                    
                    <div class="d-flex flex-column gap-2">
                        <label for="email" class="fw-bold">Email</label>
                        <input v-model="newUser.email" type="email" name="email" id="email" class="form-control">
                    </div>

                    <!-- separator -->
                    
                    <div class="d-flex flex-column gap-2">
                        <label for="phone_number" class="fw-bold">Phone Number</label>
                        <input v-model="newUser.phone_number" type="text" name="phone_number" id="phone_number" class="form-control">
                    </div>
                    
                    <!-- separator -->

                    <div class="d-flex flex-column gap-2">
                        <label for="address" class="fw-bold">Address</label>
                        <input v-model="newUser.address" type="text" name="address" id="address" class="form-control">
                    </div>

                    <!-- separator -->

                    <div class="d-flex flex-column gap-2">
                        <label for="gender" class="fw-bold">Sex<span class="text-danger">*</span></label>
                        <select v-model="newUser.gender" id="gender" :class="['form-control',genderValid ? 'is-valid' : 'is-invalid']" name="gender"  aria-label="Default select example">
                            <option value="m">Male</option>
                            <option value="f">Female</option>
                        </select>
                    </div>
                    
                    <!-- separator -->

                    <div class="d-flex flex-column gap-2">
                        <label for="birth_date" class="fw-bold">Birth Date</label>
                        <input v-model="newUser.birth_date" type="date" name="birth_date" id="birth_date" class="form-control">
                    </div>

                    <!-- separator -->

                    <div class="d-flex flex-row gap-1">
                        <input v-model="newUser.is_blocked" class="form-check-input" name="is_blocked"  type="checkbox" id="is_blocked">
                        <label class="form-check-label" for="is_blocked">
                            Is He Blocked
                        </label>
                    </div>

                    <!-- separator -->

                    <div class="d-flex flex-column gap-2">
                        <label class="fw-bold">This User Is <span class="text-danger">*</span></label>
                        <div class="d-flex flex-row gap-1">
                            <input v-model="newUser.is_operator" class="form-check-input" name="student"  type="checkbox" id="student">
                            <label class="form-check-label" for="student">
                                Operator
                            </label>
                        </div>
                        <div class="d-flex flex-row gap-1">
                            <input v-model="newUser.is_admin" class="form-check-input" name="admin" type="checkbox" id="admin">
                            <label class="form-check-label" for="admin">
                                Manager
                            </label>
                        </div>
                        <div v-if="!roleValid" class="small text-danger">At Least Choose One</div>
                    </div>

                    <!-- separator -->

                    <div class="d-flex flex-column gap-2">
                        <label for="study_level" class="fw-bold">Education Level</label>
                        <select v-model="newUser.study_level"  id="study_level" class="form-select" name="study_level"  aria-label="Default select example">
                            <option value="0">Not Educated</option>
                            <option value="1">Primary School</option>
                            <option value="2">Middle School</option>
                            <option value="3">High School</option>
                            <option value="4">University</option>
                        </select>
                    </div>
                    <div class="d-flex flex-row gap-1">
                        <input v-model="newUser.is_sick" class="form-check-input" name="is_sick"  type="checkbox" id="is_sick">
                        <label class="form-check-label" for="is_sick">
                            Is He Sick
                        </label>
                    </div>
                    
                </div>
                <button 
                    type="submit"  
                    :class="['btn', 'btn-primary', 'mt-3', 'w-fit', 'align-self-end']"
                >
                    Add
                </button>
            </form>
        </div>
    </div>
</template>