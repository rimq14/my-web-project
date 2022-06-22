<template>
  <div class="index">
    <!--变化检测-->
    <!-- 表头   -->

    <!-- 侧边栏-->
    <div class="aside_down">

      <!-- 功能选择框 -->
      <div class="choice_box">
        <div class="choice" style="background:radial-gradient(rgb(60, 66, 74) 0%,rgb(38, 109, 215) 100%)">
          <img :src="picfive" class="choice_pic" />
          <h4 style="font-weight: 500">通用变化检测</h4>
        </div>
      </div>

      <!-- 分割线 -->
      <div style="width: 94%; height: 10px; margin-left: 3%">
        <hr style="border: 0.3px solid grey" />
      </div>

      <!-- 示例数据 -->
      <h4 style="color: white; font-weight: 400; margin-top: 10px">示例数据</h4>
      <img :src="src" class="example" />
    </div>

    <div class="el_main">
      <!--  style控制图片渲染的范围  -->
      <canvas id="layer" :width="canvasWidth" :height="canvasHeight"></canvas>

      <!-- 按钮 -->
      <div class="buttons">
        <el-tooltip class="item" effect="dark" content="框选" placement="top">
          <el-button icon="el-icon-search" circle @click="rectImage"></el-button>
        </el-tooltip>

        <el-tooltip
          class="item"
          effect="dark"
          content="运行推理"
          placement="top"
        >
          <el-button icon="el-icon-video-play" circle @click="run"></el-button>
        </el-tooltip>

        <el-tooltip
          class="item"
          effect="dark"
          content="取消选框"
          placement="top"
        >
          <el-button icon="el-icon-close" circle @click="rectCancel"></el-button>
        </el-tooltip>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { getImages } from "../../api/apiRequest";

import picfive from "./pic/tool3.svg";

export default {
  name: "change_detection",
  data() {
    return {
      canvasWidth: 1096, // 画布大小
      canvasHeight: 694,
      imageData: [], // 列表显示的数据
      imgList: [],
      myCanvas: null,
      ctx: null,
      imgObject: [],
      imgX: 0, // 图片在画布中渲染的起点x坐标
      imgY: 0,
      imgScale: 0.1, // 图片的缩放大小
      rectflag: false, // 框选标志位
      rectangles: [], // 框选的参数
      pos: {}, // 存储点击鼠标坐标
      rate: {}, // 框选的位置在图片的比例
      pictureSize: {}, // 图片的尺寸
      dialog: false,
      loading: false,
      dialogImageUrl: "",
      dialogVisible: false,
      disabled: false,
      formLabelWidth: "80px",
      timer: null,
      fullscreenLoading: false,
      src: "http://127.0.0.1:8000/media/pictures/b54410e4d8.png",
      picfive: picfive,
    };
  },
  mounted() {
    this.layer = document.getElementById("layer");
    this.ctx = this.layer.getContext("2d");
    this.loadImages(); // 加载图片块
  },
  methods: {
    loadImages() {
      var _this = this;
      getImages().then(res => {
        _this.imageData = res.data;
        // 数据库查找图片
        for (var i = 0; i < _this.imageData.length; i++) {
          if (_this.imageData[i].name == "示例数据") {
            // console.log(_this.imageData[i]);
            _this.imgList.push(_this.imageData[i].image_url);
          }
        }
        _this.preImg(); // 图片拼接
      });
    }, // 加载图片块
    preImg() {
      // console.log("开始加载")
      var _this = this,
        imgList = _this.imgList;
      let length = imgList.length;
      var imageList = [];
      var count = 0;
      if (length > 1) {
        for (let key = 0; key < length; key++) {
          var item = imgList[key];
          var extraImg = new Image(); // 创建画布
          extraImg.src = item;
          var x = extraImg.src.match(/[0-9]+/g)[6],
            y = extraImg.src.match(/[0-9]+/g)[5]; // 图片的行列

          imageList.push({
            img: extraImg,
            x: (x - 1) * 1024,
            y: (y - 1) * 1024,
            width: 1024,
            height: 1024
          }),
            count++;
          // 图片信息添加完毕
          if (count >= length) {
            extraImg.onload = function() {
              _this.imgObject = imageList;
              _this.drawImage(imageList);
            };
          }
        }
        // console.log(imageList);
      } else {
        _this.imgObject = imageList;
        _this.drawImage(imageList);
      }
    }, // 图片拼接
    drawImage(imageList) {
      var _this = this;
      _this.ctx.clearRect(0, 0, this.canvasWidth, this.canvasHeight);
      for (var i = 0; i < imageList.length; i++) {
        _this.ctx.drawImage(
          imageList[i].img, //规定要使用的图片
          _this.imgX + imageList[i].x * _this.imgScale,
          _this.imgY + imageList[i].y * _this.imgScale, //在画布上放置图像的 x 、y坐标位置。
          imageList[i].width * _this.imgScale,
          imageList[i].height * _this.imgScale //要使用的图像的宽度、高度
        );
      }
      _this.canvasEventsInit(); // 图片移动
      _this.canvasMouseWheel(); // 图片缩放操作
    }, // 图片加载
    rectar(x, y, width, height) {
      this.x = x;
      this.y = y;
      this.width = width;
      this.height = height;
    }, // 定义矩形框
    drawRect() {
      var _this = this;
      var rect = _this.rectangles[_this.rectangles.length - 1]; // 取数组最后一个元素
      _this.ctx.beginPath();
      _this.ctx.clearRect(rect.x, rect.y, rect.width, rect.height); // 清除前一元素
      _this.drawImage(_this.imgObject); //重新绘制图片
      _this.ctx.strokeStyle = "#00ff00"; // 设置线条颜色，必须放在绘制之前
      _this.ctx.lineWidth = 3; // 线宽设置，必须放在绘制之前-->
      _this.ctx.strokeRect(rect.x, rect.y, rect.width, rect.height); // 矩形绘制
    }, // 绘制矩形
    rectImage() {
      var _this = this;
      _this.rectflag = true;
    }, // 框选图片
    run() {
      var _this = this;
      var rect = _this.rectangles[_this.rectangles.length - 1]; // 取数组最后一个元素

      var params = {
        name: "示例数据",
        x1: rect.x - _this.imgX,
        y1: rect.y - _this.imgY,
        x2: rect.x - _this.imgX + rect.width,
        y2: rect.y - _this.imgY + rect.height,
        scale: _this.imgScale
      };

      axios.post("http://127.0.0.1:8000/api/pic/result/", params).then(res => {
        console.log(res);
      });
    }, // 进行框选区域图片推理
    rectCancel() {
      var _this = this;
      _this.rectangles.length = 0;
      _this.drawImage(_this.imgObject); //重新绘制图片
    }, // 取消框选的区域
    canvasEventsInit() {
      var _this = this,
        canvas = _this.layer;
      canvas.onmousedown = function(e) {
        var imgx = _this.imgX,
          imgy = _this.imgY;
        var pos = {
          x: e.clientX - canvas.offsetLeft,
          y: e.clientY - canvas.offsetTop
        }; //鼠标点击坐标
        console.log(pos.x,pos.y);
        _this.pos = pos;
        canvas.onmousemove = function(e) {
          var movenumber = {
            x: e.clientX - canvas.offsetLeft - pos.x,
            y: e.clientY - canvas.offsetTop - pos.y
          };

          if (_this.rectflag) {
            if (movenumber.x && movenumber.y) {
              var x = pos.x - 425,
                y = pos.y - 60,
                width = movenumber.x,
                height = movenumber.y; // 选框的参数
              var rectangle = new _this.rectar(x, y, width, height); // 创建一个新的矩形对象
              _this.rectangles.push(rectangle); // 将矩形对象保存在数组中
              _this.drawRect(); // 绘制矩形
            }
          } else {
            canvas.style.cursor = "move"; // 移动标识
            var x = movenumber.x + imgx,
              y = movenumber.y + imgy; // 图像渲染的起始点坐标
            (_this.imgX = x), (_this.imgY = y); // 渲染图象的位置
            _this.drawImage(_this.imgObject); //重新绘制图片
          }
        };
        canvas.onmouseup = function(e) {
          canvas.onmousemove = null;
          canvas.style.cursor = "default"; // 默认标识
          _this.rectflag = false;
        };
      };
    }, // 鼠标监听
    canvasMouseWheel() {
      var _this = this,
        canvas = _this.layer;
      canvas.onmousewheel = canvas.onwheel = function(event) {
        //滚轮放大缩小
        var wheelDelta = event.wheelDelta
          ? event.wheelDelta
          : event.deltalY * -40; //获取当前鼠标的滚动情况
        if (wheelDelta > 0) {
          _this.imgScale *= 1.1;
          // _this.rectScale *= 1.1;
        } else {
          if (_this.imgScale > 0.1) {
            _this.imgScale *= 0.9;
            // _this.rectScale *= 0.9;
          }
        }
        event.preventDefault && event.preventDefault(); // 阻止页面的点击菜单栏
        _this.drawImage(_this.imgObject); //重新绘制图片
        return false;
      };
    } // 鼠标滚轮
  }
};
</script>

<style scoped>
.template {
  width: 100%;
  height: 100%;
}
.el-header {
  color: rgb(85, 82, 82);
  text-align: center;
  line-height: 60px;
}
.el_aside {
  color: #333;
  text-align: center;
  height: 100%;
}
.el_main {
  position: absolute;
  top: 60px;
  left: 440px;
  background-color: rgb(14, 14, 17);
  text-align: center;
  display: inline-block;
  justify-content: center;
  align-items: center;
  /* height: 694px; */
  width: 1096px;
  padding-bottom: auto;
  padding-top: auto;
}
</style>
<style>
* {
  margin: 0;
  padding: 0;
}
.more {
  height: 400px;
}
.choice {
  margin-left: 18px;
  margin-right: 18px;
  color: white;
  height: 110px;
  width: 170px;
  border-radius: 6px;
  
}
.choice_box {
  margin-top: 30px;
  display: flex;
  flex-wrap: wrap;
  margin-bottom: 30px;
  margin-left: auto;
  margin-right: auto;
  padding-left: 10px;
}
.choice_pic {
  height: 65px;
  margin-top: 6px;
}
.example {
  height: 150px;
  width: 300px;
  margin-top: 23px;
  border: 2px rgb(38, 109, 215) solid;
}
/*侧边栏那一块*/
.aside_down {
  width: 440px;
  background-color: #333;
  text-align: center;
  height: 694px;
  margin-top: -5px;
}
</style>
