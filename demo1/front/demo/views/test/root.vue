<template>
  <div class="test" style="background-color: burlywood;">
    <canvas id="myCanvas" ref="myCanvas"
            width="460" height="240" @mousedown="mousedown" @mouseup="mouseup" @mousemove="mousemove">
    </canvas>
  </div>
</template>

<script>
  export default {
    name:"hello-world",
    data() {
      return {
        flag: false,
        x: 0,
        y: 0
      };
    },
    watch: {},
    computed: {},
    methods: {
      mousedown(e){
        console.log("鼠标落下");
        this.flag = true;
        this.x = e.offsetX; // 鼠标落下时的X
        this.y = e.offsetY; // 鼠标落下时的Y
      },
      mouseup(e){
        console.log("鼠标抬起");
        this.flag = false;
      },
      mousemove(e){
        console.log("鼠标移动");
        this.drawRect(e);
      },
      drawRect(e){
        if(this.flag){
          console.log("绘制图形");
          const canvas = this.$refs.myCanvas;
          var ctx = canvas.getContext("2d");
          let x = this.x;
          let y = this.y;

          ctx.clearRect(0,0,canvas.width,canvas.height);
          ctx.beginPath();

          //设置线条颜色，必须放在绘制之前
          ctx.strokeStyle = '#00ff00';
          // 线宽设置，必须放在绘制之前
          ctx.lineWidth = 1;

          ctx.strokeRect(x,y,e.offsetX-x,e.offsetY-y);
        }
      }
    },
    created() {

    },
    mounted() {

    }
  };
</script>

<style scoped>
  #myCanvas{
    background-color: forestgreen;
  }
</style>
