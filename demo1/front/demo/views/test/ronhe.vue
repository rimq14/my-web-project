<template>
  <div class="root">
    <div class="mycanvas">
      <canvas id="layer" :width="canvasWidth" :height="canvasHeight"
        :style="'width:'  + '100%;height:' + '100%;'"></canvas>
    </div>
    <div>
      <button @click="preImg">处理</button>
    </div>
  </div>
</template>

<script>
import { getPic,postId } from '../../api/apiRequest';


export default {
  name: 'laborImage',
  components: {},
  data() {
    return {
      canvasWidth: 2400, // 画布大小
      canvasHeight: 1400,
      imgList: [],
      myCanvas: null,
      ctx: null,
      imgObject: [],
      imgX: 200, // 图片在画布中渲染的起点x坐标
      imgY: 100,
      imgScale: 0.1, // 图片的缩放大小
    }
  },
  mounted() {
    this.myCanvas = document.getElementById('layer');
    this.ctx = this.myCanvas.getContext('2d');
    this.loadImg();
    this.canvasEventsInit();
  },
  methods: {
    loadImg() {
      getPic().then(res => {
        this.imgList = res.data
      })
    },  // 加载分块图片
    preImg() {
      var _this = this, imgList = _this.imgList;
      let length = imgList.length;
      var imageList = [];
      var count = 0;
      if (length > 1) {
        for (let key = 0; key < length; key++) {
          var item = imgList[key];
          var extraImg = new Image();   // 创建画布
          extraImg.src = item.image_url;
          var x = extraImg.src.match(/[0-9]+/g)[6], y = extraImg.src.match(/[0-9]+/g)[5];   // 图片的行列
          imageList.push({ img: extraImg, x: (x - 1) * 1024, y: (y - 1) * 1024, width: 1024, height: 1024 }), count++;
          // 图片信息添加完毕
          if (count >= length) {
            extraImg.onload = function () {
              _this.imgObject = imageList;
              _this.drawImage(imageList);
            }
          }
        }
      } else {
        _this.imgObject = imageList;
        _this.drawImage(imageList);
      }
    },
    drawImage(imageList) {
      var _this = this;
      _this.ctx.clearRect(0, 0, this.canvasWidth, this.canvasHeight);
      for (var i = 0; i < imageList.length; i++) {
        _this.ctx.drawImage(
          imageList[i].img, //规定要使用的图片
          _this.imgX + imageList[i].x * _this.imgScale,
          _this.imgY + imageList[i].y * _this.imgScale,//在画布上放置图像的 x 、y坐标位置。
          imageList[i].width * _this.imgScale,
          imageList[i].height * _this.imgScale //要使用的图像的宽度、高度
        );
      }
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
        var pos = { x: event.clientX, y: event.clientY };  //坐标转换，将窗口坐标转换成canvas的坐标
        canvas.onmousemove = function (evt) {  //移动
          canvas.style.cursor = 'move';
          var x = (evt.clientX - pos.x) * 2 + imgx;
          var y = (evt.clientY - pos.y) * 2 + imgy;
          _this.imgX = x;
          _this.imgY = y;
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
          if (_this.imgScale > 0.1) {
            _this.imgScale *= 0.9;
          }
        }
        _this.drawImage(_this.imgObject);   //重新绘制图片
        event.preventDefault && event.preventDefault();
        return false;
      };
    },
  },
}
</script>
