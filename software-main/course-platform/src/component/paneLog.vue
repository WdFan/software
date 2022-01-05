<template>
  <div class="pane-log">
    <div class="noTeachingContent" v-if="messageList.length == 0">
      <el-image
        :src="require('@/assets/img/noactivity.png')"
        alt="noMessage"
      ></el-image>
      <p>暂无任务</p>
    </div>
    <div class="logs-list" v-else>
      <div class="card" v-for="(message, index) in messageList" :key="index">
        <div class="message-box">
          <div class="time">
            {{ this.$dayjs.unix(message.createTime).format("MM-DD HH:mm:ss") }}
            周{{ this.$dayjs.unix(message.createTime).format("d") }}
          </div>
          <div class="content-box">
            <div class="activity__wrap">
              <div class="activity-info">
                <div>
                  <h2>{{ message.title }}</h2>
                  <div class="sub-info">
                    {{ message.msg }}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "paneLog",
  props: {
    messageList: Array,
  },
  data() {
    return {};
  },
  mounted() {
    console.log(this.messageList);
  },
};
</script>

<style scoped>
.pane-log {
  height: calc(100% - 70px);
  overflow: auto;
  padding-top: 20px;
}
.pane-log > .noTeachingContent {
  height: calc(100% - 160px);
  background: #fff;
  padding-top: 140px;
  border: 1px solid #eee;
  border-radius: 4px;
}

.noTeachingContent {
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

.card:first-of-type {
  margin-top: 0;
}

.card {
  position: relative;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
  margin-top: 20px;
}

.card .message-box {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  padding-left: 8px;
}

.card .message-box .time {
  margin: 20px 17px 0 0;
  width: 50px;
  height: 30px;
  background: #f5f5f5;
  font-size: 14px;
  color: #333;
  text-align: center;
  line-height: 30px;
  font-weight: 500;
}

.card .content-box {
  background: #fff;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 20px;
  -webkit-box-flex: 1;
  -ms-flex: 1;
  flex: 1;
}

.logs-list {
  height: 100%;
}

.activity__wrap {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: start;
  -ms-flex-align: start;
  align-items: flex-start;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
  cursor: pointer;
}

.activity__wrap .activity-info {
  -webkit-box-flex: 1;
  -ms-flex: 1;
  flex: 1;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: start;
  -ms-flex-align: start;
  align-items: flex-start;
  text-align: left;
}

.activity__wrap .activity-info h2 {
  font-size: 20px;
  font-weight: 600;
  line-height: 28px;
  color: #333;
  margin-right: 40px;
}

.activity__wrap .activity-info .sub-info {
  margin-top: 15px;
  font-size: 14px;
}
</style>