<template>
  <div>
    <!--  头部    -->
    <el-menu :default-active="activeIndex2" class="el-menu-demo" mode="horizontal" @select="handleSelect"
      background-color="rgb(35, 35, 35)" text-color="grey" active-text-color="#fff">
      <el-menu-item index="1">
        <router-link class="list-group-item" active-class="active" to="/experience/change_detection"><h3 style="font-weight:400">变化检测</h3></router-link>
      </el-menu-item>
      <el-menu-item index="2">
        <router-link class="list-group-item" active-class="active" to="/experience/target_detection"><h3 style="font-weight:400">目标检测</h3></router-link>
      </el-menu-item>
      <el-menu-item index="3">
        <router-link class="list-group-item" active-class="active" to="/experience/object_classification"><h3 style="font-weight:400">地物分类</h3>
        </router-link>
      </el-menu-item>
    </el-menu>
    <!-- 子路由容器   -->
    <router-view />
  </div>
</template>

<script>
export default {
  name: "root",
  data() {
    return {
      activeIndex: '1',
      src: ''
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    }
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
}

.el-col {
  background-color: rgb(52, 52, 52);
  color:white;
  font-size: 15px;
  font-weight: 300;
  margin-top: 15px;
}

.el-aside {
  background-color: rgb(52, 52, 52);
  text-align: center;
}

.el-row {


  background-color: rgb(52, 52, 52);
}
</style>
