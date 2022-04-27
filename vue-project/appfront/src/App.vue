<!--展示模板-->
<template>
  <div id="app">

  </div>
</template>



<script>
// 导入组件
export default {
  name: 'app',
  methods: {
    go() {
      // 注意path不能与params一起使用，需要通过path来匹配路由的时候，使用query来传参。
      // this.$router.push({name: 'test',params:{id:'3'}})    //注意这里一定要使用别名，否则无法用动态路由传值
      this.$router.push({path:'/demo3',query:{id:'1234'}})
    },
  },
  mounted() {
    console.log('挂载')
  }
}
</script>


<!--样式代码-->
<style scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
