<template>
  <div class="home">
    <h1>home</h1>
    <el-button type="primary" @click="jumpLogin">登录</el-button>
    <el-button type="primary" @click="logout">注销</el-button>
  </div>
  <router-view></router-view>
</template>

<script>
import { ElMessage } from "element-plus";

export default {
  name: "home",
  data() {
    return {};
  },
  methods: {
    jumpLogin() {
      this.$router.push("/login");
    },
    logout() {
      localStorage.clear();
      ElMessage.success("注销成功！");
      this.$router.push("/login");
    },
  },
};
</script>