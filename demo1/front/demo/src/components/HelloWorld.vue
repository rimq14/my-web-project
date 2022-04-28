<template>
  <div class="hello">
      <div>
         <router-link :to="{path:'/detail'}" class="btn btn-primary" role="button" target="_blank">books</router-link>
        <router-link :to="{path:'/hello'}" class="btn btn-primary" role="button" target="_blank">pics</router-link>
      </div>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  /*body{*/
  /*  background-image: url('');*/
  /*}*/
</style>
