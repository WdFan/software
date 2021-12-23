<template>
  <div id="login">
    <el-form :model="loginForm" ref="loginForm">
      <h2>登录</h2>
      <el-form-item prop="username">
        <el-input
          v-model="loginForm.username"
          name="username"
          placeholder="请输入用户名/手机号"
          auto-complete="on"
        ></el-input>
      </el-form-item>

      <el-form-item>
        <el-input
          v-model="loginForm.password"
          name="password"
          placeholder="请输入密码"
          auto-complete="on"
          prop="password"
        ></el-input>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="handleLogin">登录</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>


<script>
import { getUser } from "../api/api";
export default {
  name: "Home",
  data() {
    return {
      userType: "",
      loginForm: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    handleLogin() {
      getUser().then((res) => {
        console.log(res.data);
        this.loginForm.username = res.data[0].userName;
        this.loginForm.password = res.data[0].passWord;
      });
    },
  },
};
</script>

<style scoped>
.el-input {
  width: 300px;
}
</style>