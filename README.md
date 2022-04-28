# web-development
用于web开发学习，基于django框架，前端采用boostrap

website 为项目文件夹，home为创建的web应用

1.由于对前后端知识的欠缺，前后端并未进行分离，而是直接采用前端模板直接从数据库传递参数

重新创建一个项目文件进行后续的测试

2.现阶段尝试django完全进行后端的开发，vue进行前端的开发

3.vue+django实现了一个基本的book_demo前后端分离实例

4.vue如何进行路由的分配呢？
为了解决单页问题，采用vue+vue router，通过vue router进行路由的跳转

5.现阶段还未对前端页面进行美化，后续该如何选择呢？
boostrap 直接使用还是使用boostrap-vue

6.目前对vue有了一定的理解，但是对app.vue的作用仍然有点迷惑。app.vue的作用？
app.vue可以当做是网站首页，是一个vue项目的主组件，页面入口文件 ，所有页面都是在App.vue下进行切换的。
是整个项目的关键，app.vue负责构建定义及页面组件归集。

7.vue整合boostrap时，相关的布局css文件该放在哪里呢？
可以通过每个组件的<style>标签进行页面呈现的美化，但是需要对css代码进行编写。app.vue中的布局会使用到其他页面。
