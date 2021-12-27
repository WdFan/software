<template>
  <div class="signup_page">
    <el-container>
      <el-header>
        <el-button class="logo" @click="this.$router.push('/login')">
          <el-image
            :src="require('@/assets/img/logo.png')"
            style="width: 25px; height: 25px"
            alt="logo"
          >
          </el-image>
        </el-button>
      </el-header>
      <el-main>
        <el-scrollbar style="width: 100%">
          <div class="main">
            <el-form :model="signupForm" ref="signupForm">
              <div class="welcome">欢迎注册</div>
              <div class="header">每一天，乐在沟通。</div>
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
        </el-scrollbar>
      </el-main>
    </el-container>
  </div>
</template>


<script>
import api from "@/api/api";
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
      api.signup(this.signupForm).then((res) => {
        if (res.data.code == 200) {
          const user_info = res.data.user_info;
          this.$store.commit('updateUser', user_info)
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
  font-size: 40px;
  background: #249ce1;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 50px;
  width: 50px;
  border-radius: 50%;
  margin-top: 5px;
  margin-left: 20px;
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

.header {
  font-size: 28px;
  margin-bottom: 64px;
  line-height: 1.2;
  color: #333;
}

.welcome {
  font-size: 44px;
  margin-bottom: 20px;
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

>>> .el-input__suffix {
  font-size: 30px;
}
</style>