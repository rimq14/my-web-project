<template>
  <div class="hello">
    <div>
      <el-container>
        <el-header>
          <!--导航栏-->
          <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
            <el-menu-item index="1">Overview</el-menu-item>
            <el-submenu index="2">
              <template slot="title">功能选项</template>
              <el-menu-item index="2-1">变化检测</el-menu-item>
              <el-menu-item index="2-2">目标检测</el-menu-item>
              <el-menu-item index="2-3">目标提取</el-menu-item>
              <el-menu-item index="2-4">地物分类</el-menu-item>
            </el-submenu>
            <el-menu-item index="3">
              <router-link :to="{path:'/experience'}" class="btn btn-primary" role="button" target="_blank">
                <el-button type="text">体验中心</el-button>
              </router-link>
            </el-menu-item>
            <el-menu-item index="4">
              <router-link :to="{path:'/menu'}" class="btn btn-primary" role="button" target="_blank">
                <el-button type="text">进入平台</el-button>
              </router-link>
            </el-menu-item>
          </el-menu>
<!--          <router-link :to="{path:'/detail'}" class="btn btn-primary" role="button" target="_blank">books</router-link>-->
<!--          <router-link :to="{path:'/hello'}" class="btn btn-primary" role="button" target="_blank">pics</router-link>-->
        </el-header>
        <el-main>
          <!-- 走马灯  -->
          <el-carousel indicator-position="outside">
            <el-carousel-item v-for="item in items" :key="item">
              <el-image :src="item"></el-image>
            </el-carousel-item>
          </el-carousel>

        </el-main>
      </el-container>
    </div>
  </div>
</template>

<script>
export default {
  name: 'index',
  data() {
    return {
      // 后端服务器图片
      items: [
        'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
        'https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg',
        '',
        ''
      ],
      activeIndex: '1',
      activeIndex2: '1',
    }
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-header {
  /*background-color: #B3C0D1;*/
  color: #333;
  text-align: right;
  line-height: 60px;
}

.el-main {
  /*background-color: #E9EEF3;*/
  color: #333;
  text-align: center;
  line-height: 160px;
}

.el-carousel__item h3 {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    line-height: 1200px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #0b121a;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }

body > .el-container {
  margin-bottom: 0;
}



</style>
