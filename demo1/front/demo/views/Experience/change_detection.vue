<template>
  <div class="index" >

    <!-- 表头   -->
    <el-container style="height:690px;width:100%;">
      <!-- 侧边栏-->
      <el-aside width="420px" height="800px" >
        <div class="choice_box">
          <div class="choice" @click="blue1">
            <img :src="picone" class="choice_pic" />
            <h4 style="font-weight:500">建筑物提取</h4>
          </div>
          <div class="choice" @click="blue2">
            <img :src="pictwo" class="choice_pic" />
            <h4 style="font-weight:500">SAR水体提取</h4>
          </div>
          <div class="choice" style="margin-top:10px;" @click="blue3">
            <img :src="picthree" class="choice_pic" />
            <h4 style="font-weight:500">地块提取</h4>
          </div>
        </div>
        <div style="width:94%;height:10px;margin-left: 3%;">
          <hr style="border:0.3px solid  grey;" />

        </div>
      
          <h4 style="color:white;font-weight: 400;margin-top: 10px;">示例数据</h4>
          <img :src="example" class="example" />
       
      </el-aside>

      <!--  中间容器  -->
      <el-main>
        <div >
          <img :src="example" class="more" />
        </div>
        
      </el-main>
    </el-container>

  </div>
</template >

<script>
import building from "./pic/building.svg"
import bar from "./pic/bar.svg"
import piece from "./pic/piece.svg"
import example from "./pic/example.jpg"

export default {
  name: "index",
  data() {
    return {
      activeIndex: '1',
      src: 'http://127.0.0.1:8000/media/pictures/82d8c7c349.png',
      picone: building,
      pictwo: bar,
      picthree: piece,
      example: example

    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
    blue1() {
      const choices = document.querySelectorAll(".choice");
      choices[0].style.background = "radial-gradient(rgb(60, 66, 74) 0%,rgb(38, 109, 215) 100%"
      choices[1].style.background = "rgb(60, 66, 74)";
      choices[2].style.background = "rgb(60, 66, 74)";
    },
    blue2() {
      const choices = document.querySelectorAll(".choice");
      choices[1].style.background = "radial-gradient(rgb(60, 66, 74) 0%,rgb(38, 109, 215) 100%"
      choices[0].style.background = "rgb(60, 66, 74)";
      choices[2].style.background = "rgb(60, 66, 74)";
    },
    blue3() {
      const choices = document.querySelectorAll(".choice");
      choices[2].style.background = "radial-gradient(rgb(60, 66, 74) 0%,rgb(38, 109, 215) 100%"
      choices[1].style.background = "rgb(60, 66, 74)";
      choices[0].style.background = "rgb(60, 66, 74)";
    },
  }
}

</script>
<style scoped>
.template{
  width:100%;
  height:100%
}
.el-header {

  color: rgb(85, 82, 82);
  text-align: center;
  line-height: 60px;
}

.el-aside {
  color: #333;
  text-align: center;
}

.el-row {
  margin-bottom: 0;
  width: 500px;
}

.el-col {
  border-radius: 4px;
}

.el-main {

background-color: rgb(29, 28, 28);
text-align: center;
display: flex;
justify-content: center;
align-items: center;
}

</style>
<style >
.more{
height:400px;




}
.choice {
  margin-left: 18px;
  margin-right: 18px;
  color: white;
  height: 110px;
  width: 170px;
  border-radius: 6px;
  background-color: rgb(60, 66, 74);
}

.choice_box {
  margin-top: 30px;
  display: flex;
  flex-wrap: wrap;
  margin-bottom: 30px;
}

.choice_pic {
  height: 65px;
  margin-top: 6px;
}

.example {
  height: 170px;
  margin-top: 23px;
  border: 2px rgb(38, 109, 215) solid;
}

</style>
