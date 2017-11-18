<template>
  <div class="rooms__container">
      <div class="add_room" @click="showAddRoom">
        <icon name="plus" label="Add a room" scale="2"></icon>
        <p>Add new monitoring device</p>
      </div>
      <div class="rooms__table animated fadeIn">
          <div class="room__table--header">
              <div class="room__id">DeviceId</div>
              <div class="room__name">Room</div>
              <div class="room__count">Count</div>
          </div>
          <div class="room__table--row" v-for="room in rooms" :key="room.piId" @click="showDetails(room)">
              <div class="room__id">{{ room.piId }}</div>
              <div class="room__name">{{ room.roomName }}</div>
              <div class="room__count">{{ room.count }} / {{ room.max }}</div>
          </div>
      </div>

      <modal name="room-details" width="80%">
        <div class="modal__room_id">Device with ID: <span class="bold-text">{{ room.piId }}</span></div>
        <hr>
        <div class="modal__room_name">Registered for room: <span class="bold-text">{{ room.roomName }}</span></div>
        <hr>
        <div class="room__room_count">There is (approximately) <span class="bold-text">{{ room.count }}</span> people in the room.</div>
        <hr>
        <span class="bold-text">{{ placesLeft }}.</span>
      </modal>

      <modal name="add-room" width="80%" >
        <div class="modal__add-room">
          <div class="add__room--header">Add new room form</div>
          <hr>
          <span>
          <label for="roomName">Room name: </label>
          <input v-model="newRoom.roomName" placeholder="Kitchen" name="roomName">
        </span>
        <span>
          <label for="deviceId">DeviceID: </label>
          <input v-model="newRoom.deviceId" placeholder="1234567890ABCDEF" name="deviceId">
        </span>
        <span>
          <label for="capacity">Capacity: </label>
          <input v-model="newRoom.capacity" placeholder="edit me" type="number" min="0" max="20" name="capacity"> 
        </span>
        </div>
      </modal>
  </div>
</template>
<script>
export default {
  data() {
    return {
      room: {
        piId: "",
        roomName: "",
        count: 0,
        max: 0
      },
      newRoom: {
        roomName: "",
        deviceId: "",
        capacity: 0
      }
    };
  },

  computed: {
    rooms() {
      return this.$store.state.rooms.rooms;
    },
    placesLeft() {
      const placesLeft = this.room.max - this.room.count;
      return placesLeft > 0
        ? `There is ${placesLeft} places left in the room`
        : "There is too many people in the room!";
    }
  },

  methods: {
    showDetails(room) {
      this.room = room;
      this.$modal.show("room-details");
    },
    hideDetails() {
      this.$modal.hide("room-details");
    },
    showAddRoom() {
      this.$modal.show("add-room");
    },
    hideAddRoom() {
      this.$modal.hide("add-room");
    },
    submitAddRoom() {
      //  submit
      this.hideAddRoom();
    }
  },

  created() {
    this.$store.dispatch("getRooms");
  }
};
</script>
<style lang="scss">
@import "./Rooms.scss";
</style>
