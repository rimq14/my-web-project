<template xmlns="http://www.w3.org/1999/html">
  <div class="hello">
    <div>
      <el-container>
        <el-header>
          <!--导航栏-->
          <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
            <el-menu-item index="1">Overview</el-menu-item>
            <el-submenu index="2">
              <template slot="title">功能选项</template>
              <el-menu-item index="2-1">
                <router-link class="list-group-item" active-class="active" to="/experience/change_detection">变化检测</router-link>
              </el-menu-item>
              <el-menu-item index="2-2">
                <router-link class="list-group-item" active-class="active" to="/experience/target_detection">目标检测</router-link>
              </el-menu-item>
              <el-menu-item index="2-3">
                <router-link class="list-group-item" active-class="active" to="/experience/target_extraction">目标提取</router-link>
              </el-menu-item>
              <el-menu-item index="2-4">
                <router-link class="list-group-item" active-class="active" to="/experience/object_classification">地物分类</router-link>
              </el-menu-item>
            </el-submenu>
            <el-menu-item index="3">
              <router-link :to="{path:'/experience/change_detection'}" class="btn btn-primary" role="button" target="_blank">
                <el-button type="text">体验中心</el-button>
              </router-link>
            </el-menu-item>
            <el-menu-item index="4">
              <router-link :to="{path:'/menu'}" class="btn btn-primary" role="button" target="_blank">
                <el-button type="text">进入平台</el-button>
              </router-link>
            </el-menu-item>
          </el-menu>
        </el-header>
        <div class="images">
          <!-- 走马灯  -->
          <el-carousel :interval="3000" type="card" height="400px">
            <el-carousel-item v-for="item in pictures" :key="item">
              <el-image
                style="width: 100%; height: 100%;"
                :src="item"></el-image>
            </el-carousel-item>
          </el-carousel>
        </div>
        <el-main>
          <p><strong>智能遥感图像解析平台</strong></p>
          <p>基于国产深度学习框架百度飞桨进行模型搭建,并利用百度Aistudio进行模型训练</p>
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
      pictures: [
        'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
        'https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg',
        'http://127.0.0.1:8000/media/pictures/90c8f476cd.png',
        'http://127.0.0.1:8000/media/pictures/82d8c7c349.png'
      ],
      activeIndex: '1',
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
.hello {
  width: 100%;
}

.images {
  width: auto;
  height: auto;
  /*border: 1px solid green;*/
}
 .el-main {
   text-align: center;
 }
.el-main p {
  text-align: center;
  font-size: large;
}
</style>
