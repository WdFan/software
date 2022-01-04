<template>
  <div class="personal">
    <el-container>
      <el-header>
        <span class="title">
          <el-icon :size="24" color="var(--el-color-primary)"
            ><user-filled
          /></el-icon>
          <span> 个人中心</span>
        </span>
      </el-header>
      <el-main class="personal_main">
        <el-tabs tab-position="left" type="border-card">
          <el-tab-pane label="个人信息">
            <div class="panle person-info">
              <h1>个人信息</h1>
              <el-form>
                <el-form-item label="用户">
                  <el-input v-model="personInfoForm.username"></el-input>
                </el-form-item>
                <el-form-item label="姓名">
                  <el-input v-model="personInfoForm.stu_name"></el-input>
                </el-form-item>
                <el-form-item label="学校">
                  <el-input v-model="personInfoForm.stu_school"></el-input>
                </el-form-item>
                <el-form-item label="学号">
                  <el-input v-model="personInfoForm.stu_id"></el-input>
                </el-form-item>
                <el-form-item>
                  <el-button
                    class="btn active"
                    type="primary"
                    @click="savePersonInfo"
                    >保存</el-button
                  >
                </el-form-item>
              </el-form>
            </div>
          </el-tab-pane>
          <el-tab-pane label="人脸识别">
            <div class="panle">
              <h1>人脸识别</h1>
            </div>
          </el-tab-pane>
        </el-tabs>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import { ElMessage } from "element-plus";
import api from "../../api/api";

export default {
  name: "personal",
  data() {
    return {
      personInfoForm: this.$store.state.user_info,
    };
  },
  methods: {
    savePersonInfo() {
      api.savePersonInfo(this.personInfoForm).then((res) => {
        if (res.data.code == 200) {
          this.$store.commit('updateUser', res.data.data);
          ElMessage.success("本次修改已保存");
        } else {
          ElMessage.error("修改失败");
        }
      });
    },
  },
};
</script>

<style scoped>
.personal header {
  height: 50px;
  line-height: 50px;
  padding: 0 20px;
  background-color: #ffffff;
  -webkit-box-shadow: 0 1px 4px 0 rgba(0, 0, 0, 0.1);
  box-shadow: 0 1px 4px 0 rgba(0, 0, 0, 0.1);
  position: relative;
  z-index: 10;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
}
.personal .title {
  width: 300px;
  text-align: left;
  color: #333333;
  font-size: 18px;
  display: inline-block;
  vertical-align: middle;
}

.personal .title > i {
  vertical-align: middle;
}

.personal .personal_main {
  padding: 0;
}

.person-info {
  font-size: 14px;
  min-height: auto;
}

.panle {
  background: #fff;
  min-width: 980px;
  border-radius: 5px;
}

.panle h1 {
  font-size: 16px;
  color: #333333;
  text-align: left;
  padding-left: 26px;
  padding-top: 14px;
  padding-bottom: 12px;
  border-bottom: 1px solid #ddd;
  line-height: 22px;
}

.panle.person-info .el-form {
  padding-top: 40px;
  margin: 0 auto;
  width: 600px;
}

.panle.person-info .el-form > .el-form-item {
  margin-bottom: 30px;
}

.person-info .btn {
  font-weight: bold;
  color: #9b9b9b;
  background: #ddd;
  border-radius: 34px;
  width: 180px;
  height: 34px;
  margin: 0px auto;
  margin-top: 30px;
  cursor: pointer;
}

.person-info .btn.active {
  background: #5096f5;
  color: #fff;
}
</style>