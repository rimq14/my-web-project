<template>
  <div class="current-page">
    <el-container>
      <el-header>
        <el-button type="text" @click="dialog = true">添加图片</el-button>
        <el-button type="text" @click="rectImage">选择区域</el-button>
        <el-button type="text" @click="rectCancel">删除区域</el-button>
        <el-button type="text" @click="run">运行推理</el-button>
      </el-header>
      <el-container>
        <el-drawer
          title="图片上传"
          :before-close="handleClose"
          :visible.sync="dialog"
          direction="ltr"
          custom-class="demo-drawer"
          ref="drawer"
        >
          <div class="demo-drawer__content">
            <!-- form表单 -->
            <el-form
              :model="ruleForm"
              :rules="rules"
              ref="ruleForm"
              label-width="100px"
            >
              <el-form-item label="地区名称" prop="name">
                <el-input
                  v-model="ruleForm.name"
                  style="width: 150px"
                ></el-input>
              </el-form-item>

              <el-form-item label="上传图片" prop="image_url">
                <!-- 图片选择 -->
                <el-upload
                  list-type="picture-card"
                  class="image-uploader"
                  action="none"
                  :on-change="fileChange"
                  :auto-upload="false"
                >
                  <i class="el-icon-plus"></i>
                  <div slot="file" slot-scope="{ file }">
                    <img
                      class="el-upload-list__item-thumbnail"
                      :src="file.url"
                      alt=""
                    />
                    <span class="el-upload-list__item-actions">
                      <span
                        class="el-upload-list__item-preview"
                        @click="handlePictureCardPreview(file)"
                      >
                        <i class="el-icon-zoom-in"></i>
                      </span>
                    </span>
                  </div>
                </el-upload>
                <!-- 图片缩略图显示 -->
                <el-dialog :visible.sync="dialogVisible">
                  <img width="100%" :src="dialogImageUrl" alt="" />
                </el-dialog>
              </el-form-item>
            </el-form>
            <!-- 抽屉按键 -->
            <div class="demo-drawer__footer">
              <el-button
                type="primary"
                @click="submitForm('ruleForm')"
                :loading="loading"
                >{{ loading ? "上传中 ..." : "上传" }}</el-button
              >
              <el-button @click="cancelForm">取 消</el-button>
            </div>
          </div>
        </el-drawer>

        <div class="right">
          <el-main>
            <!--  style控制图片渲染的范围  -->
            <canvas
              id="layer"
              :width="canvasWidth"
              :height="canvasHeight"
            ></canvas>
          </el-main>
        </div>
      </el-container>
    </el-container>
  </div>
</template>


<script>
import axios from "axios";
import { getImages, postPic, postName } from "../../api/apiRequest";
export default {
  name: "operation",
  data() {
    return {
      canvasWidth: 1900, // 画布大小
      canvasHeight: 1300,
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
      imageName: [], // 处理的图片名
      id: [], // 加载的图片id
      ruleForm: {
        name: "",
        image_url: "",
      },
      rules: {
        name: [
          {
            required: true,
            message: "请输入图片所属地区名称",
            trigger: "blur",
          },
          { max: 5, message: "长度必须少于5 个字符", trigger: "blur" },
        ],
        image_url: [{ required: true, message: "请选择图片", trigger: "blur" }],
      },
    };
  },
  mounted() {
    // this.loadinfo();   // 获取图片信息
    this.layer = document.getElementById("layer");
    this.ctx = this.layer.getContext("2d");
    // this.canvasEventsInit();
  },
  methods: {
    handleClose(done) {
      if (this.loading) {
        return;
      }
      this.$confirm("确定要上传吗？")
        .then((_) => {
          this.loading = true;
          this.timer = setTimeout(() => {
            done();
            // 动画关闭需要一定的时间
            setTimeout(() => {
              this.dialog = false;
              this.loading = false;
            }, 400);
          }, 4000);
        })
        .catch((_) => {});
    }, // 关闭抽屉
    cancelForm() {
      this.loading = false;
      this.dialog = false;
      clearTimeout(this.timer);
    }, // 关闭抽屉
    openFullScreen() {
      const loading = this.$loading({
        lock: true,
        text: "Loading",
        spinner: "el-icon-loading",
        background: "rgba(0, 0, 0, 0.7)",
      });
      setTimeout(() => {
        loading.close();
      }, 2000);
    },
    fileChange(file) {
      this.ruleForm.image_url = file.raw;
    }, // 表单信息填写
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          // 请求体编码,使用form-data库
          let formData = new FormData();
          formData.append("name", this.ruleForm.name);
          formData.append("image_url", this.ruleForm.image_url); // 构造formData数据
          postPic(formData).then((res) => {
            // 上传formData数据,formData作为实参
            this.splitImage(this.ruleForm.name); // 进行图片拆分
            // this.handleClose();
          });
          this.$refs.drawer.closeDrawer(); // 关闭抽屉
        } else {
          console.log("上传失败");
          return false;
        }
      });
    }, // 提交表单
    handlePictureCardPreview(file) {
      this.dialogImageUrl = file.url;
      this.dialogVisible = true;
    }, // 缩略图可视化
    splitImage(name) {
      this.imageName = name;
      var splitData = new FormData();
      // console.log("拆分图片的名称：",name);
      splitData.append("name", name);
      postName(splitData).then((res) => {
        this.loadImages(name);
      });
    }, // 对图片进行拆分
    loadImages(name) {
      var _this = this;
      _this.openFullScreen(); // loading
      getImages().then((res) => {
        _this.imageData = res.data;
        for (var i = 0; i < _this.imageData.length; i++) {
          if (_this.imageData[i].name == name) {
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
            height: 1024,
          }),
            count++;
          // 图片信息添加完毕
          if (count >= length) {
            // extraImg.onload = function () {
              _this.imgObject = imageList;
              _this.drawImage(imageList);
            // };
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
    windowToCanvas(x, y, type) {
      //返回元素的大小以及位置
      var bbox = canvas.getBoundingClientRect();
      // bbox 的宽度会加上 canvas 的 border 会影响精度
      return new Point(
        x - bbox.left * (canvas.width / bbox.width),
        y - bbox.top * (canvas.height / bbox.height),
        type
      );
    },
    run() {
      var _this = this;
      var rect = _this.rectangles[_this.rectangles.length - 1]; // 取数组最后一个元素

      var params = {
        name: _this.imageName,
        x1 :_this.pos.x - _this.imgX,
        y1 :_this.pos.y - _this.imgY,
        x2 :_this.pos.x - _this.imgX + rect.width,
        y2 :_this.pos.y - _this.imgY + rect.height,
        scale:_this.imgScale
      };

      axios
        .post("http://127.0.0.1:8000/api/pic/result/", params)
        .then((res) => {
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
      canvas.onmousedown = function (e) {
        var imgx = _this.imgX,
          imgy = _this.imgY;
        var pos = {
          x: e.clientX - canvas.offsetLeft,
          y: e.clientY - canvas.offsetTop,
        }; //鼠标点击坐标
        _this.pos = pos;
        console.log(pos.x,pos.y);
        canvas.onmousemove = function (e) {
          var movenumber = {
            x: e.clientX - canvas.offsetLeft - pos.x,
            y: e.clientY - canvas.offsetTop - pos.y,
          };

          if (_this.rectflag) {
            if (movenumber.x && movenumber.y) {
              var x = pos.x,
                y = pos.y,
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
        canvas.onmouseup = function (e) {
          canvas.onmousemove = null;
          canvas.style.cursor = "default"; // 默认标识
          _this.rectflag = false;
        };
      };
    },
    canvasMouseWheel() {
      var _this = this,
        canvas = _this.layer;
      canvas.onmousewheel = canvas.onwheel = function (event) {
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
    },
  },
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
}

.current-page {
  width: 100%;
  height: 100%;
  display: flex;
}

.left {
  width: auto;
}

.right {
  flex: 1;
}

.el-header {
  height: 30px;
  background-color: #1f1f20;
  color: white;
  text-align: center;
  line-height: 60px;
}

.flat_header_left {
  height: 40px;
  width: 25%;
  background-color: #1f1f20;
  color: white;
  text-align: center;
  line-height: 60px;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  margin-left: 130px;
}

.header_char:hover {
  color: rgb(63, 125, 217);
}

.flat_header_button {
  height: 35px;
  width: 100px;
  border-radius: 3px;
  border: 1px solid white;
  background-color: rgb(112, 109, 109);
  color: white;
}

.flat_header_button:hover {
  background-color: black;
  border: 1px solid rgb(63, 125, 217);
}

.flat_header_right {
  float: right;
  margin-right: 160px;
  margin-top: -30px;
}

.el-main {
  margin: 0;
  background-color: black;
}

canvas {
  display: block;
}

/* */
.choices {
  height: 35px;
  width: 90%;
  border-radius: 3px;
  margin-top: 20px;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 30px;
  background-color: #252424;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  flex-wrap: nowrap;
}

.choice {
  color: grey;
  width: 33.3%;
  text-align: center;
  line-height: 35px;
}

.choice:hover {
  background-color: grey;
  color: white;
}

.example {
  height: 30px;
  text-align: center;
  color: grey;
  margin-top: 20px;
  font-size: 14px;
}

/* */
.imgs {
  height: 400px;
  width: 85%;
  /* background-color: rgb(166, 163, 163);*/
  margin-left: auto;
  margin-right: auto;
  display: flex;
  flex-direction: column;
}

.img {
  height: 120px;
  margin: 10px;
  width: 90%;
  background-color: antiquewhite;
  border: 1px solid #252424;
  margin-left: auto;
  margin-right: auto;
}

.img:active {
  border: 3px solid rgb(63, 125, 217);
}

.router-link {
  color: white;
}

a {
  color: white;
  text-decoration: none;
}
</style>
