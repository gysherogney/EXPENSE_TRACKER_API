<template>
  <section id="home" class="pt-28 pb-20 px-6 md:px-20 bg-gradient-to-br from-orange-100 via-white to-orange-50">
    <div class="flex flex-col-reverse md:flex-row items-center justify-between">
      <div data-aos="fade-right" class="max-w-xl flex flex-col space-y-6">
        <h1 class="text-4xl md:text-5xl font-bold text-orange-600 leading-tight">
          Smart & Simple Expense Tracker
        </h1>
        <p class="text-gray-700 text-lg ">
          Track your expenses, set budgets, and gain financial control with our intuitive platform.
        </p>
        <a href="#login" class="bg-orange-500 text-white px-6 py-3 rounded-lg shadow hover:bg-orange-600 transition w-40">
  Get Started
</a>

      </div>

      <img data-aos="fade-left" :src="expenseImg" alt="Expense Tracker Illustration"
        class="rounded-lg shadow-lg w-full md:w-[820px] max-h-[540px] object-contain" />
    </div>
  </section>
</template>
<script setup>
import expenseImg from '@/assets/images/expense3.jpeg';

</script>