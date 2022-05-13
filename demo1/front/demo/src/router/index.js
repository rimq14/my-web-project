import Vue from 'vue'
import Router from 'vue-router'


Vue.use(Router)

export default new Router({
  mode:'history',
  routes: [
    {
      path: '/',
      redirect:'/index'
    },    //  重定向
    {
      path:'/index',
      name:'home',
      component: () => import('../../views/Home/index')
    },   // 主页
    {
      path:'/menu',
      name:'menu',
      component:() => import('../../views/Content/index')
    },  // 功能选择页
    {
      path:'/experience',
      name:'experience',
      component:() => import('../../views/Experience/root'),
      children:[
        {
          path: 'change_detection',
          name:'change_detection',
          component:() => import('../../views/Experience/change_detection')
        },
        {
          path: 'target_detection',
          name:'target_detection',
          component:() => import('../../views/Experience/target_detection')
        },
        {
          path: 'object_classification',
          name: 'object_classification',
          component:() => import('../../views/Experience/object_classification')
        }
      ]
    },  // 体验中心
    {
      path: '/change_detection',
      name: 'upload',
      component: () => import('../../views/change_detection/upload')
    },  // 变化检测上传图片
    {
      path:'/change_detection/operation',
      name:'operation',
      component:() => import('../../views/change_detection/operation')
    },    // 图片显示及后续操作
  ]
})
