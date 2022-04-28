<template>
   <div class="hello">
     <h1>{{ msg }}</h1>
     <ul>
       <li v-for="(pic, index) in pic" :key="index" style="display: block">
         {{ index }}-{{ pic }}-
       </li>
     </ul>
     <button type="submit" @click="upPic()">上传</button>
  </div>
</template>

<script>
import {getPic,postPic} from "../../api/apiRequest";

export default {
  name: "hello",
  data() {
    return {
      msg: '图片展示',
      pic: [

      ],
      inputPic:{

      }
    }
  },
  methods: {
    loadPic() {
      getPic().then(response => {
        this.pic = response.data
      })
    },
    upPic(){
      postPic().then(response => {
        console.log(response)
        // 加载图片
        this.loadPic()
      })
    },
    created:function (){
      this.loadPic()
    }
  }
}
</script>

<style scoped>

</style>
