<template>
  <div class="operation">
    <el-container>
      <el-header>Header</el-header>
      <el-container>
        <el-aside width="200px">
          <h1>变化检测</h1>
          <el-button @click="getpic">获取图片</el-button>
          <ul>
            <li v-for="(img,index) in pic" :key="index" style="display: block">
              {{ img.id }}: {{ img.img }}
            </li>
          </ul>
        </el-aside>
        <el-main>
          <div>
            <canvas
              id="myCanvas"
              width="800"
              height="600"
              style="display: block;width: 100%;height: auto;"
            ></canvas>
            <el-button @click="qg">切割图片</el-button>
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>

import {getPic} from "../../api/apiRequest";

export default {
  name: "operation",
  data(){
    return{
         pic:[]
    }
  },
  methods:{
    getpic(){
      getPic().then(res =>{
        this.pic = res.data
      })
    },
    qg() {
      let image = new Image();
      image.src = "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg";
      let canvas = document.getElementById("myCanvas");   // 查找特定元素
      let context = canvas.getContext("2d");
      let boxWidth, boxHeight;
      let rows = 10,
        columns = 20,
        counter = 0;

      image.onload = function () {
        boxWidth = image.width / columns;
        boxHeight = image.height / rows;
        requestAnimationFrame(animate);
      };

      function animate() {
        let x = Math.floor(Math.random() * columns);
        let y = Math.floor(Math.random() * rows);
        context.drawImage(
          image,
          x * boxWidth, // 横坐标起始位置
          y * boxHeight, // 纵坐标起始位置
          boxWidth, // 图像的宽
          boxHeight, // 图像的高
          x * boxWidth, // 在画布上放置图像的 x 坐标位置
          y * boxHeight, // 在画布上放置图像的 y 坐标位置
          boxWidth, // 要使用的图像的宽度
          boxHeight // 要使用的图像的高度
        );
        counter++;
        if (counter > columns * rows * 0.9) {
          context.drawImage(image, 0, 0);
        } else {
          requestAnimationFrame(animate);
        }
      }
    },
  }
}
</script>

<style>
 .el-header {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }

  .el-aside {
    background-color: #333333;
    color: #333;
    text-align: center;
    line-height: 200px;
  }

  .el-main {
    background-color: #333333;
    color: #333;
    text-align: center;
    line-height: 160px;
  }

  body > .el-container {
    margin-bottom: 40px;
  }

  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }

  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }
</style>
