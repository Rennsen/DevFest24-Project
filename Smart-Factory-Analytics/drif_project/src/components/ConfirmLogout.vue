<template>
    <div>
      <p class="fw-bold">هل أنت متأكد أنك تريد تسجيل الخروج ?</p>
      <div class="d-flex flex-row gap-1">
        <button @click="onConfirm" class="btn btn-danger">نعم</button>
        <button @click="onCancel" class="btn btn-primary">لا</button>
      </div>
    </div>
  </template>
  
  <script setup>
  const emit = defineEmits(['confirm', 'cancel']); // Emit events to parent component
  
  const onConfirm = () => {
    emit('confirm'); // Emit the confirm event to the parent
  };
  
  const onCancel = () => {
    emit('cancel'); // Emit the cancel event to the parent
  };
  </script>
  