<template>
  <div class="rooms__container">
      <div class="rooms__table animated fadeIn">
          <div class="room__table--header">
              <div class="room__id">DeviceId</div>
              <div class="room__name">Room</div>
              <div class="room__count">Count</div>
          </div>
          <div class="room__table--row" v-for="room in rooms" :key="room.piId" @click="show(room)">
              <div class="room__id">{{ room.piId }}</div>
              <div class="room__name">{{ room.roomName }}</div>
              <div class="room__count">{{ room.count }} / {{ room.max }}</div>
          </div>
      </div>
      <modal name="hello-world" width="80%">
        <div class="modal__room_id">Device with ID: <span class="bold-text">{{ room.piId }}</span></div>
        <hr>
        <div class="modal__room_name">Registered for room: <span class="bold-text">{{ room.roomName }}</span></div>
        <hr>
        <div class="room__room_count">There is (approximately) <span class="bold-text">{{ room.count }}</span> people in the room</div>
        <hr>
        <span class="bold-text">{{ placesLeft }}</span>
      </modal>
  </div>
</template>
<script>
export default {
  data() {
    return {
      room: {
        piId: '',
        roomName: '',
        count: 0,
        max: 0
      }
    }
  },
  computed: {
    rooms() {
      return this.$store.state.rooms.rooms;
    },
    placesLeft() {
      const placesLeft = this.room.max - this.room.count;
      return placesLeft > 0 ? `There is ${placesLeft} places left in the room` : 'There is too many people in the room!';
    }
  },
  methods: {
    show(room) {
      debugger;
      this.room = room;
      this.$modal.show("hello-world");
    },
    hide() {
      this.$modal.hide("hello-world");
    }
  }
};
</script>
<style lang="scss">
@import "./Rooms.scss";
</style>
