<template>
  <div class="index">
    <el-container>
      <el-main>
        <el-empty>
          <el-upload 
            class="upload-picture" 
            action="none" 
            :on-change="fileChange" 
            :auto-upload="false"
            :limit="1"
            >
            <el-button slot="trigger" type="file">选取文件</el-button>
            <el-button @click="toDetail">上传文件</el-button>
            <div slot="tip" class="el-upload__tip">只能上传jpg/png文件</div>
          </el-upload>
        </el-empty>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import { postPic } from "../../api/apiRequest";

export default {
  name: "index",
  data() {
    return {
      fileList: []     // 文件列表
    };
  },
  methods: {
    // 上传图片
    fileChange(data) {
      console.log(data)

      let file = data.raw;
      console.log(file)
      // 请求体编码,使用form-data库
      let formData = new FormData()

      formData.append("image_url", file)  // 构造formData数据

      postPic(formData).then(res => {    // 上传formData数据,formData作为实参
        console.log(res)
      })
        .catch(function (error) {     // 错误处理
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
    toDetail() {
      this.$router.push('/change_detection/operation')
    }
  },
}
</script>

<style scoped>
</style>
