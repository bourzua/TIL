<template>
  <div class="clearAllContainer">
    <span class="clearAllBtn" v-on:click="clearTodo">Clear All</span>
  </div>
</template>

<script>
export default {
  methods: {
    clearTodo: function() {
      this.$emit("clearAll");
    }
  }

}
</script>

<style scoped>
.clearAllContainer {
  width: 8.5rem;
  height: 50px;
  line-height: 50px;
  background-color: white;
  border-radius: 5px;
  /* 위 아래에는 값을 주지 않는다 */
  /* 좌우는 균등하게 값을 주어 중앙에 둠 */
  margin: 0 auto;
}

.clearAllBtn {
  color: #e20303;
  display: block;
}

</style>