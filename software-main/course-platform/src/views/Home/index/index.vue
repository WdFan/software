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
      <span>加入班级</span>
      <span
        ><el-icon :size="14"><plus /></el-icon>创建课程</span
      >
    </div>
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
    };
  },
  watch: {
    tabActiveName() {
      this.$store.commit("updateTab", this.tabActiveName);
    },
  },
  methods: {},
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
</style>