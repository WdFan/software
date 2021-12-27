<template>
  <div class="index">
    <el-tabs v-model="tabActiveName">
      <el-tab-pane label="我教的课" name="teach">教</el-tab-pane>
      <el-tab-pane label="我听的课" name="study">
        <el-row>
          <el-col :span="6" class="studentCol">
            <student-lesson-card
              style-str="style1"
              class-name="1班"
              course-name="英美文学鉴赏"
              teacher-name="周博"
            ></student-lesson-card>
          </el-col>
        </el-row>
      </el-tab-pane>
    </el-tabs>

    <div class="headerButtonGroup">
      <span @click="joinClass = true">加入班级</span>
      <span
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
              autofocus="true"
              v-model="joinClassForm.classId"
              @input="joinClassChange"
            ></el-input>
          </el-form-item>
          <div class="input-tips c9b">
            请输入班级邀请码/课堂暗号(不区分大小写)
          </div>
        </el-form>
        <div class="flexbox buttonGroup">
          <button
            class="cancel"
            @click="
              joinClass = false;
              joinClassForm.classId = null;
              diabledAddButton = 'disabled';
            "
          >
            取消
          </button>
          <button
            :disabled="diabledAddButton"
            class="addButton"
            @click="studentJoinClass"
          >
            确认
          </button>
        </div>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import StudentLessonCard from "@/component/StudentLessonCard.vue";
export default {
  components: { StudentLessonCard },
  name: "index",
  component: {
    StudentLessonCard,
  },
  data() {
    return {
      tabActiveName: this.$store.state.home_index_tab,
      joinClass: false,
      joinClassForm: {
        classId: null,
      },
      diabledAddButton: "disabled",
    };
  },
  watch: {
    tabActiveName() {
      this.$store.commit("updateTab", this.tabActiveName);
    },
  },
  methods: {
    joinClassChange(value) {
      if (value && value.length > 0) {
        this.diabledAddButton = null;
      } else {
        this.diabledAddButton = "disabled";
      }
    },
    studentJoinClass() {
      console.warn(this.joinClassForm.classId);
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

.studentCol {
  margin-bottom: 30px;
  padding: 0 20px;
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
</style>