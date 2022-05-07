<template>
  <div class="detail">
    <el-container>
      <el-header>Header</el-header>
      <el-container>
        <el-aside width="200px">Aside</el-aside>
        <el-main>
          图片<img :src="http://127.0.0.1:8000/media/pictures/e5eae28a21.png">
        </el-main>
      </el-container>
    </el-container>

  </div>
</template>

<script>
export default {
  name: "detail"
}
</script>

<style scoped>

</style>
