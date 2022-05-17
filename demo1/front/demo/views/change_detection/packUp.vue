<template>
  <div class="curr-contents" ref="outerDiv">
    <div class="show-areas" v-show="openflags">
      <!-- 内容插槽 -->
      <slot></slot>
    </div>
    <div class="pack-ups" ref="packUps" @click="handlePack">
      <i class="icon-bar el-icon-d-arrow-left"></i>
    </div>
  </div>
</template>
<script>
export default {
  name:'',
  data() {
    return {
      liConWidth:500, // 左边容器的宽度
      openflags:true,
    }
  },
  methods: {
    // 点击展开 折叠
    handlePack(){
      this.openflags=!this.openflags
      const liCon = this.$refs.outerDiv
      let packUps=this.$refs.packUps
      if (this.openflags) { // 展开
        liCon.style.width = 'auto'
        liCon.style.width = this.liConWidth + 'px'
        packUps.style.position='absolute'
        packUps.style.left='auto'
        packUps.style.right='0'
      } else { // 收起
        liCon.style.width = 0 + 'px'
        packUps.style.position='absolute'
        packUps.style.right='auto'
        packUps.style.left='0'
      }
    }
  }
}
</script>
<style scoped>
 .curr-contents{
    width: 500px;
    height: auto;
    position: relative;
    background: #333333;
    transition: all .5s ease-in-out;
    padding: 0 10px;
    /* transition: height .3s; */
  }
  .curr-contents .pack-ups{
    height: auto;
    background: #E9EEF3;
    position: absolute;
    right: 0;
    top: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    transition: all .5s ease-in-out;
  }
  .show-areas{
    transition: all .5s ease-in-out;
  }
</style>
