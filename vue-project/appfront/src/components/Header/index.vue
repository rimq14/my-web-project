<template>
  <header class="header">
    <!--头部第一行导航栏区域  图标展示-->
    <div class="top">
      <h1 class="logoArea">
        <!-- router-link组件本省就是一个a标签 -->
        <router-link to="/home" class="logo">
          <img src="./images/logo.png" alt="图标"/>
        </router-link>
      </h1>
      <!-- 导航栏区域 菜单按钮 -->
      <div class="navArea">
        <button
          class="sui-btn btn-xlarge btn-danger"
          type="button"
          @click="goMenu"
        >菜单
        </button>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: "index",
  data() {
    return{}
  },
  methods:{
    goMenu(){
      this.$router.push({path:'/menu'})   // 跳转至菜单路由
    },
  },
}
</script>

<style scoped lang="less">
.header{
  & > .top{
    width:1200px;
    margin: 0 auto;
    overflow: hidden;

    .logoArea{
      float: left;

      .logo{
        img{
          width: 175px;
          margin: 25px 45px;
        }
      }
    }
    .navArea{
      float: right;
      margin-top: 35px;

      button{
        height: 32px;
        width: 68px;
        background-color: #00b3ee;
        border: none;
        color: #abdde5;
        float: left;
      }
    }
  }
}
</style>
