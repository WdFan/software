<template>
  <div class="lesson-cardS" @click="jumpToStudentPage">
    <el-card :class="'box-card ' + classData.color" shadow="hover">
      <div class="left">
        <div class="top">
          <h1>{{ classData.course.name }}</h1>
          <span class="hidden"></span> <span class="hidden2"></span>
        </div>
        <div class="bottom">
          <span class="avatorContainer">
            <span class="teacherName">{{
              classData.course.teacher
            }}</span></span
          >
          <span>
            <el-icon color="#fff" :size="18"><home-filled /></el-icon>
            <span class="className">{{ classData.name }}</span></span
          >
        </div>
      </div>
      <div class="right">
        <el-dropdown
          ><el-icon color="#fff" :size="22"><more-filled /></el-icon>
          <template #dropdown>
            <el-dropdown-menu style="padding: 5px 0">
              <el-dropdown-item @click="quitClass">退出</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </div>
    </el-card>
    <div class="mark">
      <img
        v-if="classData.color == 'style0'"
        :src="require('@/assets/img/mark0.png')"
        alt="mark"
      />
      <img
        v-else-if="classData.color == 'style1'"
        :src="require('@/assets/img/mark1.png')"
        alt="mark"
      />
      <img
        v-else-if="classData.color == 'style2'"
        :src="require('@/assets/img/mark2.png')"
        alt="mark"
      />
      <img
        v-else-if="classData.color == 'style3'"
        :src="require('@/assets/img/mark3.png')"
        alt="mark"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "StudentLessonCard",
  props: {
    classData: Object,
  },
  data() {
    return {};
  },
  methods: {
    quitClass() {
      this.$emit('clickQuitButton', this.classData);
    },
    jumpToStudentPage() {
      this.$router.push("/home/studentLog/" + this.classData.id);
    },
  },
};
</script>

<style scoped>
.el-card {
  -webkit-box-shadow: 0 1px 4px 0 rgba(0, 0, 0, 0.1) !important;
  box-shadow: 0 1px 4px 0 rgba(0, 0, 0, 0.1) !important;
  border: 0 !important;
}

.el-card {
  border-radius: 4px;
  border: 1px solid #ebeef5;
  background-color: #fff;
  overflow: hidden;
  color: #303133;
  -webkit-transition: 0.3s;
  transition: 0.3s;
}
.lesson-cardS {
  width: 100%;
  height: 142px;
  position: relative;
  border-radius: 4px;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
}

.lesson-cardS:hover {
  width: 100%;
  -webkit-box-shadow: rgba(0, 0, 0, 0.15) 0 2px 10px 0;
  box-shadow: rgba(0, 0, 0, 0.15) 0 2px 10px 0;
  -webkit-transform: translateY(-3px);
  transform: translateY(-3px);
  cursor: pointer;
}

.lesson-cardS .box-card > div .left {
  max-width: calc(100% - 60px);
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -ms-flex-direction: column;
  flex-direction: column;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
  -webkit-box-flex: 1;
  -ms-flex: 1;
  flex: 1;
}

.lesson-cardS .box-card > div .left .top h1 {
  font-weight: 500;
  text-align: left;
  font-size: 20px;
  word-break: break-all;
  word-wrap: break-word;
  line-height: 23px;
  max-height: 46px;
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  text-overflow: ellipsis;
  -webkit-line-clamp: 2;
}

.left {
  text-align: left;
}

.lesson-cardS .box-card {
  width: 100%;
  height: 100%;
  color: #fff;
  border: none;
}

.lesson-cardS .box-card > div .right {
  min-width: 60px;
  text-align: right;
  font-size: 20px;
  max-height: 40px;
}

.lesson-cardS .mark {
  position: absolute;
  top: 0;
  right: 0;
  height: 100%;
  z-index: 5;
}

.lesson-cardS .box-card > div .left .bottom {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: start;
  -ms-flex-pack: start;
  justify-content: flex-start;
  width: 100%;
  white-space: nowrap;
}

.lesson-cardS .box-card > div .left .bottom .avatorContainer {
  -webkit-box-flex: 0;
  -ms-flex-positive: 0;
  flex-grow: 0;
  -ms-flex-negative: 0;
  flex-shrink: 0;
  width: 40%;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
}

.lesson-cardS .box-card > div .left .bottom > span {
  font-size: 14px;
}

.lesson-cardS .box-card > div .left .bottom > span:last-child {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-flex: 1;
  -ms-flex: 1;
  flex: 1;
  width: 60%;
  text-align: left;
  margin-left: 20px;
}

.lesson-cardS .box-card > div .left .bottom .className,
.lesson-cardS .box-card > div .left .bottom .teacherName {
  overflow: hidden;
  width: 100%;
  text-align: left;
  text-overflow: ellipsis;
  white-space: nowrap;
  margin-left: 5px;
}

.lesson-cardS .mark img {
  display: block;
  height: 100%;
}

.lesson-cardS .box-card.style0 {
  background-image: -webkit-gradient(
    linear,
    left top,
    right bottom,
    from(#ff6098),
    to(#ffa96a)
  );
  background-image: linear-gradient(to bottom right, #ff6098, #ffa96a);
}

.lesson-cardS .box-card.style1 {
  background-image: -webkit-gradient(
    linear,
    left top,
    right bottom,
    from(#1fbdb8),
    to(#47e894)
  );
  background-image: linear-gradient(to bottom right, #1fbdb8, #47e894);
}

.lesson-cardS .box-card.style2 {
  background-image: -webkit-gradient(
    linear,
    left top,
    right bottom,
    from(#8360fa),
    to(#cb8dff)
  );
  background-image: linear-gradient(to bottom right, #8360fa, #cb8dff);
}

.lesson-cardS .box-card.style3 {
  background-image: -webkit-gradient(
    linear,
    left top,
    right bottom,
    from(#4762f3),
    to(#5cc3ff)
  );
  background-image: linear-gradient(to bottom right, #4762f3, #5cc3ff);
}

.lesson-cardS .box-card > div .right .el-dropdown {
  top: -5px;
  z-index: 9;
}
</style>
