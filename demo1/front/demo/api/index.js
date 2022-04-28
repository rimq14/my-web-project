// 对axios进行配置
import Vue from 'vue'
import Axios from 'axios';

// 自定义配置新建一个axios实例
const axiosInstance = Axios.create({
    withCredentials: true
})

// 通过拦截器处理csrf问题，这里的正则和匹配下标可能需要根据实际情况小改动
axiosInstance.interceptors.request.use((config) => {
    // 发送请求前做些什么
    config.headers['X-Requested-With'] = 'XMLHttpRequest'
    const regex = /.*csrftoken=([^;.]*).*$/
    config.headers['X-CSRFToken'] = document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1]
    return config
})

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
