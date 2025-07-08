<template>
    <nav class="flex justify-between items-center px-6 py-4 shadow-md bg-white fixed top-0 w-full z-50">
      <div class="text-2xl font-bold text-orange-500">ExpensePro</div>
      <div class="space-x-6 hidden md:flex">
        <a href="#home" class="hover:text-orange-500">Home</a>
        <a href="#about" class="hover:text-orange-500">About</a>
        <a href="#features" class="hover:text-orange-500">Features</a>
      <button @click="$emit('open-login')" class="bg-orange-600 px-6 rounded-md  text-white hover:text-white font-semibold focus:outline-none">Login</button>
    </div>
   
    </nav>
  </template>

<script setup>

</script>