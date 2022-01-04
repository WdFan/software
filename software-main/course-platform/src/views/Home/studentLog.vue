<template>
  <div class="index">
    <h1>student {{ id }}</h1>
  </div>
</template>

<script>
export default {
  name: "studentLog",
  props: ["id"],
  data() {
    return {};
  },
};
</script>