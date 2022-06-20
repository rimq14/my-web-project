<template>
  <div class="index">
<!--目标提取-->
    <!-- 表头   -->
   
      <!-- 侧边栏-->
      <div class="aside_down"><!--原来是el-aside-->
        
        <div class="choice_box">
          <div class="choice" @click="blue1"
            style="background:radial-gradient(rgb(60, 66, 74) 0%,rgb(38, 109, 215) 100% )">
            <img :src="picfour" class="choice_pic" />
            <h4 style="font-weight:500">地物分类</h4>
          </div>
          
        </div>
        <div style="width:94%;height:10px;margin-left: 3%;">
          <hr style="border:0.3px solid  grey;" />

        </div>

        <h4 style="color:white;font-weight: 400;margin-top: 10px;">示例数据</h4>
        <img :src="example" class="example" />

      </div>

   
      <div class="el_main">  
        <div class="photobox">
          <img :src="example" class="more" />
        </div>
       </div> 
    

  </div>
</template >

<script>
import picfour from "./pic/tool1.svg"

import example from "./pic/example.jpg"

export default {
  name: "object_classification",
  data() {
    return {
      activeIndex: '1',
      src: 'http://127.0.0.1:8000/media/pictures/82d8c7c349.png',
      picfour: picfour,
      example: example

    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
    blue1() {
      const choices = document.querySelectorAll(".choice");
      choices[0].style.background = "radial-gradient(rgb(60, 66, 74) 0%,rgb(38, 109, 215) 100%)"
      choices[1].style.background = "rgb(60, 66, 74)";
      choices[2].style.background = "rgb(60, 66, 74)";
    },
    blue2() {
      const choices = document.querySelectorAll(".choice");
      choices[1].style.background = "radial-gradient(rgb(60, 66, 74) 0%,rgb(38, 109, 215) 100%)"
      choices[0].style.background = "rgb(60, 66, 74)";
      choices[2].style.background = "rgb(60, 66, 74)";
    },
    blue3() {
      const choices = document.querySelectorAll(".choice");
      choices[2].style.background = "radial-gradient(rgb(60, 66, 74) 0%,rgb(38, 109, 215) 100%)"
      choices[1].style.background = "rgb(60, 66, 74)";
      choices[0].style.background = "rgb(60, 66, 74)";
    },
  }
}
</script>
<style scoped>
.template {
  width: 100%;
  height: 100%
}
.el-header {
  color: rgb(85, 82, 82);
  text-align: center;
  line-height: 60px;
}

.el_main {
  position: absolute;
  top:60px;
  left:440px;
  background-color: rgb(14, 14, 17);
  text-align: center;
  display: inline-block;
  justify-content: center;
  align-items: center;
  height: 694px;
  width:1096px;
 
 }.photobox{
  margin-top: 150px;
  }
</style>
<style >
*{
  margin:0;
  padding:0;
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
  background-color: rgb(60, 66, 74);
}.choice_box {
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
  height: 170px;
  margin-top: 23px;
  border: 2px rgb(38, 109, 215) solid;
}
/*侧边栏那一块*/
.aside_down{
  width:440px;
  background-color:  #333;
  text-align: center;
  height: 614px;
  margin-top: -5px;
  
}


</style>
