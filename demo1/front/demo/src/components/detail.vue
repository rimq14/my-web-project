<template>
  <div id="detail">
    <h1>{{ msg }}</h1>
    <ul>
      <li v-for="(book in books)" :key="index" style="display: block">
        {{ index }}-{{ book.name}}-{{ book.author }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "detail",
  data (){
    return{
        msg:'图书列表',
      books:[
        {}
      ]
    }
  },
  methods:{
  },
}
</script>

<style scoped>

</style>
