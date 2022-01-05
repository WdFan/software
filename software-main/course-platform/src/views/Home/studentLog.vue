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
            ><span>{{ classInfo.course.teacher }}</span></span
          >
          <span
            ><el-icon color="#333" :size="14"><home-filled /></el-icon
            ><span>{{ classInfo.name }}</span></span
          >
        </div>
      </el-header>

      <el-main>
        <el-tabs class="mainTab" v-model="activePane">
          <el-tab-pane label="教学日志" name="pane-log" class="log">
            <PaneLog v-if="messageInfo" :messageList="messageInfo"></PaneLog>
          </el-tab-pane>
        </el-tabs>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import api from "../../api/api";
import PaneLog from "../../component/paneLog.vue";

export default {
  name: "teacherLog",
  props: ["id"],
  data() {
    return {
      classInfo: null,
      activePane: null,
      messageInfo: null,
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
  methods: {},
  components: { PaneLog },
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