<template>
  <div class="teacherLog">
    <el-container>
      <el-header> </el-header>

      <el-main> </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "teacherLog",
  props: ["id"],
  data() {
    return {
      classInfo: {
        id: 7,
        course: {
          id: 1,
          teacher: "zhoubo",
          name: "高等工程数学",
          simple_name: "高工",
        },
        name: "电子信息2班",
        year: 2021,
        season: "秋季",
        couid: 1,
        color: "style0",
        num: 2,
        code: "GYQIX",
        student: [1, 2, 3],
      },
    };
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
</style>