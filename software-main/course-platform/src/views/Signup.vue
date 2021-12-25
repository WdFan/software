<template>
  <div class="signup_page">
    <el-container>
      <el-header>
        <el-button class="logo" @click="this.$router.go(0)">
          <el-image
            :src="require('@/assets/img/logo.png')"
            style="width: 20px; height: 20px"
            alt="logo"
          >
          </el-image>
        </el-button>
      </el-header>
      <el-main>
        <div class="main">
          <el-form :model="signupForm" ref="signupForm">
            <div class="welcome">欢迎注册</div>
            <el-form-item>
              <el-input
                v-model="signupForm.username"
                placeholder="用户名"
                clearable
              ></el-input>
            </el-form-item>

            <el-form-item>
              <el-input
                v-model="signupForm.password"
                type="password"
                placeholder="密码"
              ></el-input>
            </el-form-item>

            <el-form-item>
              <el-input
                v-model="signupForm.repassword"
                type="password"
                placeholder="确认密码"
              ></el-input>
            </el-form-item>

            <el-form-item>
              <el-button
                class="signup_button"
                type="primary"
                @click="handleSignup"
                >立即注册</el-button
              >
            </el-form-item>
          </el-form>
        </div>
      </el-main>
    </el-container>
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
      },
    };
  },
  methods: {
    handleSignup() {
      signup(this.signupForm).then((res) => {
        if (res.data.code == 200) {
          const user_info = res.data.user_info;
          localStorage.setItem("is_login", true);
          localStorage.setItem("user_info", JSON.stringify(user_info));
          ElMessage.success(res.data.msg);
          this.$router.push("/home");
        } else {
          ElMessage.error(res.data.msg);
        }
      });
    },
  },
};
</script>

<style scoped>
.signup_page,
.el-container {
  height: 100%;
}

.logo {
  text-align: center;
  color: #fff;
  font-size: 28px;
  background: #249ce1;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 40px;
  width: 40px;
  border-radius: 50%;
  margin-top: 10px;
  margin-left: 40px;
}

.el-header {
  height: 60px;
  background: #eff4fa;
  border-bottom: 1px solid #d6dfea;
}

.main {
  top: 50%;
  margin-top: -373.5px;
  position: absolute;
  padding-bottom: 10px;
  width: 100%;
}

.main > .el-form {
  position: relative;
  margin: 0 auto;
  width: 480px;
  font-size: 44px;
  margin-bottom: 20px;
}

.welcome {
  font-size: 44px;
  margin-bottom: 84px;
}

.el-input {
  height: 60px;
}

>>> .el-input__inner {
  font-size: 20px;
  height: 52px;
}

.signup_button {
  width: 100%;
  height: 60px;
  font-size: 24px;
  font-weight: lighter;
}
</style>