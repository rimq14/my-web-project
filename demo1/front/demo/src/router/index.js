import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '../components/HelloWorld'
import hello from "../components/hello"
import detail from "../components/detail";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path:'/hello',
      name:'hello',
      component:hello
    },
    {
      path:'/detail',
      name:'detail',
      component:detail
    }
  ]
})
