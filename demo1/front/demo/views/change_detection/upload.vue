<template>
  <div class="index">
    <el-container>
      <el-main>
        <!-- form表单 -->
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px">

          <el-form-item label="地区名称" prop="name">
            <el-input v-model="ruleForm.name" style="width: 300px"></el-input>
          </el-form-item>

          <el-form-item label="上传图片" prop="image_url">
            <!-- 图片选择 -->
            <el-upload list-type="picture-card" class="image-uploader" action="none" :on-change="fileChange"
              :auto-upload="false">
              <i class="el-icon-plus"></i>
              <div slot="file" slot-scope="{file}">
                <img class="el-upload-list__item-thumbnail" :src="file.url" alt="">
                <span class="el-upload-list__item-actions">
                  <span class="el-upload-list__item-preview" @click="handlePictureCardPreview(file)">
                    <i class="el-icon-zoom-in"></i>
                  </span>
                </span>
              </div>
            </el-upload>
            <!-- 图片缩略图显示 -->
            <el-dialog :visible.sync="dialogVisible">
              <img width="100%" :src="dialogImageUrl" alt="">
            </el-dialog>

          </el-form-item>

          <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')">上传</el-button>
            <el-button @click="toDetail">完成</el-button>
          </el-form-item>

        </el-form>
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
      dialogImageUrl: '',
      dialogVisible: false,
      disabled: false,
      ruleForm: {
        name: '',
        image_url: ''
      },
      rules: {
        name: [
          { required: true, message: '请输入图片所属地区名称', trigger: 'blur' },
          { max: 5, message: '长度少于5 个字符', trigger: 'blur' }
        ],
        image_url: [
          { required: true, message: '请选择图片', trigger: 'blur' }
        ]
      }
    };
  },
  methods: {
    // 上传图片
    fileChange(file) {
      this.ruleForm.image_url = file.raw
    },
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          // 请求体编码,使用form-data库
          let formData = new FormData()
          formData.append("name", this.ruleForm.name)
          formData.append("image_url", this.ruleForm.image_url)  // 构造formData数据
          postPic(formData).then(res => {    // 上传formData数据,formData作为实参
            console.log(res)
          })
          alert('上传成功');
        } else {
          console.log('上传失败');
          return false;
        }
      });
    },
    handlePictureCardPreview(file) {
      this.dialogImageUrl = file.url;
      this.dialogVisible = true;
    },
    toDetail() {
      this.$router.push('/change_detection/operation')
    }
  },
}
</script>

<style scoped>
.image-uploader {
  border-color: blue;
}
</style>
