<!--显示模板-->
<template>
  <div class="hello">
    <!--文本插值-->
    <h1>{{ msg }}</h1>
    <!-- show books list -->
    <ul>
      <!-- 指令是带有v-前缀的特殊属性-->
      <li v-for="(book, index) in books" :key="index" style="display:block">
        {{index}}-{{book.name}}--{{book.author}}
      </li>
    </ul>
    <!-- form to add a book -->
    <form action="">
      <!--在 input 输入框中我们可以使用 v-model 指令来实现双向数据绑定：-->
      输入书名：<input type="text" placeholder="book name" v-model="inputBook.name"><br>
      输入作者：<input type="text" placeholder="book author" v-model="inputBook.author"><br>
    </form>
    <!-- v-on 缩写   v-on:click=""  ==  @click=""-->
    <button type="submit" @click="bookSubmit()">submit</button>
  </div>
</template>

<!--处理逻辑-->
<script>
import {getBooks, postBook} from '../api/api.js'
export default {
  name: 'HelloWorld',
  // 定义属性，并设置初始值
  data() {
    return {
      msg: 'web前端',
      // books list data
      books: [
        {name: 'test', author: 't'},
        {name: 'test2', author: 't2'}
      ],
      // book data in the form
      inputBook: {
        "name": "",
        "author": "",
      }
    }
  },
  // 使用的函数
  methods: {
    // load books list when visit the page
    loadBooks() {
      getBooks().then(response => {
        this.books = response.data
      })
    },
    // add a book to backend when click the button
    bookSubmit() {
      postBook(this.inputBook.name, this.inputBook.author).then(response => {
        console.log(response)
        this.loadBooks()
      })
    }
  },
  created: function () {
    this.loadBooks()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
