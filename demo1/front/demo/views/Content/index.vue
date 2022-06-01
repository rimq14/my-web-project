<template>
  <div class="index">

    <div class="header">
      <div class="header_left">
        <h4 style="font-weight: 350; font-size: 15px;"  @mouseover="change1()" @mouseleave="changeback1()" class="b1">数据检索</h4>
        <h4 style="font-weight: 350; font-size: 15px; color:#3a70c1;">处理分析</h4>
        <h4 style="font-weight: 350; font-size: 15px;"  @mouseover="change2()" @mouseleave="changeback2()" class="b2">模型训练</h4>
      </div>
      <div class="header_right">
        <h5 style="font-size: 10px; font-weight: 350;">✉ 我的数据</h5>
        <h5 style="font-size: 10px; font-weight: 350;">✈ 帮助文档</h5>
        <h5 style="font-size: 10px; font-weight: 350;">✿ 使用反馈</h5>
        <img src="../Experience/pic/lingdang.svg" class="pto1">
        <img src="../Experience/pic/ding.svg" class="pto1">
        <img src="../Experience/pic/people.svg" class="pto2">
      </div>

    </div>
    <div class="main">
      <h1 style="color:white;text-align: center;font-size: 28px;font-weight: 400;margin-bottom: 18px;">功 能 选 择</h1>
      <hr style="border-top:0;border-bottom:1px solid grey">
      <div class="prompt">
        <button class="pro1" style="display:inline-block; font-size: 14px;font-weight:bolder;"> AI翻译</button>
        <button class="pro2" style="display:inline-block; font-size: 14px;font-weight:bolder;"> 基础处理</button>
        <button class="pro3" style="display:inline-block; font-size: 14px;font-weight:bolder;">新建处理分析项目</button>
      </div>
      <div class="tools">
        <router-link :to="{ path: '/change_detection' }" class="btn btn-primary" role="button" target="_blank">
        <div class="tool">
          <img :src="tool1" class="tool_pic" />
          <h4 style="font-size:15px;font-weight:500">变化检测</h4>
        </div></router-link>

         <router-link :to="{ path: '' }" class="btn btn-primary" role="button" target="_blank">
        <div class="tool">
          <img :src="tool2" class="tool_pic" />
          <h4 style="font-size:15px;font-weight:500">目标提取</h4>
        </div></router-link>

        <router-link :to="{ path: '' }" class="btn btn-primary" role="button" target="_blank">
        <div class="tool">
          <img :src="tool3" class="tool_pic" />
          <h4 style="font-size:15px;font-weight:500">目标检测</h4>
        </div></router-link>

        <router-link :to="{ path: '' }" class="btn btn-primary" role="button" target="_blank">
        <div class="tool">
          <img :src="tool4" class="tool_pic" />
          <h4 style="font-size:15px;font-weight:500">地物分类</h4>
        </div></router-link>
        <div class="tool">
          <img :src="tool5" class="tool_pic" />
          <h4 style="font-size:15px;font-weight:500">建筑物变化检测</h4>
        </div>
        <div class="tool">
          <img :src="tool6" class="tool_pic" />
          <h4 style="font-size:15px;font-weight:500">耕地变化检测</h4>
        </div>
        <div class="tool">
          <img :src="tool7" class="tool_pic" />
          <h4 style="font-size:15px;font-weight:500">建筑物提取</h4>
        </div>
        <div class="tool">
          <img :src="tool8" class="tool_pic" />
          <h4 style="font-size:15px;font-weight:500">大棚提取</h4>
        </div>
        <div class="tool">
          <img :src="tool9" class="tool_pic" />
          <h4 style="font-size:15px;font-weight:500">地块提取</h4>
        </div>
        <div class="tool">
          <img :src="tool10" class="tool_pic" />
          <h4 style="font-size:15px;font-weight:500">光伏电厂提取</h4>
        </div>
        <div class="tool">
          <img :src="tool11" class="tool_pic" />
          <h4 style="font-size:15px;font-weight:500">拦河坝提取</h4>
        </div>
        <div class="tool">
          <img :src="tool12" class="tool_pic" />
          <h4 style="font-size:15px;font-weight:500">去雾处理</h4>
        </div>
      </div>
      <div class="bye">
        <h4 style="font-size:15px;font-weight:500;
        color:grey; margin-top:10px;margin-left:370px">更多AI解译能力，敬请期待</h4>

      </div>


    </div>
  </div>

</template>

<script>
import tool1 from "../Experience/pic/tool1.svg"
import tool2 from "../Experience/pic/tool2.svg"
import tool3 from "../Experience/pic/tool3.svg"
import tool4 from "../Experience/pic/tool4.svg"
import tool5 from "../Experience/pic/tool5.svg"
import tool6 from "../Experience/pic/tool6.svg"
import tool7 from "../Experience/pic/tool7.svg"
import tool8 from "../Experience/pic/tool8.svg"
import tool9 from "../Experience/pic/tool9.svg"
import tool10 from "../Experience/pic/tool10.svg"
import tool11 from "../Experience/pic/tool11.svg"
import tool12 from "../Experience/pic/tool12.svg"
export default {
  name: "index",
  data() {
    return {
      tool1: tool1,
      tool2: tool2,
      tool3: tool3,
      tool4: tool4,
      tool5: tool5,
      tool6: tool6,
      tool7: tool7,
      tool8: tool8,
      tool9: tool9,
      tool10: tool10,
      tool11: tool11,
      tool12: tool12,

    };
  },
  methods: {
  change1() {
      const b1 = document.querySelector(".b1");
      b1.style.color="#3a70c1";
    },
    changeback1() {
      const b1 = document.querySelector(".b1");
      b1.style.color="white";
    },
    change2() {
      const b2 = document.querySelector(".b2");
      b2.style.color="#3a70c1";
    },
    changeback2() {
      const b2 = document.querySelector(".b2");
      b2.style.color="white";
    },
   
  }
}
</script>
<style scoped>
.el-header {
 color: #333;
  text-align: center;
  line-height: 60px;
}

.index {
  background-color: rgb(27, 27, 29);
  height: 754px;
}
</style>
<style >
* {
  margin: 0;
  padding: 0;
}

.header {
  height: 60px;
  width: 100%;
  background-color: rgb(52, 52, 52);
}

.header_left {
  height: 60px;
  width: 300px;
  margin-left: 130px;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  color: white;
  text-align: center;
  line-height: 60px;
}

.header_right {
  color: white;
  height: 60px;
  width: 350px;
  display: flex;
  flex-direction: row;
  position: absolute;
  align-items: center;
  top: 0;
  right: 0;
  justify-content: space-between;
  margin-right: 20px;
  color: rgb(194, 190, 190);
}

.pto1 {
  height: 17px;
}

.pto2 {
  height: 32px;
}

.main {
  height: 650px;
  width: 60%;
  margin-top: 30px;
 margin-left: auto;
  margin-right: auto;
}

.prompt {
  height: 35px;
  width: 95%;
  margin-left: auto;
  margin-right: auto;
  margin-top: 18px;
}

.pro1 {
  width: 160px;
  height: 35px;
  text-align: center;
  line-height: 35px;
  background-color: rgb(157, 159, 158);
  color:white;
  border-radius: 4px;
  border:0;
}

.pro2 {
  width: 160px;
  height: 35px;
  text-align: center;
  line-height: 35px;
  background-color: rgb(54, 52, 52);
  color:rgb(189, 188, 187);
  margin-left: -5px;
  border-radius: 4px;
  border:0;
}

.pro3 {
  float: right;
  width: 160px;
  height: 35px;
  text-align: center;
  line-height: 35px;
  background-color: rgb(51, 120, 232);
  color:white;
  margin-left: -5px;
  border-radius: 4px;
  border:0;
}

.tools {
  height: 480px;
  width: 95%;
  margin-left: auto;
  margin-right: auto;
  display: grid;
  grid-template-columns: 25% 25% 25% 25%;
  grid-template-rows: 33.33% 33.33% 33.33%;
}

.tool {
  background: radial-gradient(rgb(35, 44, 116) 0%,rgb(42, 45, 56) 30%,rgb(42, 45, 56) 100%) ;
  margin-top: 18px;
  height: 132px;
  width: 186px;
  margin-left: 15px;
  border-radius: 4px;
  text-align: center;
  color:rgb(212, 215, 218)
}

.tool_pic {
  height: 50px;
  margin-top: 23px;

}
</style>
