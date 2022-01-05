<template>
  <div class="pane-manage">
    <div class="noUserContent" v-if="userList.length == 0">
      <el-image
        :src="require('@/assets/img/nostudent.png')"
        alt="noStudent"
      ></el-image>
      <p>暂无学生</p>
    </div>
    <div class="user-list" v-else>
      <el-table :data="userList" border style="width:100%">
        <el-table-column prop="stu_id" label="学号" sortable></el-table-column>
        <el-table-column prop="username" label="用户名"></el-table-column>
        <el-table-column prop="stu_name" label="姓名"></el-table-column>
        <el-table-column prop="stu_school" label="学校"></el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
export default {
  name: "paneManage",
  props: {
    userList: Array,
  },
  data() {
    return {};
  },
  mounted() {
    console.log(this.userList);
  },
};
</script>

<style scoped>
.pane-manage {
  height: calc(100% - 20px);
  overflow: auto;
  padding-top: 20px;
}
.pane-manage > .noUserContent {
  height: calc(100% - 160px);
  background: #fff;
  padding-top: 140px;
  border: 1px solid #eee;
  border-radius: 4px;
}

.noUserContent {
  padding-top: 140px;
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

.user-list {
  height: 100%;
}
</style>