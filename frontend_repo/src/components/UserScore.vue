<template>
  <div class="circle-container">
    <svg width="120" height="120" viewBox="0 0 120 120">
      <circle
        class="circle-background"
        cx="60"
        cy="60"
        r="40"
        stroke-width="10"
        fill="none"
      />
      <circle
        class="circle-progress"
        cx="60"
        cy="60"
        r="40"
        stroke-width="10"
        fill="none"
        :stroke-dasharray="circumference"
        :stroke-dashoffset="offset"
        stroke-linecap="round"
      />

      <text x="50%" y="50%" text-anchor="middle" dy=".3em">{{ value }}%</text>
    </svg>
  </div>
</template>

<script>
export default {
  props: {
    value: {
      type: Number,
      required: true,
    },
  },
  computed: {
    circumference() {
      return 2 * Math.PI * 40;
    },
    offset() {
      return this.circumference - (this.value / 100) * this.circumference;
    },
  },
};
</script>

<style scoped>
.circle-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.circle-background {
  stroke: #e6e6e6;
}

.circle-progress {
  stroke: #4caf50;
  transition: stroke-dashoffset 0.5s ease;
  transform: rotate(-90deg);
  transform-origin: 50% 50%;
}

text {
  font-size: 20px;
  fill: white;
}
</style>
