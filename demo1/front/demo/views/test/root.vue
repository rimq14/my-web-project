<template>
    <div>
        <!-- 设置一个导航栏放置各按钮 -->
        <el-button type="text" @click="dialog = true">添加图片</el-button>


        <el-drawer title="图片上传" :before-close="handleClose" :visible.sync="dialog" direction="ltr"
            custom-class="demo-drawer" ref="drawer">
            <div class="demo-drawer__content">
                <!-- form表单 -->
                <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px">

                    <el-form-item label="地区名称" prop="name">
                        <el-input v-model="ruleForm.name" style="width: 150px"></el-input>
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

                    <!-- <el-form-item> -->
                        <!-- <el-button type="primary" @click="submitForm('ruleForm')">上传</el-button> -->
                        <!-- <el-button @click="toDetail">完成</el-button> -->
                    <!-- </el-form-item> -->

                </el-form>
                <div class="demo-drawer__footer">
                    <el-button type="primary" @click="submitForm('ruleForm')">上传</el-button>
                    <el-button @click="cancelForm">取 消</el-button>
                    <!-- <el-button type="primary" @click="$refs.drawer.closeDrawer()" :loading="loading">{{ loading ?
                            '提交中...' : '确 定'
                    }}</el-button> -->
                </div>
            </div>
        </el-drawer>
    </div>
</template>



<script>

import { postPic } from "../../api/apiRequest";

export default {
    data() {
        return {
            dialog: false,
            loading: false,
            dialogImageUrl: '',
            dialogVisible: false,
            disabled: false,
            formLabelWidth: '80px',
            timer: null,
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
        }
    },
    methods: {
        handleClose(done) {
            if (this.loading) {
                return;
            }
            this.$confirm('确定要关闭添加图片吗？')
                .then(_ => {
                    this.loading = false;
                    this.dialog = false;
                    // this.timer = setTimeout(() => {
                    //     done();
                    //     // 动画关闭需要一定的时间
                    //     setTimeout(() => {
                    //         this.loading = false;
                    //     }, 400);
                    // }, 2000);
                })
                .catch(_ => { });
        },
        cancelForm() {
            this.loading = false;
            this.dialog = false;
            clearTimeout(this.timer);
        },
        // 上传图片
        fileChange(file) {
            this.ruleForm.image_url = file.raw
        },  // 表单信息填写
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
        },  // 提交表单
        handlePictureCardPreview(file) {
            this.dialogImageUrl = file.url;
            this.dialogVisible = true;
        },  // 缩略图可视化
    }
}
</script>