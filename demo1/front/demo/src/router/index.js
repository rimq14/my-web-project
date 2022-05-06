import Vue from 'vue'
import Router from 'vue-router'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect:'/index'  //  重定向
    },
    {
      path:'/index',  // 主页
      name:'home',
      component: () => import('../../views/Home/index')
    },
    {
      path:'/menu',  // 功能选择页
      name:'menu',
      component:() => import('../../views/Content/index')
    },
    {
      path:'/experience',   // 体验中心
      name:'experience',
      component:() => import('../../views/Experience/index')
    },
    {
      path:'/change_detection',   // 变化检测
      name:'change_detection',
      component:() => import('../../views/change_detection/index')
    }
  ]
})
