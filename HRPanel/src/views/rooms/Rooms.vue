<template>
  <div class="rooms_container">

  </div>
</template>
<script>
export default {
  computed: {
      rooms() {
          return this.$store.state.rooms.room1;
      }
  }
}
</script>
<style lang="scss">
@import './Rooms.scss';
</style>
