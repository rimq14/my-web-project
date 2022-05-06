// 对axios进行配置
import Vue from 'vue'
import Axios from 'axios';


// 自定义配置新建一个axios实例
const axiosInstance = Axios.create({
  withCredentials: true,    // 表示跨域请求时是否需要使用凭证，默认值为false
  responseType: 'json',     // 浏览器将要响应的数据类型，默认值为json
  headers: {
    'Content-Type': 'application/json'
  },
})

// 通过拦截器处理csrf问题，请求拦截器
axiosInstance.interceptors.request.use((config) => {
  // 发送请求前做些什么
  config.headers['X-Requested-With'] = 'XMLHttpRequest'
  const regex = /.*csrftoken=([^;.]*).*$/
  config.headers['X-CSRFToken'] = document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1]
  return config;
},  // 对请求错误做什么
  function (error) {
  return Promise.reject(error)
})

// 相应拦截器
axiosInstance.interceptors.response.use(response => {
    // 对响应数据做点什么
    return response
  },
  // 对响应错误做点什么
  error => {
    return Promise.reject(error)
  }
)

Vue.prototype.axios = axiosInstance

export default axiosInstance
