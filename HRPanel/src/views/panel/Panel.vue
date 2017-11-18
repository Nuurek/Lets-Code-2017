<template>
    <div class="panel_container">
        <div class="panel_infocard" @click="routeToRooms">
            <info-card :frontType="'text'"
      :frontTitle="panelInfocard.front.title"
      :frontData="panelInfocard.front.message"
      :backTitle="panelInfocard.back.title"
      :backData="panelInfocard.back.message" />
        </div>
        <div class="panel_infocard" @click="routeToSurvey">
            <info-card :frontType="'text'"
      :frontTitle="surveyInfocard.front.title"
      :frontData="surveyInfocard.front.message"
      :backTitle="surveyInfocard.back.title"
      :backData="surveyInfocard.back.message" />
        </div>
        
    </div>
</template>

<script>
import InfoCard from "vue-info-card";

export default {
  name: "panel",
  components: {
    InfoCard
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
          message:
            "Panel zarządzania ankietyzacją jednostki ludzkiej."
        },
        back: {
          title: "Ankiety",
          message:
            "Panel zarządzania ankietyzacją jednostki ludzkiej."
        }
      }
    };
  },
  computed: {},
  methods: {
      routeToRooms() {
          this.$router.push({ path: 'rooms' })
      },
      routeToSurvey() {
          this.$router.push({ path: 'survey'})
      }
  }
};
</script>

<style lang="scss">
@import "./Panel.scss";
</style>