<template>
  <div class="root">
    <div class="mycanvas">
    <canvas
          id="myCanvas"
          :width="canvasWidth"
          :height="canvasHeight"
          :style="'width:'+canvasWidth/2+'px;height:'+canvasHeight/2+'px;'"
    ></canvas>
    </div>
    <div class="table">
            <!-- 表格-->
            <el-table
              :data="extraimg"
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
                    @click="loadImg(scope.row.img)">加载
                  </el-button>
                </template>
              </el-table-column>
            </el-table>
    </div>
  </div>
</template>

<script>
import {getPic} from "../../api/apiRequest";

export default {
    name: 'ronhe1',
    components: {},
    data() {
      return {
        canvasWidth: 2400, // 画布大小
        canvasHeight: 1400,
        extraimg: [],
        myCanvas: null,
        ctx: null,
        imgObject: [],
        imgX: 0, // 图片在画布中渲染的起点x坐标
        imgY: 0,
        imgScale: 0.1, // 图片的缩放大小
      }
    },
    mounted() {
      this.loadinfo();
       this.myCanvas = document.getElementById("myCanvas");
       this.ctx = this.myCanvas.getContext('2d');
      // this.loadImg();
      this.canvasEventsInit();
    },
    methods: {
      loadinfo(){
        getPic().then(res => {
          this.extraimg = res.data
        })
      },
      loadImg(img) {
        var _this = this;
        var image = new Image();
        image.src = img


        image.onload = function () {
          _this.imgObject = image;
          _this.drawImage(image);   // 加载图片
        }
      },
      drawImage(image) {
        var _this = this;
        _this.ctx.clearRect(0, 0, this.canvasWidth, this.canvasHeight);
          _this.ctx.drawImage(
            image, //规定要使用的图片,此处为链接
            _this.imgX + image.x * _this.imgScale,
            _this.imgY+ image.y * _this.imgScale,//在画布上放置图像的 x 、y坐标位置。
            image.width*_this.imgScale,
            image.height*_this.imgScale //要使用的图像的宽度、高度
          );
        },
      /**
       * 为画布上鼠标的拖动和缩放注册事件
      */
      canvasEventsInit() {
        var _this = this;
        var canvas = _this.myCanvas;

        canvas.onmousedown = function (event) {
          var imgx = _this.imgX;
          var imgy = _this.imgY;
          var pos = {x:event.clientX, y:event.clientY};  //坐标转换，将窗口坐标转换成canvas的坐标
          canvas.onmousemove = function (evt) {  //移动
            canvas.style.cursor = 'move';

            var x = (evt.clientX - pos.x) * 2 + imgx;
            var y = (evt.clientY - pos.y) * 2 + imgy;
            _this.imgX  = x;
            _this.imgY  = y;
            _this.drawImage(_this.imgObject);  //重新绘制图片
          };

          canvas.onmouseup = function () {
            canvas.onmousemove = null;
            canvas.onmouseup = null;
            canvas.style.cursor = 'default';
          };
        };

        canvas.onmousewheel = canvas.onwheel = function (event) {    //滚轮放大缩小
          var wheelDelta = event.wheelDelta ? event.wheelDelta : (event.deltalY * (-40));  //获取当前鼠标的滚动情况
          if (wheelDelta > 0) {
              _this.imgScale *= 1.1;
          } else {
              if(_this.imgScale > 0.1) {
                 _this.imgScale *= 0.9;
              }
          }
          _this.drawImage(_this.imgObject);   //重新绘制图片
          event.preventDefault  && event.preventDefault();  // 阻止页面的点击菜单栏
          return false;
        };
      },
    },
  }
</script>

<style scoped>
.mycanvas {
  background-color: green;
}
</style>

<!--drawRect(){-->
<!--        var _this = this;-->
<!--          if (_this.flag) {-->
<!--            let x = _this.x;-->
<!--            let y = _this.y;-->

<!--            _this.context.clearRect(0, 0, this.canvasWidth, this.canvasHeight);-->
<!--            _this.context.beginPath();-->
<!--            //设置线条颜色，必须放在绘制之前-->
<!--            _this.context.strokeStyle = '#00ff00';-->
<!--            // 线宽设置，必须放在绘制之前-->
<!--            _this.context.lineWidth = 1;-->
<!--            _this.context.strokeRect(x, y, this.w, this.h);   // 矩形绘制-->
<!--          }-->
<!--        },  // 绘制矩形-->
<!--      rectImage() {-->
<!--        var _this = this;-->
<!--        var canvas = _this.rectCanvas;-->
<!--        console.log("kuangxuan ")-->
<!--        _this.dragflag = false;   // 禁止图片移动等操作-->
<!--        _this.canvasEventsInit(); // 禁用鼠标移动-->

<!--        // console.log(_this.dragflag);  // 查看标志位状态-->

<!--        canvas.onmousedown = function (e) {-->
<!--          console.log("点击")-->
<!--          _this.flag = true;-->
<!--          var position = {x: e.offsetX, y: e.offsetY};  // 鼠标点击的坐标-->
<!--          _this.x = position.x;-->
<!--          _this.y = position.y;-->

<!--          canvas.onmousemove = function (eve) {-->
<!--          var width = eve.offsetX - position.x, height = eve.offsetY - position.y;    // 矩形的宽度和高度-->
<!--            _this.w = width;-->
<!--            _this.h = height;-->
<!--          _this.drawRect();-->
<!--           };-->

<!--          canvas.onmouseup = function (e) {-->
<!--            _this.flag = false;-->
<!--            _this.dragflag = true;-->
<!--            _this.canvasEventsInit();-->
<!--          };-->
<!--        };-->
<!--    loading(img) {-->
<!--      var image = new Image();-->
<!--      image.src = img;-->
<!--      var content = document.getElementById("myCanvas").getContext("2d");   // 查找特定元素-->

<!--      let boxWidth, boxHeight;-->
<!--      let rows = 20,-->
<!--        columns = 20,-->
<!--        counter = 0;-->

<!--      image.onload = function () {-->
<!--        boxWidth = image.width / columns;-->
<!--        boxHeight = image.height / rows;-->
<!--        window.requestAnimationFrame(animate);   // 告诉浏览器你希望执行一个动画-->
<!--      };-->

<!--      function animate() {-->
<!--        let x = Math.floor(Math.random() * columns);-->
<!--        let y = Math.floor(Math.random() * rows);-->
<!--        content.drawImage(-->
<!--          image,-->
<!--          x * boxWidth, // 横坐标起始位置-->
<!--          y * boxHeight, // 纵坐标起始位置-->
<!--          boxWidth, // 图像的宽-->
<!--          boxHeight, // 图像的高-->

<!--          x * boxWidth, // 在画布上放置图像的 x 坐标位置-->
<!--          y * boxHeight, // 在画布上放置图像的 y 坐标位置-->
<!--          boxWidth, // 要使用的图像的宽度-->
<!--          boxHeight // 要使用的图像的高度-->
<!--        );-->
<!--        counter++;-->
<!--        if (counter > columns * rows * 0.9) {-->
<!--          content.drawImage(image, 0, 0);-->
<!--        } else {-->
<!--          requestAnimationFrame(animate);-->
<!--        }-->
<!--      }-->
<!--    },    // 加载图片-->

