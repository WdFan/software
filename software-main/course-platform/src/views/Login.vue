<template>
  <div id="login">
    <h1>Login</h1>
    <el-form :model="loginForm" ref="loginForm">
      <h2>登录</h2>
      <el-form-item prop="username">
        <el-input
          v-model="loginForm.username"
          name="username"
          placeholder="请输入用户名"
        ></el-input>
      </el-form-item>

      <el-form-item>
        <el-input
          v-model="loginForm.password"
          name="password"
          placeholder="请输入密码"
          show-password
        ></el-input>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="handleLogin">登录</el-button>
      </el-form-item>
    </el-form>

    <el-button type="primary" @click="jumpSignup">注册</el-button>
  </div>
</template>


<script>
import {getUser, login} from "../api/api";
export default {
  name: "Login",
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
      const {username, password} = this.loginForm;
      console.log(username);
      getUser().then(res => {
        console.log(res)
      })
      login(username, password).then((res) => {
        console.log(res);
      })
    },
    jumpSignup() {
      this.$router.push('/signup');
    }
  },
};
</script>

<style scoped>
.el-input {
  width: 300px;
}
</style>