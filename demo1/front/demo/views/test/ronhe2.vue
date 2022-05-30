<template>
    <div class="root" style="width: 100%;height: 100%;">
        <div class="mycanvas">
            <canvas id="layer" :width="canvasWidth" :height="canvasHeight" style="width: 100%;height: 100%;"></canvas>
        </div>
        <div class="table">
            <!-- 表格-->
            <el-table :data="extraimg" style="width:auto">
                <el-table-column label="ID" prop="id">
                </el-table-column>

                <el-table-column label="IMG" prop="img">
                </el-table-column>

                <el-table-column align="right">
                    <!-- 通过设置 Scoped slot 来自定义表头 -->
                    <template v-slot:header>操作</template>
                    <template v-slot="scope">
                        <!-- scope.row.img 获取图片链接数据-->
                        <el-button size="mini" type="text" @click="loadImg(scope.row.img)">加载
                        </el-button>
                    </template>
                </el-table-column>
            </el-table>
        </div>
        <div class="btn">
            <el-button icon="el-icon-search" size="mini" @click="rectImage"></el-button>
            <el-button icon="el-icon-close" size="mini" @click="rectCancel"></el-button>
        </div>
    </div>
</template>

<script>
import { getPic } from "../../api/apiRequest";

export default {
    name: 'ronhe1',
    components: {},
    data() {
        return {
            canvasWidth: 2400,
            canvasHeight: 1400, // 画布大小
            extraimg: [],
            myCanvas: null,
            ctx: null,
            imgObject: [],
            imgX: 200,
            imgY: 200, // 图片在画布中渲染的起点坐标
            imgScale: 0.1, // 图片的缩放大小
            rectflag: false, // 框选标志位
            w: 0,
            h: 0, // 框选框的宽
            pos: {},// 存储点击鼠标坐标
        }
    },
    mounted() {
        this.loadinfo();
        this.layer = document.getElementById("layer");      // 用于图片的一系列操作
        this.ctx = this.layer.getContext('2d');
        this.layer2 = document.createElement("canvas");     // 用于
        this.ctx2 = this.layer2.getContext('2d');
        this.canvasEventsInit();
        this.canvasMouseWheel();
    },
    methods: {
        loadinfo() {
            getPic().then(res => {
                this.extraimg = res.data
            })
        },
        loadImg(img) {
            var _this = this;
            _this.ctx.clearRect(0, 0, this.canvasWidth, this.canvasHeight); // 初始化画布
            var image = new Image();
            image.src = img;
            image.crossOrigin = "";    // 解决getImageData()函数跨域
            image.onload = function () {
                _this.imgObject = image;
                _this.drawImage(image); // 加载图片
            }
        },
        drawImage(image) {
            var _this = this;
            _this.ctx.clearRect(0, 0, this.canvasWidth, this.canvasHeight);
            _this.ctx.drawImage(
                image, //规定要使用的图片,此处为链接
                _this.imgX + image.x * _this.imgScale,
                _this.imgY + image.y * _this.imgScale, //在画布上放置图像的 x 、y坐标位置。
                image.width * _this.imgScale,
                image.height * _this.imgScale //要使用的图像的宽度、高度
            );
        },
        drawRect() {
            var _this = this, canvas = _this.layer;
            if (_this.rectflag == false) {
                // _this.ctx.clearRect(_this.pos.x, _this.pos.y, _this.w, _this.h);
                console.log("开始绘制");
                _this.ctx.beginPath();
                _this.ctx.moveTo(_this.pos.x, _this.pos.y); // 设置起点
                // 设置线条颜色，必须放在绘制之前
                _this.ctx.strokeStyle = '#00ff00';
                // 线宽设置，必须放在绘制之前-->
                _this.ctx.lineWidth = 2;
                _this.ctx.strokeRect(_this.pos.x, _this.pos.y, _this.w, _this.h); // 矩形绘制
                _this.getImgData();    // 调用获取框选区域参数函数
            }
        }, // 绘制矩形
        rectImage() {
            var _this = this;
            _this.rectflag = true;
        },  // 框选图片
        getImgData() {
            var _this = this;
            var imageData = _this.ctx.getImageData(_this.pos.x, _this.pos.y, _this.w, _this.h);     // 获取框选数据
            _this.layer2.width = _this.w, _this.layer2.height = _this.h; 
            _this.ctx2.putImageData(imageData,0,0);
            console.log(_this.layer2.toDataURL("image/png", 1.0));   // 查看信息
            
            
        },    // 获取框选区域的参数
        putImgData() {
            var _this = this;
            _this.ctx.putImageData(imageData, _this.pos.x, _this.pos.y);
        },    // 将图像数据重画至Canvas画布中
        rectCancel() {
            var _this = this;
        }, // 取消框选的区域
        canvasEventsInit() {
            var _this = this,
                canvas = _this.layer;
            canvas.onmousedown = function (event) {
                var imgx = _this.imgX, imgy = _this.imgY;
                var pos = {
                    x: event.offsetX,
                    y: event.offsetY
                }; //鼠标点击坐标
                _this.pos = pos;

                canvas.onmousemove = function (e) { //移动
                    if (_this.rectflag) {
                        var width = (e.offsetX - pos.x) * 2,
                            height = (e.offsetY - pos.y) * 2; // 矩形的宽度和高度
                        _this.w = width, _this.h = height; // 框选框的尺寸
                    } else {
                        canvas.style.cursor = 'move';     // 移动标识
                        var x = (e.offsetX - pos.x) * 2 + imgx,
                            y = (e.offsetY - pos.y) * 2 + imgy; // 图像渲染的起始点坐标
                        _this.imgX = x, _this.imgY = y; // 渲染图象的位置
                        _this.drawImage(_this.imgObject); //重新绘制图片
                    }
                };
                canvas.onmouseup = function (e) {
                    canvas.onmousemove = null;
                    canvas.style.cursor = 'default';    // 默认标识
                    _this.rectflag = false;
                    _this.drawRect(); // 绘制矩形
                };
            };
        },
        canvasMouseWheel() {
            var _this = this,
                canvas = _this.layer;
            canvas.onmousewheel = canvas.onwheel = function (event) { //滚轮放大缩小
                var wheelDelta = event.wheelDelta ? event.wheelDelta : (event.deltalY * (-40)); //获取当前鼠标的滚动情况
                if (wheelDelta > 0) {
                    _this.imgScale *= 1.1;
                } else {
                    if (_this.imgScale > 0.1) {
                        _this.imgScale *= 0.9;
                    }
                }
                _this.drawImage(_this.imgObject); //重新绘制图片
                event.preventDefault && event.preventDefault(); // 阻止页面的点击菜单栏
                return false;
            };
        },
    },
}
</script>

<style scoped>
</style>
