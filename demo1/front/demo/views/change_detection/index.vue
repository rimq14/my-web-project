<template>
  <div>
    <canvas
      id="myCanvas"
      width="1200"
      height="800"
      style="display: block;"
    ></canvas>
    <el-button @click="qg">切割图片</el-button>
  </div>
</template>

<script>
export default {
  name: "index",
  methods:{
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

<style scoped>

</style>
