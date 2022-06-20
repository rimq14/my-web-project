<template>
  <div>
    <!--  头部    -->

    <el-header>
      <div class="header_left_try">
        <div>
          <h4 style="font-weight:400;" class="header_char">数据集</h4>
        </div>
        <div>
          <h4 style="font-weight:400;color: rgb(63, 125, 217)">体验中心</h4>
        </div>
        <div>
          <h4 style="font-weight:400" class="header_char">解决方案</h4>
        </div>
      </div>

      <div class="header_right_try">
        <button class="header_button_try">
          <router-link :to="{ path: '/menu' }" class="except" style="color:white;">
            进入平台
          </router-link>
        </button>
      </div>

    </el-header>

    <div>
      <div class="other">
        <div class="aside">
          <div class="try_choices">
            <router-link :to="{ path: '/experience/target_detection' }" active-class="active">
              <div class="try_choice">
                目标提取
              </div>
            </router-link>
            <router-link :to="{ path: '/experience/object_classification' }" active-class="active">
              <div class="try_choice"> 地物分类 </div>
            </router-link>
            <router-link :to="{ path: '/experience/change_detection' }" active-class="active">
              <div class="try_choice"> 变化检测 </div>
            </router-link>
          </div>
          <router-view></router-view>
        </div>
      </div>

    </div>




    <!--侧边选择栏-->

    <!-- 子路由容器   -->


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

.aside {
  width: 440px;
  height: 60px;
  background-color: #333;
  padding-top: 20px;
}

.el-header {
  height: 40px;
  background-color: #1f1f20;
  color: white;
  text-align: center;
  line-height: 40px;
}

.header_left_try {
  height: 60px;
  width: 25%;
  background-color: #1f1f20;
  color: white;
  text-align: center;
  line-height: 60px;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  margin-left: 130px;
}

.header_char:hover {
  color: rgb(63, 125, 217);
}

.header_button_try {
  height: 35px;
  width: 100px;
  border-radius: 3px;
  border: 1px solid white;
  background-color: rgb(112, 109, 109);
  color: white;
  margin-top: -10px;
}

.header_button_try:hover {

  background-color: black;
  border: 1px solid rgb(63, 125, 217);
}

.header_right_try {
  position: absolute;
  height: 35px;
  left: 1280px;
  top: 10px;

}

.except:hover {
  color: white;
  background-color: black;
}

/*侧边选择栏*/
.try_choices {
  height: 35px;
  width: 90%;
  border-radius: 3px;

  margin-left: auto;
  margin-right: auto;

  background-color: #252424;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  flex-wrap: nowrap;
  justify-items: center;
}

a {
  color: grey;
  text-align: center;
  line-height: 35px;
  width: 100%;
  text-decoration: none;
}

a:hover {
  background-color: grey;
  color: white;
}

.active {
  background-color: grey;
  color: white;
}

/*其余部分*/
.other {
  background-color: antiquewhite;
  height:694px;
}
</style>
