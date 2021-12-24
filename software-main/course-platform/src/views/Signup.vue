<template>
  <div id="signup">
    <h1>Sign up</h1>
    <el-form :model="signupForm" ref="signupForm">
      <h2>注册</h2>
      <el-form-item prop="username">
        <el-input
          v-model="signupForm.username"
          name="username"
          placeholder="请输入用户名"
        ></el-input>
      </el-form-item>

      <el-form-item>
        <el-input
          v-model="signupForm.password"
          name="password"
          placeholder="请输入密码"
          show-password
        ></el-input>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="handleSignup">注册</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>


<script>
import { getUser, login } from "../api/api";
export default {
  name: "Signup",
  data() {
    return {
      userType: "",
      signupForm: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    handleSignup() {
      getUser().then((res) => {
        console.log(res.data);
        this.signupForm.username = res.data[0].userName;
        this.signupForm.password = res.data[0].passWord;
      });

      login("zzzzzzzzz", "zzzzz").then((res) => {
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