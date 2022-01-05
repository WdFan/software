<template>
  <div class="pane-sign">
    <div class="noSignContent" v-if="signList.length == 0">
      <el-image
        :src="require('@/assets/img/nostudent.png')"
        alt="noSign"
      ></el-image>
      <p>暂无学生</p>
    </div>
    <div class="sign-list" v-else>
        <el-table :data="signList" border style="width:100%">
        <el-table-column prop="sid" label="学号" sortable></el-table-column>
        <el-table-column prop="sname" label="姓名"></el-table-column>
        <el-table-column prop="sign_time" label="签到时间" sortable></el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
export default {
  name: "paneSign",
  props: {
    signList: Array,
  },
  data() {
    return {};
  },
  mounted() {
    console.log(this.signList);
  },
};
</script>

<style scoped>
.pane-sign {
  height: calc(100% - 20px);
  overflow: auto;
  padding-top: 20px;
}
.pane-sign > .noSignContent {
  height: calc(100% - 160px);
  background: #fff;
  padding-top: 140px;
  border: 1px solid #eee;
  border-radius: 4px;
}

.noSignContent {
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
</style>