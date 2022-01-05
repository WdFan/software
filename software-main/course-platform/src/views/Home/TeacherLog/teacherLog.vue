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
          <el-tab-pane label="教学日志" name="pane-log" class="log">
            <div class="radioTab">
              <div class="buttonGroup" @click="addMessage">
                <span
                  ><el-icon><promotion /></el-icon>发布任务</span
                >
              </div>
            </div>
            <PaneLog v-if="messageInfo" :messageList="messageInfo"></PaneLog>
          </el-tab-pane>
          <el-tab-pane label="成员管理" name="pane-manage">
            <PaneManage v-if="studentList" :userList="studentList"></PaneManage>
          </el-tab-pane>
          <el-tab-pane label="签到信息" name="pane-sign">
            <PaneSign v-if="signInfo" :signList="signInfo"></PaneSign>
          </el-tab-pane>
        </el-tabs>
      </el-main>
    </el-container>

    <el-dialog
      v-model="addMessageDialog"
      title="发布任务"
      center
      @closed="closeMessageDialog"
    >
      <el-input v-model="messageForm.title" label="标题"></el-input>
      <VueVditor v-model="messageForm.msg" class="editor"></VueVditor>
      <el-button type="primary" @click="clickSubmit">提交</el-button>
    </el-dialog>
  </div>
</template>

<script>
import { ElMessage } from "element-plus";
import api from "../../../api/api";
import PaneLog from "../../../component/paneLog.vue";
import PaneManage from "./paneManage.vue";
import PaneSign from "./paneSign.vue";

export default {
  name: "teacherLog",
  props: ["id"],
  data() {
    return {
      classInfo: null,
      activePane: null,
      messageInfo: null,
      studentList: null,
      signInfo: null,
      addMessageDialog: false,
      messageForm: {
        title: "",
        msg: "",
        createTime: null,
      },
    };
  },
  watch: {
    activePane(newPane) {
      if (newPane == "pane-log" && this.messageInfo === null) {
        api.getClassMessage(this.id).then((res) => {
          if (res.data.code == 200) {
            this.messageInfo = res.data.data.sort((l, r) => {
              return r.createTime - l.createTime;
            });
          }
        });
      } else if (newPane == "pane-manage" && this.studentList === null) {
        api.getClassStudentInfo(this.id).then((res) => {
          this.studentList = res.data.studentList;
        });
      } else if (newPane == "pane-sign" && this.signInfo === null) {
        api.getDbInfo().then((res) => {
          if (res.data.code == 200) {
            this.signInfo = res.data.data;
          }
        });
      }
    },
  },
  created() {
    api.getClassInfo(this.id).then((res) => {
      if (res.data.code == 200) {
        this.classInfo = res.data.data;
        // console.warn(this.classInfo);
      }
    });
  },
  mounted() {
    this.activePane = "pane-log";
  },
  components: { PaneLog, PaneManage, PaneSign },
  methods: {
    addMessage() {
      this.addMessageDialog = true;
    },
    closeMessageDialog() {
      this.addMessageDialog = false;
      this.messageForm.title = "";
      this.messageForm.msg = "";
      this.createTime = null;
    },
    clickSubmit() {
      this.messageForm.createTime = this.$dayjs().unix();
      api.addMessage(this.id, this.messageForm).then((res) => {
        if (res.data.code == 200) {
          ElMessage.success('任务发布成功')
          this.messageInfo = res.data.data.sort((l, r) => {
            return r.createTime - l.createTime;
          });
        } else {
          ElMessage.error('任务发布失败')
        }
      });
    },
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
  overflow: hidden;
}

.teacherLog .radioTab {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  color: #4f95f5;
  min-width: 1090px;
  padding-top: 30px;
  padding-left: 20px;
  z-index: 9;
  background-color: #f5f5f5;
  width: 100%;
  position: relative;
  cursor: pointer;
}
</style>