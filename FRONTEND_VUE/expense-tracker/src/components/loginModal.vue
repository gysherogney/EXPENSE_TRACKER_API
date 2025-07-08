<template>
    <div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50" @click.self="close">
      <div
        class="bg-white rounded-lg shadow-xl w-full max-w-md p-8"
        data-aos="zoom-in"
      >
        <h2 class="text-2xl font-bold mb-6 text-orange-600 text-center">Login</h2>
  
        <form @submit.prevent="submitLogin" class="space-y-5">
          <div>
            <label class="block text-gray-700 mb-1" for="email">Email</label>
            <input
              v-model="email"
              id="email"
              type="email"
              required
              class="w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-orange-500"
              placeholder="you@example.com"
            />
          </div>
  
          <div>
            <label class="block text-gray-700 mb-1" for="password">Password</label>
            <input
              v-model="password"
              id="password"
              type="password"
              required
              class="w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-orange-500"
              placeholder="********"
            />
          </div>
  
          <button
            type="submit"
            class="w-full bg-orange-500 hover:bg-orange-600 text-white font-semibold py-3 rounded-lg transition"
          >
            Login
          </button>
        </form>
  
        <button
          @click="close"
          class="absolute top-4 right-4 text-gray-400 hover:text-gray-600"
          aria-label="Close"
        >
          ✕
        </button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref,defineEmits } from "vue";
  
  const email = ref("");
  const password = ref("");
  
  const emit = defineEmits(["close", "login"]);
  
  function close() {
    emit("close");
  }
  
  function submitLogin() {
    alert(`Logging in as: ${email.value}`);
    close();
  }
  </script>
  