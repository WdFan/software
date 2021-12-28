<template>
  <div class="blank-card">
    <el-card class="box-card">
      <div class="container">
        <el-icon :size="30" color="#9b9b9b"><plus /></el-icon>
        <span>新增班级</span>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: "BlankCard",
  data() {
    return {};
  },
};
</script>

<style scoped>
.blank-card {
  width: 100%;
  height: 142px;
  position: relative;
  border-radius: 4px;
  cursor: pointer;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
}

.blank-card:hover {
  width: 100%;
  -webkit-box-shadow: rgba(0, 0, 0, 0.1) 0 2px 10px 0;
  box-shadow: rgba(0, 0, 0, 0.1) 0 2px 10px 0;
  -webkit-transform: translateY(-3px);
  transform: translateY(-3px);
}

.blank-card .box-card {
  width: 100%;
  height: 100%;
  color: #9b9b9b;
  font-size: 14px;
  border: 1px solid #ddd !important;
  -webkit-box-shadow: none !important;
  box-shadow: none !important;
}
</style>