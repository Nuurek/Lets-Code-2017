<template>
  <div class="group-survey__container animated fadeIn">
      <div class="group-survey__header form-header">
          <h2>Group Survey</h2>
      </div>
      <span class="form-conatiner">
          <v-card color="white" flat>
            <v-card-text>
                    <v-radio-group v-model="row" row>
                    <v-radio label="Binary" value="0" ></v-radio>
                    <v-radio label="Score" value="1"></v-radio>
                    </v-radio-group>
            <v-text-field
                    name="input-1"
                    label="Text"
                    textarea
                ></v-text-field>
            </v-card-text>
                <v-btn
        @click="submit"
        color="primary"
        class="submit-survey">
        submit
        </v-btn>
    </v-card>    
      </span>
  </div>
</template>
<script>
export default {
  data() {
    return {
      row: null
    };
  },
  methods: {
    submit() {
      const scope = this;
      setTimeout(function() {
        scope.$router.push({ path: "" });
      }, 500);
    }
  },
  created() {
    this.$store.dispatch("getUsers");
  }
};
</script>
<style lang="scss">
@import "./GroupSurvey.scss";
</style>
