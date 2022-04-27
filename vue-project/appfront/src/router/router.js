import Vue from 'vue'
import Router from 'vue-router'


// 1.安装路由功能(使用模块化机制编程)
Vue.use(Router)

// 2.配置并导出创建的路由实例
export default new Router({
    routes: [
      {
        name:'index',
        path: '/',
        components: () => import('../components/Overview/index'),
      },
      {
        name:'',  // 是当前路由的标识名称
        path: "/welcome",
        components: () => import('../components/Context/index'),
        props: true       //props为true时，可以将动态路由的值传递给相应的组件
      },
      {
        path: "/menu",
        components: () => import('../components/Menu/index')
      },

    ]
  }
)




