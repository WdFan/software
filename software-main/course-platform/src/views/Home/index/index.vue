<template>
  <div class="index">
    <el-tabs v-model="tabActiveName">
      <el-tab-pane label="我教的课" name="teach">
        <div v-if="this.$store.state.userTeachData" v-loading="loading1">
          <teacher-container
            v-for="teachData in this.$store.state.userTeachData"
            :lesson-data="teachData"
            :key="teachData.id"
            @addClass="showAddClass"
            @editClass="editClass"
            @editLesson="editLesson"
            @deleteLesson="deleteLesson"
            @deleteClass="deleteClass"
          >
          </teacher-container>
        </div>
      </el-tab-pane>
      <el-tab-pane label="我听的课" name="study">
        <div class="TcardGroup">
          <el-row
            class="grid"
            v-if="this.$store.state.userStudyData"
            v-loading="loading2"
          >
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
                @clickQuitButton="quitClass"
              ></student-lesson-card>
            </el-col>
          </el-row>
        </div>
      </el-tab-pane>
    </el-tabs>

    <div class="headerButtonGroup">
      <span @click="joinClassDialog = true">加入班级</span>
      <span @click="createLessonDialog = true"
        ><el-icon :size="14"><plus /></el-icon>创建课程</span
      >
    </div>
    <el-dialog
      v-model="joinClassDialog"
      title="加入班级"
      center
      width="350px"
      top="calc(50vh - 143px)"
      custom-class="specialDialog joinClassDialog"
      @closed="closeClassDialog"
    >
      <div class="dialog-body">
        <el-form :model="joinClassForm" class="commonForm joinClassForm">
          <el-form-item>
            <el-input
              type="text"
              :maxlength="6"
              :autofocus="true"
              v-model="joinClassForm.classCode"
              @input="joinClassChange"
            ></el-input>
          </el-form-item>
          <div class="input-tips c9b">请输入班级邀请码/课堂暗号</div>
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
      v-model="createLessonDialog"
      width="460px"
      top="calc(50vh - 255px)"
      custom-class="specialDialog createLessonDialog editLessonDialog"
      @closed="closeCreateLessonDialog"
    >
      <template #title>
        <span class="dialog-header"
          ><span>{{ lessonDialogTitle }}</span>
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

    <el-dialog
      v-model="createClassDialog"
      width="460px"
      top="calc(50vh - 230px)"
      custom-class="specialDialog createClassDialog editClassDialog"
      @closed="closeCreateClassDialog"
    >
      <template #title>
        <span class="dialog-header"
          ><span>{{ classDialogTitle }}</span>
          <span @click="closeCreateClassDialog">取消</span></span
        >
      </template>

      <div class="dialog-body">
        <el-form :model="createClassForm" class="commonForm">
          <el-form-item>
            <template #label
              ><div>
                <span class="name">班级名称</span>
                <span class="fill">必填</span>
              </div></template
            >
            <el-input
              @input="createClassChange"
              v-model="createClassForm.name"
            ></el-input>
          </el-form-item>
          <el-form-item>
            <template #label
              ><div>
                <span class="name">开学学期</span>
              </div></template
            >
            <el-row :gutter="10">
              <el-col :xs="9" :sm="9" :md="9" :lg="9"
                ><el-select v-model="createClassForm.year" placeholder="请选择">
                  <el-option
                    v-for="year in classYearOptions"
                    :key="year"
                    :value="year"
                  ></el-option> </el-select
              ></el-col>
              <el-col :xs="5" :sm="5" :md="5" :lg="5"
                ><span class="nowrap">学年度</span></el-col
              >
              <el-col :xs="10" :sm="10" :md="10" :lg="10"
                ><el-select
                  v-model="createClassForm.season"
                  placeholder="请选择"
                >
                  <el-option
                    v-for="season in classSeasonOptions"
                    :key="season"
                    :value="season"
                  ></el-option> </el-select
              ></el-col>
            </el-row>
          </el-form-item>
        </el-form>
        <button
          :disabled="createClassButton"
          @click="doCreateClass"
          class="createButton"
        >
          确认
        </button>
      </div>
    </el-dialog>

    <el-dialog
      v-model="showWaringDialog"
      custom-class="warningDialog"
      width="350px"
      top="calc(50vh - 170px)"
      @closed="closeWarningDialog"
    >
      <template #title><span class="dialog-header">提示</span></template>
      <div class="word-container">
        <span>{{ warningDialog.warningInfo[warningDialog.type] }}</span>
      </div>
      <template #footer>
        <span class="dialog-footer">
          <el-button class="confirm" type="danger" round @click="confirmWarning"
            >退出</el-button
          >
          <el-button class="cancel" round @click="closeWarningDialog"
            >取消</el-button
          >
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script>
import { ElMessage } from "element-plus";
import api from "../../../api/api";
import StudentLessonCard from "../../../component/StudentLessonCard.vue";
import TeacherContainer from "../../../component/TeacherContainer.vue";
export default {
  components: { TeacherContainer, StudentLessonCard },
  name: "index",
  data() {
    return {
      loading1: false,
      loading2: false,
      tabActiveName: "teach",
      joinClassDialog: false,
      createLessonDialog: false,
      createClassDialog: false,
      classDialogTitle: "新增班级",
      lessonDialogTitle: "创建课程",
      joinClassForm: {
        classCode: null,
      },
      createLessonForm: {
        lessonName: null,
        lessonSimpleName: null,
      },
      createClassForm: {
        name: null,
        year: null,
        season: null,
        color: null,
        lessonId: null,
      },
      classYearOptions: [],
      classSeasonOptions: ["春季", "夏季", "秋季", "冬季"],
      addClassButton: "disabled",
      createLessonButton: "disabled",
      createClassButton: "disabled",
      editClassId: null,
      editLessonId: null,
      showWaringDialog: false,
      warningDialog: {
        warningInfo: [
          "该操作将退出班级，确定退出吗？",
          "课程删除后，该课程所有班级将被删除确认删除吗？",
          "该操作将清空该班级所有教学数据，确定删除吗？",
        ],
        type: null,
        id: null,
      },
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
    let nowYear = this.$dayjs().year();
    for (let i = 0; i < 5; ++i) {
      this.classYearOptions.push(nowYear + i);
    }
  },
  computed: {
    userInfo() {
      return this.$store.state.user_info;
    },
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
        this.loading1 = true;
        api.getTeachClass(this.userInfo.username).then((res) => {
          this.$store.state.userTeachData = res.data.sort((l, r) => {
            return r.id - l.id;
          });
          // console.warn(res.data);
          this.loading1 = false;
        });
      } else if (
        this.tabActiveName == "study" &&
        this.$store.state.userStudyData === null
      ) {
        this.loading2 = true;
        api.getStudyClass(this.userInfo.username).then((res) => {
          this.$store.state.userStudyData = res.data.sort((l, r) => {
            return r.id - l.id;
          });
          // console.warn(res.data);
          this.loading2 = false;
        });
      }
    },
    studentJoinClass() {
      api.joinClass(this.userInfo.username, this.joinClassForm).then((res) => {
        if (res.data.code == 200) {
          ElMessage.success(res.data.msg);
        } else {
          ElMessage.error(res.data.error);
        }
      });
      this.closeClassDialog();
    },
    closeClassDialog() {
      this.joinClassDialog = false;
      this.joinClassForm.classCode = null;
      this.addClassButton = "disabled";
    },
    closeCreateLessonDialog() {
      this.createLessonDialog = false;
      this.createLessonForm.lessonName = null;
      this.createLessonForm.lessonSimpleName = null;
      this.createLessonButton = "disabled";
      this.editLessonId = null;
      this.lessonDialogTitle = "创建课程";
    },
    closeCreateClassDialog() {
      this.createClassDialog = false;
      this.createClassForm.name = null;
      this.createClassForm.year = null;
      this.createClassForm.season = null;
      this.createClassForm.lessonId = null;
      this.createClassButton = "disabled";
      this.editClassId = null;
      this.classDialogTitle = "新增班级";
    },
    createLessonChange(value) {
      if (value && value.length > 0) {
        this.createLessonButton = null;
      } else {
        this.createLessonButton = "disabled";
      }
    },
    createClassChange(value) {
      if (value && value.length > 0) {
        this.createClassButton = null;
      } else {
        this.createClassButton = "disabled";
      }
    },
    doCreateLesson() {
      if (this.editLessonId) {
        api.editLesson(this.editLessonId, this.createLessonForm).then((res) => {
          console.log(res);
          ElMessage.success("编辑课程成功");
        });
      } else {
        api
          .createLesson(this.userInfo.username, this.createLessonForm)
          .then((res) => {
            this.$store.state.userTeachData = res.data.sort((l, r) => {
              return r.id - l.id;
            });
          });
      }
      this.closeCreateLessonDialog();
    },
    showAddClass(lessonId) {
      this.createClassDialog = true;
      this.createClassForm.lessonId = lessonId;
    },
    doCreateClass() {
      if (this.editClassId) {
        api.editClass(this.editClassId, this.createClassForm).then((res) => {
          console.log(res);
          ElMessage.success("编辑班级成功");
        });
      } else {
        this.createClassForm.color = "style" + Math.floor(Math.random() * 4);
        api.createClass(this.createClassForm).then((res) => {
          console.log(res);
          ElMessage.success("班级添加成功!");
        });
      }
      this.closeCreateClassDialog();
    },
    editLesson(lessonData) {
      this.editLessonId = lessonData.id;
      this.lessonDialogTitle = "编辑课程信息";
      this.createLessonForm.lessonName = lessonData.name;
      this.createLessonForm.lessonSimpleName = lessonData.simple_name;
      this.createLessonButton = null;
      this.createLessonDialog = true;
      // console.warn(lessonData);
    },
    editClass(classData) {
      this.editClassId = classData.id;
      this.classDialogTitle = "编辑班级信息";
      this.createClassForm.name = classData.name;
      this.createClassForm.year = classData.year;
      this.createClassForm.season = classData.season;
      this.createClassForm.color = classData.color;
      this.createClassForm.lessonId = classData.couid;
      this.createClassButton = null;
      this.createClassDialog = true;
      console.warn(classData);
    },
    quitClass(classInfo) {
      this.warningDialog.type = 0;
      this.warningDialog.id = classInfo.id;
      this.showWaringDialog = true;
    },
    deleteLesson(lessonId) {
      this.warningDialog.type = 1;
      this.warningDialog.id = lessonId;
      this.showWaringDialog = true;
    },
    deleteClass(classId) {
      this.warningDialog.type = 2;
      this.warningDialog.id = classId;
      this.showWaringDialog = true;
    },
    closeWarningDialog() {
      this.showWaringDialog = false;
      this.warningDialog.type = null;
      this.warningDialog.id = null;
    },
    confirmWarning() {
      if (this.warningDialog.type == 0) {
        api
          .quitClass(this.userInfo.username, this.warningDialog.id)
          .then((res) => {
            console.log(res);
          });
      } else if (this.warningDialog.type == 1) {
        api.deleteLesson(this.warningDialog.id).then((res) => {
          console.log(res);
        });
      } else if (this.warningDialog.type == 2) {
        api.deleteClass(this.warningDialog.id).then((res) => {
          console.log(res);
        });
      }
      this.closeWarningDialog();
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

.specialDialog.createClassDialog .dialog-body .createButton {
  margin-top: 40px;
  width: 200px;
  height: 40px;
  border: none;
  border-radius: 20px;
  font-size: 16px;
  background-color: #4f95f5;
  color: #fff;
  outline: none;
  cursor: pointer;
}

.specialDialog.createClassDialog .dialog-body .createButton:disabled {
  color: #9b9b9b;
  background-color: #ddd;
}
</style>