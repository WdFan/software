<template>
  <div class="index">
    <h1>teacher {{ id }}</h1>
  </div>
</template>

<script>
export default {
  name: "teacherLog",
  props: ["id"],
  data() {
    return {};
  },
};
</script>