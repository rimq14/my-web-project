<template>
  <div class="current-page">
    <el-container>
      <el-header>相关操作界面</el-header>
      <el-container>
        <!-- 折叠面板-->
        <pack-up>
          <div>
            <!-- 表格-->
            <el-table
              :data="tableData"
              style="width:auto">
              <el-table-column
                label="ID"
                prop="id">
              </el-table-column>

              <el-table-column
                label="IMG"
                prop="img">
              </el-table-column>

              <el-table-column
                align="right">
                <!-- 通过设置 Scoped slot 来自定义表头 -->
                <template slot="header">操作
                </template>
                <template v-slot="scope">
                  <!-- scope.row.img 获取图片链接数据-->
                  <el-button
                    size="mini"
                    type="text"
                    @click="loading(scope.row.img)">加载
                  </el-button>
                </template>
              </el-table-column>
            </el-table>
            <el-button @click="getpic">获取数据</el-button>
          </div>
        </pack-up>
        <!--界面内容 -->
        <div class="right">
          <el-main>
            <canvas
              id="myCanvas"
              width="800px"
              height="600px"
            ></canvas>
          </el-main>
        </div>
      </el-container>
    </el-container>
  </div>
</template>

<script>

import {getPic} from "../../api/apiRequest";
import packUp from "./packUp";
export default {
  name: "operation",
  components:{ packUp },
  data() {
    return {
      tableData: [],    // 列表显示的数据
    }
  },
  mounted() {},
  methods: {
    getpic() {
      getPic().then(res => {
        this.tableData = res.data
      })
    },    // 获取图片
    loading(img) {
      let image = new Image();
      image.src = img;
      // console.log(image.src)      // 查看是否读取到图片链接
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
    },    // 加载图片
  },
}
</script>

<style>
.current-page{
  width: 100%;
  height: 100%;
  display: flex;
}
.left{
  width: 500px;
}
.right{
  flex: 1;
}

.el-header {
  height: 40px;
  background-color: #B3C0D1;
  color: #333;
  text-align: center;
  line-height: 60px;
}

.el-main {
  margin: 0;
  padding: 0;
  background-color: #333333;
  color: #333;
  text-align: center;
}

canvas {
  display: block;
  background: #333333;
  width: 100%;
  height: auto;
}

</style>
