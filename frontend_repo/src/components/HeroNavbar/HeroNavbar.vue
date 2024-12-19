<template>
  <nav
    class="dark:bg-gray-800 shadow-lg dark:shadow-gray-900 z-20 align-middle items-center py-4"
  >
    <div class="flex justify-center gap-4">
      <div
        class="text-gray-800 dark:text-white hover:text-blue-600 dark:hover:text-blue-400 cursor-pointer"
      >
        Overview
      </div>
      <div
        class="text-gray-800 dark:text-white hover:text-blue-600 dark:hover:text-blue-400 cursor-pointer"
      >
        Media
      </div>
      <div
        class="text-gray-800 dark:text-white hover:text-blue-600 dark:hover:text-blue-400 cursor-pointer"
      >
        Fandom
      </div>
      <div
        class="text-gray-800 dark:text-white hover:text-blue-600 dark:hover:text-blue-400 cursor-pointer"
      >
        Share
      </div>
    </div>
  </nav>
</template>

<script>
import { ref } from "vue";
import { LOGO_URL, SEARCH_URL } from "@/Constants";

export default {
  name: "HeroNavbar",
  setup() {
    const isMobileMenuOpen = ref(false);

    const toggleMobileMenu = () => {
      isMobileMenuOpen.value = !isMobileMenuOpen.value;
    };

    return {
      isMobileMenuOpen,
      toggleMobileMenu,
      LOGO_URL,
      SEARCH_URL,
    };
  },
};
</script>
