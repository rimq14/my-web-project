<template>
  <div class="index">

    <el-upload
      class="upload-picture"
      ref="uppic"
      action="http://127.0.0.1:8000/api/pic/"
      :file-list="fileList"
      :auto-upload="false">
      <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
      <el-button type="success" @click="upload">点击上传</el-button>
      <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
    </el-upload>
  </div>
</template>

<script>
import { postPic } from "../../api/apiRequest";

export default {
  name: "index",
  data() {
    return {
      fileList: [{}]
    };
  },
  methods: {
    // 上传图片
    upload() {
      // 请求体编码,使用form-data库
      const formData = new FormData()

      formData.append('img', this.fileList)  // 构造formData数据

      postPic(formData).then(res => {           // 上传formData数据,formData作为实参
        console.log(res.status)

      }).catch(function (error) {
        if (error.response) {
          // 请求成功发出且服务器也响应了状态码，但状态代码超出了 2xx 的范围
          console.log(error.response.data);
          console.log(error.response.status);
          console.log(error.response.headers);
        } else if (error.request) {
          console.log(error.request);
        } else {
          // 发送请求时出了点问题
          console.log('Error', error.message);
        }
        console.log(error.config);
      });
    },
  }
}
</script>

<style scoped>

</style>
