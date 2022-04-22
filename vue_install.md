本文件用于介绍vue安装步骤 ：

vue下载地址：https://nodejs.org/en/download/

根据电脑的情况自行选择版本，这里我选择WINDOWS X64

一、vue的安装

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

1.直接win+s搜索环境变量，进入环境变量对话框



