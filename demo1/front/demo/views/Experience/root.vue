<template>
  <div>
    <el-container>
      <!--  头部    -->
        <el-header>
           <el-row>
              <el-col>
                <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
                  <el-menu-item index="1">
                     <router-link class="list-group-item" active-class="active" to="/experience/change_detection">变化检测</router-link>
                  </el-menu-item>
                  <el-menu-item index="2">
                     <router-link class="list-group-item" active-class="active" to="/experience/target_detection">目标检测</router-link>
                  </el-menu-item>
                  <el-menu-item index="3">
                     <router-link class="list-group-item" active-class="active" to="/experience/object_classification">地物分类</router-link>
                  </el-menu-item>
                </el-menu>
              </el-col>
            </el-row>
        </el-header>
      </el-container>



    <!-- 子路由容器   -->
    <router-view/>
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
el-container{
  height: fit-content;
}

 div el-aside {
    color: #333;
    text-align: center;
  }

  el-row {
    margin-bottom: 0;
  }

  el-col {
    border-radius: 4px;
  }
</style>
