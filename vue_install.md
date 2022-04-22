本文件用于介绍vue安装步骤 ：

node.js下载地址：https://nodejs.org/en/download/

根据电脑的情况自行选择版本，这里我选择WINDOWS X64

一、node.js的安装

1.下载好msi文件后，直接双击运行进行安装

2.点击next，选择I accept,点击next

3.选择安装的文件夹，然后next

4.点击树形图片选择你的安装模式，然后next（此处我选择的是online document shortcuts）

5.点击install，然后等待安装完毕，点击finish

6.检测path环境变量是否进行了添加，win+r打开cmd输入path指令查看，然后检测node.js版本

二、配置安装目录和缓存日志目录

1.安装的文件夹下创建两个文件夹【node_global】及【node_cache】分别作为默认安装目录和缓存日志目录。

2、执行命令，将npm的全局模块目录和缓存目录配置到我们刚才创建的那两个目录：
<!-- npm config set prefix "D:\Program Files\nodejs\node_global"
npm config set cache "D:\Program Files\nodejs\node_cache" -->

三、环境配置

直接win+s搜索环境变量，进入环境变量对话框

1、【系统变量】下新建【NODE_PATH】，此处设置第三方依赖包安装目录
如果跟着第2步修改了全局安装目录，则输入【D:\Program Files\nodejs\node_global\node_modules 】

2.【系统变量】下的【Path】添加上node的路径【D:\Program Files\nodejs\】

3.如果设置了全局安装目录，【用户变量】下的【Path】将默认的 C 盘下 APPData/Roaming\npm 修改为【D:\Program Files\nodejs\node_global】，【D:\Program Files\nodejs\node_cache】，这是nodejs默认的模块调用路径

四、配置淘宝镜像源

查看npm下载源 npm config get registry

（1）临时使用
npm --registry https://registry.npm.taobao.org install cluster

（2）永久使用
npm config set registry https://registry.npm.taobao.org 

vue的安装：
1.安装vue及脚手架
  1.npm install vue -g  其中-g是全局安装，指安装到global全局目录去

  2.查看安装的vue信息：npm info vue 

  3.查看安装的vue版本npm list vue

2.安装webpack模板
在命令行中运行命令 npm install webpack -g ，然后等待安装完成
  webpack 4x以上，webpack将命令相关的内容都放到了webpack-cli，
  所以还需要安装webpack-cli：npm install --global webpack-cli，
  安装成功后可使用webpack -v查看版本号。

3.安装脚手架vue-cli 2.x
  npm install vue-cli -g
 
 用这个命令来检查其版本是否正确：vue --version或vue -V

4.这里顺手安装上vue-router
  npm install -g vue-router
  
5.可以在文件夹看到安装目录








