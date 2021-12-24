<template>
  <div class="home">
    <h1>home</h1>
    <el-button type="primary" @click="jumpLogin">Login</el-button>
  </div>
  <router-view></router-view>
</template>

<script>
export default {
  name: "home",
  data() {
    return {};
  },
  methods: {
    jumpLogin() {
      this.$router.push("/Login");
    },
  },
};
</script>