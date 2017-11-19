<template>
  <div class="survey_container">
      <div class="survey_infocard animated fadeIn" @click="routeToSingleSurvey">
            <infocard header="Individual" content="Administration panel for rooms section" iconName="user"></infocard>
        </div>
        <div class="survey_infocard animated fadeIn" @click="routeToManySurvey">
            <infocard header="Group" content="Administration panel for survey section" iconName="users"></infocard>
        </div>
  </div>
</template>

<script>
import Infocard from "@/components/Infocard/Infocard";
export default {
  components: {
    Infocard
  },
  methods: {
    routeToSingleSurvey() {
      const scope = this;
      setTimeout(function() {
        scope.$router.push({ path: "survey/single" });
      }, 500);
    },
    routeToManySurvey() {
      const scope = this;
      setTimeout(function() {
        scope.$router.push({ path: "survey/group" });
      }, 500);
    }
  }
};
</script>

<style lang="scss">
@import "./Survey.scss";
</style>
