<template>
  <div id="signup">
    <el-form :model="signupForm" ref="signupForm">
      <h2>注册</h2>
      <el-form-item label="用户名">
        <el-input
          v-model="signupForm.username"
          placeholder="请输入用户名"
        ></el-input>
      </el-form-item>

      <el-form-item label="密码">
        <el-input
          v-model="signupForm.password"
          placeholder="请输入密码"
          show-password
        ></el-input>
      </el-form-item>

      <el-form-item label="确认密码">
        <el-input
          v-model="signupForm.repassword"
          placeholder="再次输入密码"
          show-password
        ></el-input>
      </el-form-item>

      <el-form-item label="用户类型">
        <el-radio-group v-model="signupForm.user_type">
          <el-radio label="student">学生</el-radio>
          <el-radio label="teacher">教师</el-radio>
        </el-radio-group>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="handleSignup">注册</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>


<script>
import { signup } from "@/api/api";
import { ElMessage } from "element-plus";
export default {
  name: "Signup",
  data() {
    return {
      userType: "",
      signupForm: {
        username: "",
        password: "",
        repassword: "",
        user_type: "",
      },
    };
  },
  methods: {
    handleSignup() {
      signup(this.signupForm).then(res => {
        if (res.data.code == 200) {
          const user_info = res.data.user_info;
          sessionStorage.setItem("is_login", true);
          sessionStorage.setItem("user_info", JSON.stringify(user_info));
          ElMessage.success(res.data.msg);
          this.$router.push('/home')
        } else {
          ElMessage.error(res.data.msg)
        }
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