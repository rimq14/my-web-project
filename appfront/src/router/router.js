import Vue from 'vue'
import Router from 'vue-router'


// 1.安装路由功能(使用模块化机制编程)
Vue.use(Router)

// 2.配置并导出创建的路由实例
export default new Router({
  routes: [
    {
      path: "/demo1/:id",
      components:() => import('../components/demo1'),
      props: true       //props为true时，可以将动态路由的值传递给相应的组件
    },
    {
      path: "/Menu",
      components:() => import('../components/Menu')
    },
    {
      path: "/demo3/:id",
      name: "test",    //name属性是给路由起别名，方便用js的方式去跳转
      components:() => import('../components/demo3')
    },
  ]
},
)




