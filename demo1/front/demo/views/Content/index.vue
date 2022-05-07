<template>
  <div class="index">
    <el-container>
      <el-header></el-header>
      <el-main>
        <div>
          <nav class="nav align-items-center">
            <h1>功能选择</h1>
          </nav>
        </div>

        <div>
          <el-row>
            <router-link :to="{path:'/change_detection'}" class="btn btn-primary" role="button" target="_blank">
              <el-button>变化检测</el-button>
            </router-link>
            <router-link :to="{path:''}" class="btn btn-primary" role="button" target="_blank">
              <el-button>目标提取</el-button>
            </router-link>
            <router-link :to="{path:''}" class="btn btn-primary" role="button" target="_blank">
              <el-button>目标检测</el-button>
            </router-link>
            <router-link :to="{path:''}" class="btn btn-primary" role="button" target="_blank">
              <el-button>地物分类</el-button>
            </router-link>
          </el-row>
        </div>

      </el-main>
    </el-container>
  </div>

</template>

<script>
export default {
  name: "index",

}
</script>



<style scoped>
.el-header {
  background-color: #B3C0D1;
  color: #333;
  /*text-align: center;*/
  line-height: 60px;

}

.el-main {
  background-color: #E9EEF3;
  color: #333;
  text-align: center;
  line-height: 160px;
}

.nav {
  text-align: center;
  line-height: 60px;
}


</style>
