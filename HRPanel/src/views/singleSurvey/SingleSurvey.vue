<template>
  <div class="single-survey__container animated fadeIn">
      <div class="single-survey__header form-header">
          <h2>Single Survey</h2>
      </div>
      <span class="form-conatiner">
          <p v-for="user in getUsers" :key="user.username">{{ user.username }}</p>
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
                    v-model="text"
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
      e1: null,
      items: [{ text: "Binary" }, { text: "Score" }],
      row: null,
      text: ""
    };
  },
  methods: {
    submit() {
      const survey = {
        type: 0,
        text: this.text,
        username: "rjwaberski"
      };
      this.$store.dispatch("addIndividualSurvey", survey);
    //   this.$notify({
    //     title: "Important message",
    //     text: "Hello user! This is a notification!"
    //   });
    }
  },
  created() {
    this.$store.dispatch("getUsers");
  },
  computed: {
    getUsers() {
      return this.$store.getters.users;
    }
  }
};
</script>
<style lang="scss">
@import "./SingleSurvey.scss";
</style>
