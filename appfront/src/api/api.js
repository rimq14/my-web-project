// 对后端进行请求
import axiosInstance from './index'

const axios = axiosInstance

// axios get方法
export const getBooks = () => {
  return axios.get(`http://localhost:8000/api/books/`)
}

// axios post方法
export const postBook = (bookName, bookAuthor) => {
  return axios.post(`http://localhost:8000/api/books/`,
    {'name': bookName, 'author': bookAuthor})
}
