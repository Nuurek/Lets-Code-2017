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
                    v-model="text"
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
      row: null,
      text: ""
    };
  },
  methods: {
    submit() {
      const survey = {
        type: 0,
        text: this.text
      };
      this.$store.dispatch("addGroupSurvey", survey).then(
        response => {
          this.$notify({
            title: "Succes",
            text: "You added new group survey!"
          });
        },
        error => {
          this.$notify({
            title: "Error",
            text: "Something went wrong!",
            type: 'error'
          });
        }
      );
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
