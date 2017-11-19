<template>
  <div id="app">
    <header class="nav_container">
      <router-link to="/panel" class="header-logo">
      <span><icon name="briefcase"></icon></span>
      <span>OfficeLink</span>
      </router-link>
      <router-link to="/rooms" class="nav_elem">rooms</router-link>
      <router-link to="/survey" class="nav_elem">surveys</router-link>
    </header>
    <!-- <quick-menu :menu-count='count' :icon-class='icons' :menu-url-list='list'></quick-menu>     -->
    <main class="body_container">
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
import quickMenu from 'vue-quick-menu'
export default {
  name: 'app',
  components: {
    quickMenu
  },
  data() {
    return {
    }
  }
}
</script>

<style lang="scss">
@import './App.scss';
</style>
