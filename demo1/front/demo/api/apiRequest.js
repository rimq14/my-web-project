// 对后端进行请求
import axiosInstance from './index'



const axios = axiosInstance
// 图片数据
// axios get
export const getPic = () => {
  return axios.get('http://127.0.0.1:8000/api/pic/')
}

// axios post
export const postPic = (params) => {
  return axios.request({
    url:'/api/pic/',
    method:'post',
    headers:{
      'Content-Type':'multipart/form-data'
    },
    data:params
  })
}


