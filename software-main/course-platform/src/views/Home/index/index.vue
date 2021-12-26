<template>
  <div class="index">
    <el-tabs v-model="tabActiveName">
      <el-tab-pane label="我教的课" name="teach">教</el-tab-pane>
      <el-tab-pane label="我听的课" name="study">学</el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
export default {
  name: "index",
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
</style>