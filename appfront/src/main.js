// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router/router'

Vue.config.productionTip = false

/* eslint-disable no-new */
// 创建和挂载根实例，从而让整个应用都有路由功能
new Vue({
  // DOM元素，挂载视图模型
  el: '#app',
  router,   // 挂在路由
  render: h => h(App),

})
