<template xmlns="http://www.w3.org/1999/html">
  <div class="hello">
    <div>
      <el-container>
        <!--不知道这个地方是干啥的-->
        <el-header class="el-header">
          <!--导航栏-->
          <el-menu :default-active="activeIndex2" class="el-menu-demo" mode="horizontal" @select="handleSelect"
            background-color="rgb(35, 35, 35)" text-color="#fff" active-text-color="white">
            <el-menu-item index="1">Overview</el-menu-item>
            <!---->
            <el-submenu index="2">
              <template slot="title" >功能选项</template>
              <el-menu-item index="2-1">
                <router-link class="list-group-item" active-class="active" to="/experience/change_detection" >变化检测
                </router-link>
              </el-menu-item>
              <el-menu-item index="2-2">
                <router-link class="list-group-item" active-class="active" to="/experience/target_detection">目标检测
                </router-link>
              </el-menu-item>
              <el-menu-item index="2-3">
                <router-link class="list-group-item" active-class="active" to="/experience/target_extraction">目标提取
                </router-link>
              </el-menu-item>
              <el-menu-item index="2-4">
                <router-link class="list-group-item" active-class="active" to="/experience/object_classification">地物分类
                </router-link>
              </el-menu-item>
            </el-submenu>

            <el-menu-item index="3">
              <router-link :to="{ path: '/experience/change_detection' }" class="btn btn-primary" role="button"
                target="_blank">
                <!---->
                <button class="el_button" @mouseover="change1()" @mouseleave="changeback1()">体验中心</button>
              </router-link>

            </el-menu-item>
            <el-menu-item index="4">
              <router-link :to="{ path: '/menu' }" class="btn btn-primary" role="button" target="_blank">
                <!---->
                <button class="el_button" @mouseover="change2()" @mouseleave="changeback2()">进入平台</button>
              </router-link>
            </el-menu-item>
          </el-menu>
        </el-header>
        <!--页面大标题-->
        <el-main>
          <h1 style="font-size:4em;font-weight: 500;color:white;
          margin-bottom: 50px;">智能遥感图像解析平台</h1>
          <p style="color:white">
            深度学习
          </p>
          <router-link :to="{ path: '/menu' }" class="btn btn-primary" role="button" target="_blank">
          <button class="main_button" @mouseover="turnBlack" @mouseout="turnWhite">
            <h2 style="font-weight: 350;">进入平台→</h2>
          </button></router-link>
        </el-main>

      </el-container>
    </div>
  </div>
</template>

<script>
export default {
  name: "index",
  data() {
    return {
      // 后端服务器图片+
      pictures: [
        "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        "https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg",
        "http://127.0.0.1:8000/media/pictures/90c8f476cd.png",
        "http://127.0.0.1:8000/media/pictures/82d8c7c349.png"
      ],
      activeIndex: "1"
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
    change1() {
      const elButton = document.querySelectorAll(".el_button");
      elButton[0].classList.add('over-button');
    },
    changeback1() {
      const elButton = document.querySelectorAll(".el_button");
      elButton[0].classList.remove('over-button');
    },
    change2() {
      const elButton = document.querySelectorAll(".el_button");
      
      elButton[1].classList.add('over-button');
    },
    changeback2() {
      const elButton = document.querySelectorAll(".el_button");
      elButton[1].classList.remove('over-button');
    },
    turnBlack() {
      const mainButton = document.querySelector(".main_button");
      mainButton.style.background = "rgba(32, 32, 32, 0.3)"
    }
    , turnWhite() {
      const mainButton = document.querySelector(".main_button");
      mainButton.style.background = "rgba(224, 221, 221, 0.3)"
    }
  }
};
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
* {
  margin: 0;
  padding: 0;
}

/*主页背景*/
.hello {
  width: 100%;
  height: 754px;
  background: url(../Experience/pic/earth1.png);
  background-size: cover;
  object-fit: cover;
  animation: fade 15s linear infinite;
}

@keyframes fade {
  0% {
    background: url(../Experience/pic/earth1.png) no-repeat center;
    background-size: cover;
  }

  25% {
    background: url(../Experience/pic/earth2.png) no-repeat center;
    background-size: cover;
  }

  50% {
    background: url(../Experience/pic/earth3.png) no-repeat center;
    background-size: cover;
  }

  75% {
    background: url(../Experience/pic/earth4.png) no-repeat center;
    background-size: cover;
  }

  100% {
    background: url(../Experience/pic/earth5.png) no-repeat center;
    background-size: cover;
  }
}

/*导航栏 */
.el-menu-demo {
  display: flex;
  justify-content: flex-end;
  background-color: rgb(40, 30, 137);
}

/*导航栏的四小个提示*/
.el-menu-item {
  width: 160px;
  font-weight: 300;
}

.el-submenu {
  margin-right: 60px;
  ;
}

.images {
  width: auto;
  height: auto;
  /*border: 1px solid green;*/
}

/*页面的主要部分*/
.el-main {
  text-align: center;
  height: 500px;
  width: 50%;
  margin-left: auto;
  margin-right: auto;
  margin: auto;
  margin-top: 150px;
}

.el-main p {
  text-align: center;
  font-size: large;
  line-height: 35px;

}

.el_button {
  height: 30px;
  width: 90px;
  border: 1.5px solid rgb(184, 180, 180);
  background-color: rgb(122, 121, 119);
  color: white;
  border-radius: 4px;
}

.over-button {
  border: 2px solid rgb(74, 74, 204);
  background-color: rgb(30, 30, 30);
  opacity: 0.8;

}

/*下拉选框*/
.list-group-item {
  color: white;
}
</style>
<style>
.main_button {
  margin-top: 80px;
  height: 55px;
  width: 180px;
  border: 1px solid white;
  background-color: rgba(224, 221, 221, 0.3);
  color: white;
  border-radius: 3px;
}
</style>
