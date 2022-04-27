<template>
  <div id="overview">
    <div class="container">
      <a class="navbar-brand" href="./"><strong>Boomerang</strong> UI Kit</a>
        <button class="navbar-toggler" type="button" data-action="offcanvas-open" data-target="#navbar_main" aria-controls="navbar_main" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="navbar-collapse offcanvas-collapse" id="navbar_main">
          <ul class="navbar-nav ml-auto align-items-lg-center">
            <h6 class="dropdown-header font-weight-600 d-lg-none px-0">Menu</h6>
            <li class="nav-item active">
              <a class="nav-link" href="./index.html">Overview</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbar_main_dropdown_1" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Pages</a>
              <div class="dropdown-menu" aria-labelledby="navbar_1_dropdown_1">
                <a class="dropdown-item" href="">Homepage</a>
                <a class="dropdown-item" href="">About us</a>
                <a class="dropdown-item" href="">Sign in</a>
                <a class="dropdown-item" href="">Contact</a>
              </div>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="">Docs</a>
            </li>
            <li class="nav-item">
              <a href="https://github.com/webpixels/boomerang-ui-kit/archive/master.zip" target="_blank" class="nav-link d-lg-none">Download Free</a>
              <a href="https://github.com/webpixels/boomerang-ui-kit/archive/master.zip" target="_blank" class="btn btn-sm bg-white d-none d-lg-inline-flex">Download Free</a>
            </li>
          </ul>
      </div>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: "index"
}
</script>

<style scoped>

</style>
