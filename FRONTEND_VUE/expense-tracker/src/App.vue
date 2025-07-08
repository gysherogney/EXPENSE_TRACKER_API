<template>
  <MainNavbar @open-login="openLogin"  />
  <HeroSection />
  <AboutSection />
  <FeatureSection />
  <LoginPage />
  <FooterSection />
  <loginModal v-if="showLogin" @close="closeLogin"/>
 

</template>

<script setup>
import {ref} from 'vue'
import MainNavbar from './components/MainNavbar.vue';
import HeroSection from './components/HeroSection.vue';
import AboutSection from './components/AboutSection.vue';
import FeatureSection from './components/FeatureSection.vue';
import LoginPage from './components/LoginPage.vue';
import FooterSection from './components/FooterSection.vue';
import loginModal from './components/loginModal.vue';

const showLogin = ref(false);
function openLogin(){
  showLogin.value=true;
}
function closeLogin(){
  showLogin.value=false;
}
</script>
