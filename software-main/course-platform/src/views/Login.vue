<template>
  <div class="login-wrap">
    <div class="ms-login">
      <div class="ms-title">账号登录</div>
      <el-form :model="loginForm" :rules="rules" ref="login" class="ms-content">
        <el-form-item prop="username">
          <el-input v-model="loginForm.username" placeholder="用户名">
          </el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input
            type="password"
            placeholder="密码"
            v-model="loginForm.password"
          >
          </el-input>
        </el-form-item>
        <div class="login-btn">
          <el-button type="primary" @click="handleLogin()">登 录</el-button>
        </div>
      </el-form>
      <div class="sign-link">
        <el-button type="text" @click="jumpSignup()">注册新用户</el-button>
      </div>
    </div>
    <div class="login-pics">
      <div class="login-pics-pict"></div>
      <div class="login-pics-txt">
        <p>到头来，</p>
        <p>我们记住的，</p>
        <p>不是敌人的攻击，</p>
        <p>而是朋友的沉默。</p>
        <p>——马丁·路德·金</p>
      </div>
    </div>
  </div>
</template>


<script>
import { login } from "@/api/api";
import { ElMessage } from "element-plus";
export default {
  name: "Login",
  data() {
    return {
      userType: "",
      loginForm: {
        username: "",
        password: "",
      },
      rules: {
        username: [
          { required: true, message: "请输入用户名", trigger: "blur" },
        ],
        password: [{ required: true, message: "请输入密码", trigger: "blur" }],
      },
    };
  },
  methods: {
    handleLogin() {
      login(this.loginForm).then((res) => {
        console.log(res);
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
    jumpSignup() {
      this.$router.push("/signup");
    },
  },
};
</script>

<style scoped>
.login-wrap {
  width: 960px;
  margin: 150px auto 32px auto;
  padding: 0 24px;
  min-height: 500px;
}

.login-pics {
  position: relative;
  margin-right: 395px;
}

.login-pics-txt {
  padding-top: 25px;
  position: relative;
  font-weight: normal;
  line-height: 30px;
  padding: 100px;
}
.login-pics-pict {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  height: 400px;
  background-repeat: no-repeat;
  background-position: right 40px;
  background-image: url("../assets/img/tg-smile.jpg");
}
.ms-title {
  width: 100%;
  line-height: 50px;
  text-align: center;
  font-size: 20px;
  color: #333;
  background: #f9fbfe;
  border-bottom: 1px solid #a0b1c4;
}
.ms-login {
  float: right;
  width: 350px;
  border-radius: 5px;
  height: 390px;
  background: rgba(255, 255, 255, 0.3);
  border: 1px solid #a0b1c4;
  overflow: hidden;
  z-index: 12;
}
.ms-content {
  padding: 40px 30px 80px 30px;
}
.login-btn {
  text-align: center;
}
.login-btn button {
  width: 100%;
  height: 36px;
  margin-bottom: 10px;
  font-size: 18px;
}
.el-link.el-link--primary {
  --el-link-text-color: var(--el-color-primary);
  color: var(--el-color-primary);
}

.sign-link {
  text-align: right;
  margin-bottom: 15px;
  padding-right: 20px;
}
</style>