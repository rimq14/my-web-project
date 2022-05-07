<template>
  <div class="index">
    <el-container>
      <!-- 表头   -->
      <el-header>Header</el-header>
      <el-container>
        <!-- 侧边栏-->
        <el-aside width="300px">
          <el-row>
            <el-col>
              <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
                <el-menu-item index="1">目标提取</el-menu-item>
                <el-menu-item index="2">地物分类</el-menu-item>
                <el-menu-item index="3">变化检测</el-menu-item>
              </el-menu>
            </el-col>
          </el-row>

          <el-row>
            <el-col>
              示例数据
            </el-col>
          </el-row>

          <el-row>
            <el-main>
              <el-image :src="src" style="width: 280px;height: 100px"></el-image>
            </el-main>
          </el-row>
        </el-aside>

        <!--  中间容器  -->
        <el-main>
           <el-image :src="src" style="width: 280px;height: 100px"></el-image>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "index",
  data() {
    return {
      activeIndex: '1',
       src: 'http://127.0.0.1:8000/media/pictures/82d8c7c349.png'
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    }
  }
}
</script>

<style scoped>
.el-container{
  height: fit-content;
}
  .el-header {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }

  .el-aside {
    color: #333;
    text-align: center;
  }

  .el-row {
    margin-bottom: 0;
  }

  .el-col {
    border-radius: 4px;
  }
  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 500px;
  }

</style>
