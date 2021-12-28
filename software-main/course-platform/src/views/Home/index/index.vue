<template>
  <div class="index">
    <el-tabs v-model="tabActiveName">
      <el-tab-pane label="我教的课" name="teach">
        <div v-if="this.$store.state.userTeachData">
          <teacher-container
            v-for="teachData in this.$store.state.userTeachData"
            :lesson-data="teachData"
            :key="teachData.id"
          >
          </teacher-container>
        </div>
      </el-tab-pane>
      <el-tab-pane label="我听的课" name="study">
        <div class="TcardGroup">
          <el-row class="grid" v-if="this.$store.state.userStudyData">
            <el-col
              v-for="studyData in this.$store.state.userStudyData"
              :key="studyData.id"
              class="studentCol"
              :xs="8"
              :sm="8"
              :md="8"
              :lg="8"
              :xl="6"
            >
              <student-lesson-card
                :class-data="studyData"
              ></student-lesson-card>
            </el-col>
          </el-row>
        </div>
      </el-tab-pane>
    </el-tabs>

    <div class="headerButtonGroup">
      <span @click="joinClass = true">加入班级</span>
      <span @click="createLesson = true"
        ><el-icon :size="14"><plus /></el-icon>创建课程</span
      >
    </div>
    <el-dialog
      v-model="joinClass"
      title="加入班级"
      center
      width="350px"
      top="calc(50vh - 143px)"
      custom-class="specialDialog joinClassDialog"
    >
      <div class="dialog-body">
        <el-form :model="joinClassForm" class="commonForm joinClassForm">
          <el-form-item>
            <el-input
              type="text"
              :maxlength="6"
              :autofocus="true"
              v-model="joinClassForm.classId"
              @input="joinClassChange"
            ></el-input>
          </el-form-item>
          <div class="input-tips c9b">
            请输入班级邀请码/课堂暗号(不区分大小写)
          </div>
        </el-form>
        <div class="flexbox buttonGroup">
          <button class="cancel" @click="closeClassDialog">取消</button>
          <button
            :disabled="addClassButton"
            class="addButton"
            @click="studentJoinClass"
          >
            确认
          </button>
        </div>
      </div>
    </el-dialog>

    <el-dialog
      v-model="createLesson"
      width="460px"
      top="calc(50vh - 255px)"
      custom-class="specialDialog createLessonDialog editLessonDialog"
    >
      <template #title>
        <span class="dialog-header"
          ><span>创建课程</span>
          <span @click="closeCreateLessonDialog">取消</span></span
        >
      </template>

      <div class="dialog-body">
        <el-form :model="createLessonForm" class="commonForm">
          <el-form-item>
            <template #label
              ><div>
                <span class="name">课程名称</span>
                <span class="fill">必填</span>
              </div></template
            >
            <el-input
              @input="createLessonChange"
              v-model="createLessonForm.lessonName"
            ></el-input>
          </el-form-item>
          <el-form-item>
            <template #label
              ><div>
                <span class="name">课程简介</span>
                <span class="NoFill">选填</span>
              </div></template
            >
            <el-input v-model="createLessonForm.lessonSimpleName"></el-input>
          </el-form-item>
        </el-form>
        <button
          :disabled="createLessonButton"
          @click="doCreateLesson"
          class="createButton"
        >
          确认
        </button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import api from "../../../api/api";
import StudentLessonCard from "../../../component/StudentLessonCard.vue";
import TeacherContainer from "../../../component/TeacherContainer.vue";
export default {
  components: { TeacherContainer, StudentLessonCard },
  name: "index",
  data() {
    return {
      tabActiveName: "teach",
      joinClass: false,
      createLesson: false,
      joinClassForm: {
        classId: null,
      },
      createLessonForm: {
        lessonName: null,
        lessonSimpleName: null,
      },
      addClassButton: "disabled",
      createLessonButton: "disabled",
    };
  },
  watch: {
    tabActiveName() {
      this.getData();
      this.$store.commit("updateTab", this.tabActiveName);
    },
  },
  created() {
    if (this.tabActiveName != this.$store.state.home_index_tab) {
      this.tabActiveName = this.$store.state.home_index_tab;
    } else {
      this.getData();
    }
  },
  methods: {
    joinClassChange(value) {
      if (value && value.length > 0) {
        this.addClassButton = null;
      } else {
        this.addClassButton = "disabled";
      }
    },
    getData() {
      if (
        this.tabActiveName == "teach" &&
        this.$store.state.userTeachData === null
      ) {
        api.getTeachClass(this.$store.state.user_info.username).then((res) => {
          this.$store.state.userTeachData = res.data;
          // console.warn(res.data);
        });
      } else if (
        this.tabActiveName == "study" &&
        this.$store.state.userStudyData === null
      ) {
        api.getStudyClass(this.$store.state.user_info.username).then((res) => {
          this.$store.state.userStudyData = res.data;
          // console.warn(res.data);
        });
      }
    },
    studentJoinClass() {
      console.warn(this.joinClassForm.classId);
      this.closeClassDialog();
    },
    closeClassDialog() {
      this.joinClass = false;
      this.joinClassForm.classId = null;
      this.addClassButton = "disabled";
    },
    closeCreateLessonDialog() {
      this.createLesson = false;
      this.createLessonForm.lessonName = null;
      this.createLessonForm.lessonSimpleName = null;
      this.createLessonButton = "disabled";
    },
    createLessonChange(value) {
      if (value && value.length > 0) {
        this.createLessonButton = null;
      } else {
        this.createLessonButton = "disabled";
      }
    },
    doCreateLesson() {
      console.warn(this.createLessonForm);
      this.closeCreateLessonDialog();
    },
  },
};
</script>

<style scoped>
>>> .el-tabs__nav-scroll {
  padding-left: 45px;
}

>>> .el-tabs__item {
  height: 54px;
  line-height: 54px;
  font-size: 16px;
  color: #9b9b9b;
}

>>> .el-tabs__item.is-active {
  color: #4f95f5;
}

.index {
  min-width: 1130px;
  width: 100%;
  background-color: #fff;
  min-height: 100%;
  position: relative;
}

.index .headerButtonGroup {
  color: #9b9b9b;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: end;
  -ms-flex-pack: end;
  justify-content: flex-end;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  position: fixed;
  top: 0px;
  right: 45px;
  z-index: 1000;
}

.index .headerButtonGroup span {
  display: -webkit-inline-box;
  display: -ms-inline-flexbox;
  display: inline-flex;
  height: 54px;
  line-height: 54px;
  cursor: pointer;
  padding-left: 20px;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
}

.index .headerButtonGroup span:hover {
  color: #4f95f5;
}

.specialDialog.joinClassDialog .dialog-body {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -ms-flex-direction: column;
  flex-direction: column;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
}

.specialDialog.joinClassDialog .dialog-body .joinClassForm {
  padding-bottom: 0;
  border-bottom: none;
}

.specialDialog .dialog-body .commonForm {
  padding-bottom: 40px;
  border-bottom: 1px solid #eee;
}

.specialDialog.joinClassDialog .dialog-body .joinClassForm .el-form-item {
  margin-bottom: 0;
}

.el-input {
  position: relative;
  font-size: 14px;
  display: inline-block;
  width: 100%;
}

.specialDialog.joinClassDialog .dialog-body .joinClassForm .input-tips {
  font-size: 14px;
  text-align: left;
  margin-top: 10px;
  line-height: 20px;
}

.specialDialog.joinClassDialog
  .dialog-body
  .joinClassForm
  .el-form-item
  .el-input {
  width: 290px;
  height: 32px;
}

.specialDialog.joinClassDialog .dialog-body .buttonGroup {
  width: 350px;
  padding: 0 60px;
  box-sizing: border-box;
}

.specialDialog.joinClassDialog .dialog-body .buttonGroup .addButton,
.specialDialog.joinClassDialog .dialog-body .buttonGroup .cancel {
  margin-top: 30px;
  width: 100px;
  height: 34px;
  border: none;
  border-radius: 20px;
  background-color: #4f95f5;
  color: #fff;
  font-size: 16px;
  outline: none;
  cursor: pointer;
}

.specialDialog.joinClassDialog .dialog-body .buttonGroup .addButton:disabled,
.specialDialog.joinClassDialog .dialog-body .buttonGroup .cancel:disabled {
  color: #9b9b9b;
  background-color: #ddd;
}

.specialDialog.joinClassDialog .dialog-body .buttonGroup .cancel {
  background: #fff;
  color: #5096f5;
  border: 1px solid #5096f5;
}

.specialDialog .dialog-header span:first-child {
  font-size: 18px;
  color: #333;
  font-weight: bold;
}

.specialDialog .dialog-header span:last-child {
  font-size: 14px;
  color: #4f95f5;
  cursor: pointer;
  font-weight: bold;
}

.specialDialog.createLessonDialog .dialog-body .createButton:disabled {
  color: #9b9b9b;
  background-color: #ddd;
}

.specialDialog.createLessonDialog .dialog-body .createButton {
  margin-top: 40px;
  width: 200px;
  height: 40px;
  border: none;
  border-radius: 20px;
  font-size: 16px;
  background-color: #4f95f5;
  font-weight: 500;
  color: #fff;
  outline: none;
  cursor: pointer;
}

.specialDialog .dialog-body .commonForm .el-form-item {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -ms-flex-direction: column;
  flex-direction: column;
  -webkit-box-align: start;
  -ms-flex-align: start;
  align-items: flex-start;
}

.specialDialog .dialog-body .commonForm .el-form-item:not(:last-child) {
  margin-bottom: 20px;
}

.specialDialog .dialog-body .commonForm .el-form-item:last-child {
  margin-bottom: 0;
}
.TcardGroup {
  width: 100%;
}

.TcardGroup .grid {
  margin-left: -20px;
  margin-right: -20px;
  -webkit-transition: all 1s;
  transition: all 1s;
}

.TcardGroup .studentCol {
  margin-bottom: 30px;
  padding: 0 20px;
}
</style>