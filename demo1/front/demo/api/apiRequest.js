// 对后端进行请求
import axiosInstance from './index'



const axios = axiosInstance


// 整图上传
export const postPic = (params) => {
  return axios.request({
    url: '/api/pic/',
    method: 'post',
    headers: {
      'Content-Type': 'multipart/form-data'
    },
    data: params
  })
}

// 变化检测 获取整图信息
export const getPic = () => {
  return axios.get('http://127.0.0.1:8000/api/pic/')
}

// 向后端传送图片id
export const postName = (splitData) => {
  return axios.request({
    url: '/api/pic/deal/',
    method: 'post',
    headers: {
      'Content-Type': 'multipart/form-data'
    },
    data: splitData
  })
}

// 获取拆分后的图片
export const getImages = () => {
  return axios.get('http://127.0.0.1:8000/api/split_images/')
}
