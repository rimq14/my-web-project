<template>
    <div class="root">
        <div class="mycanvas" style="width=100%;height: 100%;position: absolute;">
            <canvas id="layer" width=1024 height=955></canvas>
        </div>
        <div class="table">
            <!-- 表格-->
            <el-table :data="extraimg" style="width:100%;position: absolute;">

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
        <div class="btn" style="position:absolute">
            <el-button icon="el-icon-search" size="mini" @click="rectImage"></el-button>
            <el-button @click="rectCancel">删除</el-button>
            <el-button @click="dealData">处理</el-button>
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
            extraimg: [],
            myCanvas: null,
            ctx: null,
            imgObject: [],
            imgX: 0,
            imgY: 0, // 图片在画布中渲染的起点坐标
            imgScale: 0.1, // 图片的缩放大小
            rectScale: 1,    // 选框的比例
            rectflag: false, // 框选标志位
            dealflag: false,
            rectangles: [],  // 框选的参数
            pos: {},// 存储点击鼠标坐标
            rate: {},    // 框选的位置在图片的比例
        }
    },
    mounted() {
        this.loadinfo();
        this.layer = document.getElementById("layer");      // 用于图片的一系列操作
        this.ctx = this.layer.getContext('2d');
        this.canvasEventsInit();
    },
    methods: {
        loadinfo() {
            getPic().then(res => {
                this.extraimg = res.data
            });
            
        },
        loadImg(img) {
            var _this = this;
            _this.ctx.clearRect(0, 0, 2400, 1400);  // 初始化画布
            var image = new Image();
            image.src = img;
            // image.crossOrigin = "";    // 解决getImageData()函数跨域
            image.onload = function () {
                _this.imgObject = image;
                _this.drawImage(image); // 加载图片
            }
        },
        drawImage(image) {
            var _this = this;
            _this.ctx.clearRect(0, 0, 2400, 1400);
            _this.ctx.drawImage(
                image, //规定要使用的图片,此处为链接
                _this.imgX,
                _this.imgY, //在画布上放置图像的 x 、y坐标位置。
                image.width * _this.imgScale,
                image.height * _this.imgScale //要使用的图像的宽度、高度
            );
            _this.canvasMouseWheel();   // 图片缩放操作
        },
        rectar(x, y, width, height) {
            this.x = x;
            this.y = y;
            this.width = width;
            this.height = height;
        },
        drawRect() {
            var _this = this;
            var rect = _this.rectangles[_this.rectangles.length - 1];   // 取数组最后一个元素
            _this.ctx.beginPath();
            _this.ctx.clearRect(rect.x, rect.y, rect.width, rect.height);       // 清除前一元素
            _this.drawImage(_this.imgObject);       //重新绘制图片
            _this.ctx.strokeStyle = '#00ff00';      // 设置线条颜色，必须放在绘制之前
            _this.ctx.lineWidth = 2;        // 线宽设置，必须放在绘制之前-->
            _this.ctx.strokeRect(rect.x * _this.rectScale, rect.y * _this.rectScale, rect.width * _this.rectScale, rect.height * _this.rectScale); // 矩形绘制
        }, // 绘制矩形
        rectImage() {
            var _this = this;
            _this.rectflag = true;
        },  // 框选图片
        dealData() {
            var _this = this; _this.dealflag = true;

        },    // 将框选的坐标参数传送至后端，并获取后端数据进行显示
        rectCancel() {
            var _this = this;
            _this.rectangles.length = 0;
            _this.drawImage(_this.imgObject);       //重新绘制图片
        }, // 取消框选的区域
        canvasEventsInit() {
            var _this = this, canvas = _this.layer;
            canvas.onmousedown = function (e) {
                var imgx = _this.imgX, imgy = _this.imgY;
                var pos = { x: e.clientX - canvas.offsetLeft, y: e.clientY - canvas.offsetTop }; //鼠标点击坐标
                _this.pos = pos;

                canvas.onmousemove = function (e) {
                    var movenumber = { x: (e.clientX - canvas.offsetLeft - pos.x) * 2, y: (e.clientY - canvas.offsetTop - pos.y) * 2 };
                
                    if (_this.rectflag) {
                        if (movenumber.x && movenumber.y) {
                            var x = pos.x, y = pos.y, width = movenumber.x, height = movenumber.y;      // 选框的参数
                            var rectangle = new _this.rectar(x, y, width, height);     // 创建一个新的矩形对象
                            _this.rectangles.push(rectangle);       // 将矩形对象保存在数组中
                            _this.drawRect();       // 绘制矩形
                        }
                    } else {
                        canvas.style.cursor = 'move';     // 移动标识
                        var x = movenumber.x + imgx, y = movenumber.y + imgy; // 图像渲染的起始点坐标
                        _this.imgX = x, _this.imgY = y; // 渲染图象的位置
                        _this.drawImage(_this.imgObject); //重新绘制图片
                    }
                };
                canvas.onmouseup = function (e) {
                    canvas.onmousemove = null;
                    canvas.style.cursor = 'default';    // 默认标识
                    _this.rectflag = false;
                };
            };
        },
        canvasMouseWheel() {
            var _this = this, canvas = _this.layer;
            canvas.onmousewheel = canvas.onwheel = function (event) { //滚轮放大缩小
                var wheelDelta = event.wheelDelta ? event.wheelDelta : (event.deltalY * (-40)); //获取当前鼠标的滚动情况
                if (wheelDelta > 0) {
                    _this.imgScale *= 1.1;
                    _this.rectScale *= 1.1;
                } else {
                    if (_this.imgScale > 0.1) {
                        _this.imgScale *= 0.9;
                        _this.rectScale *= 0.9;
                    }
                }
                event.preventDefault && event.preventDefault(); // 阻止页面的点击菜单栏
                _this.drawImage(_this.imgObject); //重新绘制图片
                _this.drawRect();       // 重新绘制矩形
                return false;
            };
        },
    },
}
</script>

<style scoped>

</style>
