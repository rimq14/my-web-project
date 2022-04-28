// 对后端进行请求
import axiosInstance from './index'

const axios = axiosInstance
// 图片数据
// axios get
export const getPic = () => {
  return axios.get('http://127.0.0.1:8000/api/pic/')
}

// axios post
export const postPic = () => {
  return axios.post('http://127.0.0.1:8000/api/pic/')
}

//书本数据
// axios get方法
export const getBooks = () => {
  return axios.get(`http://localhost:8000/api/books/`)
}

// axios post方法
export const postBook = (bookName, bookAuthor) => {
  return axios.post(`http://localhost:8000/api/books/`,
    {'name': bookName, 'author': bookAuthor})
}
