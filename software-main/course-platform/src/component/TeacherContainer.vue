<template>
  <div class="teacherContainer">
    <el-row>
      <el-col class="layoutHeader" :xs="8" :sm="8" :md="8" :lg="8" :xl="6">
        <h3>{{ lessonData[0].course.name }}</h3>
        <div class="buttonGroup">
          <el-tooltip content="编辑"
            ><el-icon :size="18" color="#9b9b9b"><edit /></el-icon
          ></el-tooltip>
          <el-tooltip content="添加"
            ><el-icon :size="18" color="#9b9b9b"><plus /></el-icon
          ></el-tooltip>
          <el-tooltip content="删除"
            ><el-icon :size="18" color="#9b9b9b"><delete /></el-icon
          ></el-tooltip>
        </div>
      </el-col>
    </el-row>
    <div class="TCardGroup">
      <el-row style="margin-left: -20px; margin-right: -20px" :gutter="40">
        <el-col
          
          class="teacherCol"
          :xs="8"
          :sm="8"
          :md="8"
          :lg="8"
          :xl="6"
        ></el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
export default {
  name: "TeacherContainer",
  props: {
    lessonData: Object,
  },
  data() {
    return {};
  },
  methods: {
    logoutClass() {
      console.warn("logOut");
    },
  },
};
</script>

<style scoped>
.teacherContainer {
  margin-bottom: 30px;
}

.layoutHeader {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: start;
  -ms-flex-pack: start;
  justify-content: flex-start;
  margin-bottom: 10px;
  height: 18px;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
}

.layoutHeader h3 {
  font-weight: 900;
  padding-right: 20px;
  font-size: 16px;
  color: #333;
  line-height: 18px;
  max-width: 65%;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  text-align: left;
}

.layoutHeader .buttonGroup {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: start;
  -ms-flex-pack: start;
  justify-content: flex-start;
  font-size: 18px;
  line-height: 18px;
  color: #9b9b9b;
  visibility: hidden;
}

.layoutHeader .buttonGroup > i {
  cursor: pointer;
  outline: none;
  margin-right: 10px;
}

.teacherContainer:hover .layoutHeader .buttonGroup {
  visibility: visible;
}

.layoutHeader .buttonGroup > i:hover {
  color: #4f95f5;
}

.TCardGroup {
  width: 100%;
}

.TCardGroup .teacherCol {
  margin-bottom: 30px;
}
</style>