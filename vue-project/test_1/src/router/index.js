import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '../components/HelloWorld'
import Menu from '../components/Menu'
import detail from "../components/detail";

Vue.use(Router)

export default new Router({
  routes: [
    // 主页显示
    {
      path: '/',
      name: 'HelloWorld',
      component:HelloWorld
    },
    {
      path:'/menu',
      name:'menu',
      component:Menu
    },
    {
      path:'/detail',
      name:'detail',
      component:detail
    },
  ]
})
