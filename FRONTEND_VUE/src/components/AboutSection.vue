<template>
    <section id="about" class="py-20 px-6 md:px-20 bg-white" >
      <div class="text-center mb-10" data-aos="fade-up">
        <h2 class="text-3xl font-bold text-orange-600">About ExpensePro</h2>
        <p class="text-gray-600 max-w-xl mx-auto mt-4">
          ExpensePro is your smart personal finance companion...
        </p>
      </div>
      <div class="flex flex-col md:flex-row gap-10 items-center">
        <div class="flex-1 flex items-center justify-center" data-aos="fade-right">
          <img :src="expenseImg" class="rounded-lg shadow-lg w-full md:w-[620px] max-h-[540px]" alt="About Illustration" />
        </div>
        <div class="flex-1 space-y-6" data-aos="fade-left">
          <h3 class="text-xl font-semibold text-orange-600">Why ExpensePro?</h3>
          <p class="text-gray-700">
            Managing money shouldn't be hard...
          </p>
          <ul class="list-disc list-inside text-gray-700 space-y-2">
            <li>Track daily, weekly, and monthly expenses</li>
            <li>Set personalized spending limits</li>
            <li>Get real-time alerts</li>
            <li>Access beautiful financial reports</li>
            <li>Offline + cloud sync</li>
          </ul>
          <div class="mt-6">
            <h4 class="text-lg font-semibold text-orange-500">Our Mission</h4>
            <p class="text-gray-600 mt-2">
              To empower individuals...
            </p>
            <h4 class="text-lg font-semibold text-orange-500 mt-4">Our Vision</h4>
            <p class="text-gray-600 mt-2">
              A world where everyone...
            </p>
          </div>
        </div>
      </div>
    </section>
  </template>
    <script setup>
    import expenseImg from '@/assets/images/expense3.jpeg';

    </script>
  