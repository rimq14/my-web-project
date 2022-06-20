<template xmlns="http://www.w3.org/1999/html">
  <div class="hello">
    <div>

      <div class="header">
        <div class="sub_menu">
          Overview
        </div>
        <div class="sub_menu">
          功能选项
          <ul class="dropdown">
            <li>
              <router-link class="list-group-item" to="/experience/change_detection">
                变化检测
              </router-link>
            </li>
            <li>
              <router-link class="list-group-item" to="/experience/target_detection">
                目标检测
              </router-link>
            </li>
            <li>
              <router-link class="list-group-item" active-class="active" to="/experience/target_extraction">
                目标提取
              </router-link>
            </li>
            <li>
              <router-link class="list-group-item" active-class="active" to="/experience/object_classification">
                地物分类
              </router-link>
            </li>
          </ul>
        </div>
        <div class="sub_menu">
          <button class="menu_button">
            <router-link :to="{ path: '/experience/change_detection' }">体验中心</router-link>
          </button>
        </div>
        <div class="sub_menu">
          <button class="menu_button">
            <router-link :to="{ path: '/menu' }" class="btn btn-primary" role="button" target="_blank">
              进入平台
            </router-link>
          </button>
        </div>
      </div>
      <div class="main">
        <h1 style="font-size:4em;font-weight: 500;color:white;
          margin-bottom: 5px;">智能遥感图像解析平台</h1> 
        <div class="box">
          <div class="chars">A</div>
          <div class="chars">I</div>
          <div class="chars">E</div>
          <div class="chars">A</div>
          <div class="chars">R</div>
          <div class="chars">T</div>
          <div class="chars">H</div>
          
          <div class="ll A"></div>
          <div class="ll I"></div>
          <div class="ll E"></div>
          <div class="ll AA"></div>
          <div class="ll R"></div>
          <div class="ll T"></div>
          <div class="ll H"></div>
          
          <div class="pcov"></div>
        </div>




      </div>
      <p style="color:white">
        深度学习
      </p>
      <section>
        <div class="section_item">
          <div class="a">
            Log in
          </div>
          <div class="a">
            Log in
          </div>
          <router-link :to="{ path: '/menu' }">
            进入平台了解更多
          </router-link>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
export default {
  name: "index",
  data() {
    return {
      // 后端服务器图片+
      pictures: [
        "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        "https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg",
        "http://127.0.0.1:8000/media/pictures/90c8f476cd.png",
        "http://127.0.0.1:8000/media/pictures/82d8c7c349.png"
      ],
      activeIndex: "1"
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },

  }
};
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
* {
  margin: 0;
  padding: 0;
}

/*主页背景*/
.hello {
  width: 100%;
  height: 754px;
  background: url(../Experience/pic/earth1.png);
  background-size: cover;
  object-fit: cover;
  animation: fade 15s linear infinite;
}

@keyframes fade {
  0% {
    background: url(../Experience/pic/t5.jpg) no-repeat center;
    background-size: cover;
  }

  25% {
    background: url(../Experience/pic/t4.jpg) no-repeat center;
    background-size: cover;
  }

 50% {
    background: url(../Experience/pic/t2.jpg) no-repeat center;
    background-size: cover;
  }

  75% {
    background: url(../Experience/pic/t9.jpg) no-repeat center;
    background-size: cover;
  }
 100% {
    background: url(../Experience/pic/t5.jpg) no-repeat center;
    background-size: cover;
  }

  
}



/*导航栏的四小个提示*/
.el-menu-item {
  width: 160px;
  font-weight: 300;
}

.el-submenu {
  margin-right: 60px;

}

.images {
  width: auto;
  height: auto;
  /*border: 1px solid green;*/
}

/*页面的主要部分*/
.main {
  text-align: center;
  height: 300px;
  width: 80%;
  margin-left: auto;
  margin-right: auto;
  margin-top:110px;
  perspective: 300;
  -webkit-perspective: 300;
  /*overflow: hidden;*/
}
.chars{
  color: #fff;
  position: relative;
  width:60px;
  height: 60px;
  text-align: center;
  line-height: 60px;
  font-size: 54px;
  font-weight: 900;
  font-style: italic;
  opacity: 0;
}
/*字符外的方块*/
.ll{
  position: absolute;
  margin-left: -480px;
  width:50px;
  height:50px;
  border-radius: 3px;
  opacity: 0;

}

.H{
  border:4px solid #fcb1b1;
  animation: hmove 2s linear forwards;
}
.T{
  border:4px solid #96c7f7;
  animation: tmove 2s linear forwards;
  animation-delay: 0.1s;
}
.R{
  border:4px solid #f5bafc;
  animation: rmove 2s linear forwards;
  animation-delay: 0.2s;
}
.AA{
  border:4px solid #96f7d2;
  animation: cmove 2s linear forwards;
    animation-delay: 0.3s;
}
.E{
  border:4px solid #f0f696;
  animation: emove 2s linear forwards;
    animation-delay: 0.4s;
}
.I{
  border:4px solid #fcb1b1;
  animation: imove 2s linear forwards;
    animation-delay: 0.5s;
}
.A{
  border:4px solid #96c7f7;
  animation: amove 2s linear forwards;
    animation-delay: 0.6s;
}
/*正中间那条线*/
.pcov{
  position: absolute;
  width:4px;
  height: 60px;
  background-color: #fcb1b1;
  opacity: 0;
  animation: showp forwards;
  animation-delay: 2.3s;
}
/*显示那条线*/
@keyframes showp{
  from{
    opacity: 0;
  }
  to{
    transform: scale(1,2);
    opacity: 1;
  }
}

/*定义动画*/
@keyframes amove{
  0%{
    opacity: 1;
    transform:rotateY(0deg);
  }
  50%{
    transform: rotateY(180deg);
  }
  100%{
    opacity: 1;
    transform: rotateY(360deg);
  }
}
@keyframes imove{
  30%{
    opacity: 1;
    transform:translate(30px) rotateY(135deg) scale(1.1,1.1);
  }
  60%{
   transform:translate(50px) rotateY(45deg) scale(1.1,1.1);
  }
  85%{
    
    transform:translate(80px) rotateY(103deg) scale(1.2,1.2);
  }
  100%{
    opacity: 1;
    transform:translate(80px) rotateY(77deg) scale(1.2,1.2);
  }

}
@keyframes emove{
  30%{
    opacity: 1;
    transform:translate(60px) rotateY(135deg) scale(1.2,1.2);
  }
  60%{
   transform:translate(120px) rotateY(45deg) scale(1.3,1.3);
  }
  85%{
    
    transform:translate(160px) rotateY(103deg) scale(1.3,1.3);
  }
  100%{
    opacity: 1;
    transform:translate(164px) rotateY(77deg) scale(1.3,1.3);
  }

}
@keyframes cmove{
  30%{
    opacity: 1;
    transform:translate(60px) rotateY(135deg) scale(1.2,1.2);
  }
  60%{
   transform:translate(120px) rotateY(45deg) scale(1.4,1.4);
  }
  85%{
    
    transform:translate(240px) rotateY(135deg) scale(1.6,1.6);
  }
  100%{
    opacity: 1;
    transform:translate(240px) rotateY(90deg) scale(1.6,1.6);
  }
}
@keyframes rmove{
  33%{
    opacity: 1;
    transform:translate(80px) rotateY(135deg) scale(1.2,1.2);
  }
  66%{
   transform:translate(240px) rotateY(45deg) scale(1.6,1.6);
  }
  95%{
    
    transform:translate(320px) rotateY(100deg) scale(1.4,1.4);
  }
  100%{
    opacity: 1;
    transform:translate(320px) rotateY(103deg) scale(1.3,1.3);
  }
}
@keyframes tmove{
  33%{
    opacity: 1;
    transform:translate(80px) rotateY(135deg) scale(1.2,1.2);
  }
  66%{
   transform:translate(240px) rotateY(45deg) scale(1.6,1.6);
  }
  95%{
    
    transform:translate(390px) rotateY(135deg) scale(1.2,1.2);
  }
  100%{
    opacity: 1;
    transform:translate(402px) rotateY(103deg) scale(1.2,1.2);
  }
}
@keyframes hmove{
  25%{
    opacity: 1;
    transform:translate(100px) rotateY(135deg) scale(1.2,1.2);
  }
  50%{
   transform:translate(260px) rotateY(45deg) scale(1.6,1.6);
  }
  85%{
    
    transform:translate(400px) rotateY(135deg) scale(1.2,1.2);
  }
  100%{
    opacity: 1;
    transform:translate(484px) rotateY(0deg) scale(1,1);
  }
}
/*前两个字符的动画*/
@keyframes show12{
  0%{
    opacity: 1;
    transform: rotateY(0deg);
  }
  100%{
    opacity: 1;
    transform: rotateY(360deg);
  }
}
/*第三个及之后字符的动画*/
@keyframes show3{
  0%{
    opacity: 1;
    transform: rotateY(90deg);
  }
  100%{
    opacity: 1;
    transform: rotateY(360deg);
  }
}
/*为每个字符添加动画*/
.box{
  text-align: center;
  height: 200px;
  width: 80%;
  margin-left: auto;
  margin-right: auto;

  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: row;
  perspective: 300;
  -webkit-perspective: 300;
}
.box div:nth-child(1){
  animation:show12 1.2s linear forwards;
  animation-delay: 0.2s;
}
.box div:nth-child(2){
  animation:show12 1.2s linear forwards;
  animation-delay: 0.4s;
}
.box div:nth-child(3){
  animation:show3 1s linear forwards;
  animation-delay: 0.7s;
}
.box div:nth-child(4){
  animation:show3 1s linear forwards;
  animation-delay: 0.9s;
}
.box div:nth-child(5){
  animation:show3 1s linear forwards;
  animation-delay: 1.1s;
}
.box div:nth-child(6){
  animation:show3 1.2s linear forwards;
  animation-delay: 1.3s;
}
.box div:nth-child(7){
  animation:show3 1.2s linear forwards;
  animation-delay: 1.6s;
}


p {
  text-align: center;
  font-size: large;
  line-height: 35px;

}



.over-button {
  border: 2px solid rgb(74, 74, 204);
  background-color: rgb(30, 30, 30);
  opacity: 0.8;

}

/*下拉选框*/
.list-group-item {
  color: white;
}
</style>
<style>
* {
  margin: 0;
  padding: 0;
}

.main_button {
  margin-top: 80px;
  height: 55px;
  width: 180px;
  border: 1px solid white;
  background-color: rgba(224, 221, 221, 0.3);
  color: white;
  border-radius: 3px;
}



.header {
  width: 100%;
  height: 60px;
  background-color: rgb(35, 35, 35);
  color: white;
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  text-align: center;

}

.sub_menu {
  line-height: 60px;
  margin-left: 15px;
  margin-right: 15px;
  width: 95px
}

.sub_menu:hover {
  color: rgb(46, 118, 226);
}

.sub_menu:hover .dropdown {
  display: block;
}

.menu_button {
  height: 35px;
  width: 95px;
  border: 1.5px solid rgb(184, 180, 180);
  background-color: rgba(122, 121, 119, 0.3);
  color: white;
  border-radius: 4px;
}

.menu_button:hover {
  border: 1px solid rgb(46, 118, 226);
  background-color: rgb(30, 30, 30);
  opacity: 0.8;

}

.dropdown {
  list-style-type: none;
  background: rgba(57, 56, 56, 0.7);
  color: white;
  box-shadow: 0 1px 2px #333;
  display: none;
  border-radius: 2px;
}

li {
  line-height: 40px;
  width: 98px;
  text-align: center;
}

.list-group-item:hover {
  color: rgb(46, 118, 226);
}

.list-group-item-active {
  text-decoration: none;
}

a {
  text-decoration: none;
  color: white;
}

/*导入字体*/
section {

  width: 100%;
  height: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
}

section .section_item {
  position: relative;
  display: flex;
  justify-content: space-around;
  align-items: center;
  transition: filter 0.5s, transform 0.5s;
}

.section_item .a {
  font-family: Georgia, 'Times New Roman', Times, serif;
  color: #fff;
  font-size: 6vw;
  top: 0;
  transition: top 0.5s, opacity 0.5s;
  opacity: 1;
}

/*切割文字*/
section .section_item .a:nth-child(1) {
  position: absolute;
  clip-path: polygon(0% 0%, 100% 0%, 100% 51%, 0% 51%);
}

section .section_item .a:nth-child(2) {
  position: relative;
  clip-path: polygon(0% 50%, 100% 50%, 100% 100%, 0% 100%);
}

/*触发景深效果*/
section:hover .section_item {
  filter: blur(10px);
  transform: scale(0.8);
  transition: filter 0.5s, transform 0.5s;
}

/*对应的取消景深效果*/
section .section_item:hover {
  filter: blur(0px);
  transform: scale(1.1);
  transition: filter 0.5s, transform 0.5s;
}

/*上半部分上移并变淡*/
section .section_item:hover .a:nth-child(1) {
  top: -40px;
  opacity: 0.5;
  transition: top 0.5s, opacity 0.5s;

}

/*下半部分下移并变淡*/
section .section_item:hover .a:nth-child(2) {
  top: 40px;
  opacity: 0.5;
  transition: top 0.5s, opacity 0.5s;

}

/*链接*/
section .section_item a {
  position: absolute;
  text-decoration: none;
  opacity: 0;
}

section .section_item a:hover {
  text-decoration: underline;
}

section .section_item:hover a {
  opacity: 1;
  transition: opacity 0.5s;
}
</style>
