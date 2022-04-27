import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import clickMaskA from '@/components/clickMaskA'
import clickMaskB from '@/components/clickMaskB'
import chart from '@/components/chart'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/clickMaskA',
      name: 'clickMaskA',
      component: clickMaskA
    },
    {
      path: '/clickMaskB',
      name: 'clickMaskB',
      component: clickMaskB
    },
    {
      path: '/chart',
      name: 'chart',
      component: chart
    }        
  ]
})
