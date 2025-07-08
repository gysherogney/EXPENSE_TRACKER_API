<template>
    <section id="features" class="py-20 px-6 md:px-20 bg-orange-50">
      <div class="text-center mb-12" data-aos="fade-up">
        <h2 class="text-3xl font-bold text-orange-600">Key Features</h2>
        <p class="text-gray-600 mt-4">Designed to make managing money effortless.</p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div v-for="(feature, index) in features" :key="index" class="bg-white p-6 rounded-xl shadow-lg text-center" :data-aos="'zoom-in'" :data-aos-delay="index * 100">
          <img :src="feature.icon" class="w-16 h-16 mx-auto mb-4" />
          <h4 class="text-xl font-semibold mb-2">{{ feature.title }}</h4>
          <p class="text-gray-600">{{ feature.description }}</p>
        </div>
      </div>
    </section>
  </template>

<script setup>
import budgetIcon from '@/assets/images/Budgeting 101.jpeg';
import realtimeIcon from '@/assets/images/realtime.jpeg';
import cloudIcon from '@/assets/images/cloud1.jpeg';

const features = [
  {
    title: "Budget Alerts",
    description: "Get notified before you overspend.",
    icon: budgetIcon
  },
  {
    title: "Real-time Reports",
    description: "Visualize your spending trends.",
    icon: realtimeIcon
  },
  {
    title: "Cloud Sync",
    description: "Access your data anywhere.",
    icon: cloudIcon
  }
];
</script>

