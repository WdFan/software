<template>
  <div class="home">
    <el-container>
      <el-aside>
        <el-scrollbar style="width: 100%">
          <el-menu default-active="2" :collapse="true" @select="menuAction">
            <el-submenu index="1" style="padding: 20px 0 0">
              <template #title>
                <el-icon :size="25"><user /></el-icon
                ><span>用户</span></template
              >
              <el-menu-item-group>
                <template #title
                  ><span class="userInfoPopover">你好，{{ username }}</span></template
                >
                <el-menu-item index="1-1" class="subitem1"
                  >个人中心</el-menu-item
                >
                <el-menu-item index="1-2" class="subitem2">退出</el-menu-item>
              </el-menu-item-group>
            </el-submenu>
            <el-menu-item index="2">
              <el-icon :size="25"><icon-menu /></el-icon
              ><template #title><span>课程班级</span></template>
            </el-menu-item>
          </el-menu>
        </el-scrollbar>
      </el-aside>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import { ElMessage } from "element-plus";
import { Menu as IconMenu } from "@element-plus/icons-vue";

export default {
  name: "home",
  components: {
    IconMenu,
  },
  data() {
    return {
      username: this.$store.state.user_info.stu_name,
    };
  },
  methods: {
    logout() {
      this.$store.commit('clearUser');
      ElMessage.success("退出成功！");
      this.$router.push("/login");
    },
    menuAction(index) {
      switch (index) {
        case "1-1":
          this.$router.push("/home/personal");
          break;
        case "1-2":
          this.logout();
          break;
        case "2":
          this.$router.push("/home/index");
          break;
      }
    },
  },
};
</script>

<style scoped>
.home,
.el-container {
  height: 100vh;
}

.el-aside {
  background-color: #e9eef3;
  width: 70px;
  max-width: 70px;
  min-width: 70px;
  height: 100vh;
}

.el-main {
  background-color: #fff;
  color: var(--el-text-color-primary);
  text-align: center;
  padding: 0;
}

.el-menu--collapse {
  width: 100%;
  background-color: #e9eef3;
}
.el-submenu,
.el-menu-item,
.el-menu-item-group {
  text-align: center;
}

.subitem1,
.subitem2 {
  height: 30px;
  line-height: 30px;
}

.subitem2 {
  color: crimson;
}

>>> .el-menu-item-group__title {
  font-size: 15px;
  padding: 7px 20px;
}

>>> .el-tabs__active-bar {
  margin-bottom: 2px;
  height: 4px;
  max-width: 34px;
}

.userInfoPopover {
    padding: 8px 0;
    text-align: center;
    font-size: 14px;
    line-height: 18px;
    color: #9b9b9b;
}
</style>