<template>
  <div>
    编程式导航页面
    <p>成功跳转到demo3</p>
  </div>
</template>

<script>
  export default {
    name: "demo3",
    data() {
      return {}
    },
    mounted() {
      console.log(this.$route.params.id)
      // console.log(this.$route.query.aid)
    }
}
</script>

<style scoped>

</style>
