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
import InfoCard from "vue-info-card";
import Infocard from "@/components/Infocard/Infocard";
export default {
  name: "panel",
  components: {
    Infocard
  },
  data() {
    return {
      panelInfocard: {
        front: {
          title: "Pokoje",
          message:
            "Panel zarządzania przepływem jednostki ludzkiej w środowisku biznesowo-gastronomicznym."
        },
        back: {
          title: "Pokoje",
          message:
            "Panel zarządzania przepływem jednostki ludzkiej w środowisku biznesowo-gastronomicznym."
        }
      },
      surveyInfocard: {
        front: {
          title: "Ankiety",
          message: "Panel zarządzania ankietyzacją jednostki ludzkiej."
        },
        back: {
          title: "Ankiety",
          message: "Panel zarządzania ankietyzacją jednostki ludzkiej."
        }
      }
    };
  },
  computed: {},
  methods: {
    routeToRooms() {
      this.$router.push({ path: "rooms" });
    },
    routeToSurvey() {
      this.$router.push({ path: "survey" });
    }
  }
};
</script>

<style lang="scss">
@import "./Panel.scss";
</style>