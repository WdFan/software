<template>
  <div class="teacherLog">
    <el-container>
      <el-header>
        <h1 v-if="classInfo">
          {{ classInfo.course.name }}-{{ classInfo.name }}:{{ classInfo.code }}
        </h1>
        <el-image
          class="background"
          :src="require('@/assets/img/headercard-background.jpg')"
          alt="background"
        ></el-image>
        <div class="userInfo" v-if="classInfo">
          <span
            ><el-icon :size="14" color="#333"><user-filled /></el-icon
            ><span>{{ classInfo.num }}</span></span
          >
          <span
            ><el-icon :size="14" color="#333"><calendar /></el-icon
            ><span>{{ classInfo.year }}年{{ classInfo.season }}学期</span></span
          >
        </div>
      </el-header>

      <el-main>
        <el-tabs class="mainTab" v-model="activePane">
          <el-tab-pane label="教学日志" name="pane-log">日志</el-tab-pane>
          <el-tab-pane label="成员管理" name="pane-manage">成员</el-tab-pane>
        </el-tabs>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import api from "../../../api/api";

export default {
  name: "teacherLog",
  props: ["id"],
  data() {
    return {
      classInfo: null,
      activePane: null,
      messageInfo: null,
      studentList: null,
    };
  },
  watch: {
    activePane(newPane) {
      if (newPane == "pane-log" && this.messageInfo === null) {
        api.getClassMessage(this.id).then((res) => {
          if (res.data.code == 200) {
            this.messageInfo = res.data.data;
            console.log(this.messageInfo)
            console.log(this.messageInfo.length)
          }
        });
      } else if (newPane == "pane-manage" && this.studentList === null) {
        api.getClassStudentInfo(this.id).then((res) => {
          this.studentList = res.data.studentList;
          console.log(this.studentList)
        });
      }
    },
  },
  created() {
    api.getClassInfo(this.id).then((res) => {
      if (res.data.code == 200) {
        this.classInfo = res.data.data;
        console.warn(this.classInfo);
      }
    });
  },
  mounted() {
    this.activePane = "pane-log";
  },
};
</script>

<style scoped>
.teacherLog {
  height: 100%;
}

.teacherLog .el-header {
  height: 100px;
  text-align: left;
  padding: 20px 20px 0 20px;
  background-color: #fff;
  position: relative;
}

.teacherLog .el-header h1 {
  color: #333;
  font-size: 20px;
  font-weight: 600;
  width: 580px;
  position: relative;
  cursor: pointer;
  height: 40px;
}

.teacherLog .el-header .background {
  position: absolute;
  top: 48px;
  right: 20px;
  z-index: 20;
}

.teacherLog .el-header .userInfo {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: start;
  -ms-flex-pack: start;
  justify-content: flex-start;
  margin-top: 5px;
}

.teacherLog .el-header .userInfo > span {
  font-size: 16px;
  color: #333;
  font-weight: 500;
}

.teacherLog .el-header .userInfo > span:first-child {
  margin-right: 40px;
}

.teacherLog .el-tabs.mainTab {
  height: 100%;
}
</style>