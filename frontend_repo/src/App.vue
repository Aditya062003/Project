<script>
import AppNavbar from "./components/AppNavbar/AppNavbar.vue";
import HeroNavabar from "./components/HeroNavbar/HeroNavbar.vue";
import HeroSection from "./components/Main/HeroSection.vue";

export default {
  name: "App",
  components: {
    AppNavbar,
    HeroNavabar,
    HeroSection,
  },
};
</script>

<template>
  <div id="app">
    <AppNavbar />
    <HeroNavabar />
    <HeroSection />
    <router-view />
  </div>
</template>
