<template>
  <div class="divbody">
    <div class="imgContainer" ref="imgContainer">
      <canvas
        :width="canvasWidth"
        :height="canvasHeight"
        class="canvasClass"
        @mousedown=""
        @mousemove="drawCurrentRect"
        @mouseup="stopDrawing"
        @mouseout="stopDrawing"
        ></canvas>
      <img
        :id="image"
        :src="imageSrc"
        :ref="'refimage'"
        class="imgClass"
        @load="uploadImgLoad"

        />
      </div>
    </div>
</template>

<script>
export default {
  name: "area-invade",
  props: {},
  data() {
    return {
      // canvas的像素大小
      canvasWidth: 0,
      canvasHeight: 0,
      // 记录矩形的坐标
      ractTarget: [],
      // 记录图片的左上角坐标
      imgX: 0,
      imgY: 0,
      // 是否正在绘制
      isDrawing: false,
      // 绘图上下文对象
      canvasContext: null,
      // 右边的canvas上下文
      newCanvasContext: null,
    };
  },
  mounted() {
    // 初始化canvas
    this.initCanvas();
    // 如果窗口大小改变了，那么canvas宽高重新计算
    window.onresize = () => {
      this.initCanvas();
    }
  },
  beforeDestroy() {
    window.onresize = null
  },
  methods: {
    // 初始化
    initCanvas() {
      // 读取图片的大小，赋值给canvas的宽高
      const el = document.querySelector(".img-box");
      this.canvasWidth = el.getBoundingClientRect().width;
      this.canvasHeight = el.getBoundingClientRect().height;
      // 记录图片左上角在页面的位置，方便计算坐标
      this.imgX = el.getBoundingClientRect().left;
      this.imgY = el.getBoundingClientRect().top;
      // 清空点数组
      this.ractTarget = []
    },
    // 鼠标按下，开始画图
    startDrawing(e) {
      // 如果还没有获取矩形，那就去获取起点坐标
      if (this.ractTarget.length == 0) {
        this.getStartPoint(e);
      } else {
        this.$confirm("确定要重新框选区域吗?", "提示", {
          confirmButtonText: "确定",
          cancelButtonText: "取消",
          type: "warning",
        })
          .then(() => {
            // 如果确认要重新画，就清空坐标数组和画布
            this.ractTarget = [];
            if (!this.canvasContext) {
              this.canvasContext = document
                .getElementById("myCanvas")
                .getContext("2d");
            }
            this.canvasContext.clearRect(0, 0, this.canvasWidth, this.canvasHeight);
            this.newCanvasContext.clearRect(0, 0, this.canvasWidth, this.canvasHeight);
          })
          .catch(() => {});
      }
    },
    // 获取起点坐标
    getStartPoint(e) {
      this.isDrawing = true;
      const point = {
        x: Math.floor(e.pageX - this.imgX),
        y: Math.floor(e.pageY - this.imgY),
      };
      // 记录到矩形坐标数组
      this.ractTarget.push(point);
    },
    // 鼠标移动，绘制当前的矩形
    drawCurrentRect(e) {
      // 确认当前正在绘制
      if (this.isDrawing) {
        // 清空掉除了第一个以外的其他元素
        while (this.ractTarget.length > 1) {
          this.ractTarget.pop();
        }
        // 获取鼠标当前相对于canvas的坐标
        const point = {
          x: Math.floor(e.pageX - this.imgX),
          y: Math.floor(e.pageY - this.imgY),
        };
        // 根据起点坐标和当前坐标，计算出矩形的宽高
        const rectWidth = Math.abs(point.x - this.ractTarget[0].x);
        const rectHeight = Math.abs(point.y - this.ractTarget[0].y);
        // 如果组成的矩形宽高不为0，那就计算一下4个点的坐标
        if (rectWidth > 0 && rectHeight > 0) {
          // 第二个点的x跟起点一致，y跟当前点的一致
          this.ractTarget.push({
            x: this.ractTarget[0].x,
            y: point.y,
          });
          // 第三个点坐标就是当前点的坐标
          this.ractTarget.push(point);
          // 第四个点的x跟当前点的一致，y跟起点的一致
          this.ractTarget.push({
            x: point.x,
            y: this.ractTarget[0].y,
          });
          // 绘制矩形
          this.drawDashedRect(this.ractTarget);
        }
      }
    },
    // 在左边canvas绘制虚线矩形
    drawDashedRect() {
      if (!this.canvasContext) {
        this.canvasContext = document
          .getElementById("myCanvas")
          .getContext("2d");
      }
      // 绘制矩形
      this.drawRect(this.canvasContext, "#36A9CE", 4, this.ractTarget, true);
    },
    // 停止绘图
    stopDrawing() {
      this.isDrawing = false;
    },
    // 点击钩，保存刚才选的矩形
    saveRect() {
      // 获取右边canvas的上下文对象
      if (!this.newCanvasContext) {
        this.newCanvasContext = document
          .getElementById("new-canvas")
          .getContext("2d");
      }
      // 绘制红色的矩形
      this.drawRect(
        this.newCanvasContext,
        "#F32329",
        4,
        this.ractTarget,
        false
      );
    },
    // 抽象一个绘制矩形的函数，参数为context，颜色，粗细，坐标数组，是否虚线
    drawRect(context, color, lineWidth, pointList, isDashed) {
      // 设置线条的粗细和颜色
      context.strokeStyle = color;
      context.lineWidth = lineWidth;
      // 设置虚线
      if (isDashed) {
        context.setLineDash([10, 5]);
      }
      // 清空之前的画布
      context.clearRect(0, 0, this.canvasWidth, this.canvasHeight);
      context.beginPath();
      // 根据矩形坐标数据，把矩形绘制出来
      context.moveTo(pointList[0].x, pointList[0].y);
      for (let i = 1; i <= pointList.length - 1; i++) {
        context.lineTo(pointList[i].x, pointList[i].y);
      }
      context.closePath();
      context.stroke();
    },
  },
};
</script>

<style scoped>
.form {
  height: 280px;
  position: relative;
  padding: 0 20px;
}

.form-box ::v-deep .form-btns {
  padding: 70px;
  text-align: center;
  .el-button {
    margin: 0 20px;
  }
}

.img-area.left {
  float: left;
}

.img-area.right {
  float: right;
}

/* 显示图片区域*/
.img-area {
  position: relative;
  padding-top: 20px;
  width: 42%;
  .label {
    font-size: 14px;
    line-height: 3;
  }
  .img-box {
    position: relative;
  }
  .img {
    width: 100%;
  }
  // canvas绝对定位，盖在图片上方，这里的z-indext如果没有设置，则canvas无法使用
  .canvas {
    position: absolute;
    top: 0;
    left: 0;
    z-index: 1;
  }
}

.tick {
  position: absolute;
  width: 16%;
  left: 42%;
  padding-top: 160px;
  text-align: center;
  font-size: 24px;
  color: #70b948;
}
</style>
