<template>
  <div class="rooms__container">
      <div class="add_room animated fadeInUp" @click="showAddRoom">
        <icon name="plus" label="Add a room"></icon>
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

      <modal name="add-room" width="80%" height="auto">
        <div class="modal__add-room">
        <v-text-field
            label="Room"
            v-model="newRoom.name"
            :rules="nameRules"
            required
          ></v-text-field>
          <v-text-field
            label="Device ID"
            v-model="newRoom.deviceId"
            :rules="idRules"
            :counter="16"
            required
          ></v-text-field>
          <v-text-field
            label="Capacity"
            v-model="newRoom.capacity"
            :rules="nameRules"
            type="number"
            min="0"
            max="20"
            required
          ></v-text-field>

          <div class="btn-footer">
            <v-btn @click="submitForm"
              :disabled="!checkIfValidForm">
            submit
          </v-btn>
          <v-btn @click="hideAddRoom">cancel</v-btn>
          </div>
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
      },

      nameRules: [v => !!v || "Room name is required"],
      idRules: [
        v => !!v || "Device ID is required",
        v => (v && v.length <= 16) || "Name must be less than 10 characters"
      ]
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
    submitForm() {
      //  submit if valid
      if (this.checkIfValidForm()) {
        this.$store.dispatch("addRoom", this.newRoom);
        this.hideAddRoom();
      }
    },
    checkIfValidForm() {
      return (
        this.newRoom.roomName != null &&
        this.newRoom.deviceId != null &&
        this.newRoom.capacity != null
      );
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
