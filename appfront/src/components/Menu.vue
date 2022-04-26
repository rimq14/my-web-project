<template>
  <div>demo2的内容</div>
</template>

<script>
export default {
  // name: "Menu",
  data(){
    return{

    }
  },
  mounted() {
      console.log(this.$route.query.id)       //页面控制台输出结果是1357
  }
}
</script>

<style scoped>

</style>
