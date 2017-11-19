<template>
    <div class="panel_container">
        <div class="panel_infocard animated fadeIn" @click="routeToRooms">
            <infocard header="Rooms" content="Administration panel for rooms section" iconName="map-marker"></infocard>
        </div>
        <div class="panel_infocard animated fadeIn" @click="routeToSurvey">
            <infocard header="Surveys" content="Administration panel for survey section" iconName="file-text-o"></infocard>
        </div>
    </div>
</template>

<script>
import Infocard from "@/components/Infocard/Infocard";
export default {
  name: "panel",
  components: {
    Infocard
  },
  data() {
    return {};
  },
  computed: {},
  methods: {
    routeToRooms() {
      const scope = this;
      setTimeout(function() {
        scope.$router.push({ path: "rooms" });
      }, 500);
    },
    routeToSurvey() {
      const scope = this;
      setTimeout(function() {
        scope.$router.push({ path: "survey" });
      }, 500);
    }
  }
};
</script>

<style lang="scss">
@import "./Panel.scss";
</style>