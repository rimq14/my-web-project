<template>
<div>
<h1>我是B组件</h1>
<router-link :to="{path:'/clickMaskA'}"><h3>跳转到回A组件</h3></router-link>
<div @click="show = true"><h2>点击展示弹窗(遮罩层)</h2></div>
<div class="model" v-if="show">
    <div  @click="show = false"><h3>点击关闭弹窗(遮罩层)</h3></div>
    <ul >
        <li><h3>list</h3></li>  
        <li><h3>list</h3></li> 
        <li><h3>list</h3></li> 
        <li><h3>list</h3></li>  
        <li><h3>list</h3></li> 
        <li><h3>list</h3></li>   
    </ul>
</div>
</div>    
</template>

<script>
    export default{
        data(){
            return {
               show:false 
            }
        },
        beforeRouteLeave (to, from, next) {
            // ...
            if(this.show){
                this.show=false
                next(false);
            }else{
                next(true);
            }

           
        }   
    }
</script>   

<style >
   .model{
       z-index:100;
       width:100%;
       height:100%;
       background:rgba(33,33,33,1);
       position:absolute;
       top:0;
   } 
</style>