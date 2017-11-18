<template>
  <div id="app">
    <header class="nav_container">
      <router-link to="/" class="header-logo">
      <span><icon name="briefcase"></icon></span>
      <span>OfficeLink</span>
      </router-link>
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
      count: 4,
      icons: [],
      list: ['/panel', '234', '67567', '456']
    }
  }
}
</script>

<style lang="scss">
@import './App.scss';
</style>
