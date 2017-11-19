<template>
  <div class="login__container">
      <div class="login-form">
        <v-form v-model="valid" ref="form" lazy-validation>
    <v-text-field
      label="Login"
      v-model="name"
      :rules="nameRules"
      :counter="10"
      required
      autofocus
    ></v-text-field>
    <v-text-field
      label="Password"
      v-model="email"
      type="password"
      :rules="emailRules"
      required
    ></v-text-field>
    <v-btn
      @click="submit"
      :disabled="!valid"
      color="primary"
    >
      submit
    </v-btn>
    <v-btn @click="clear">clear</v-btn>
  </v-form>
      </div>
  </div>
</template>
<script>
export default {
  data: () => ({
    valid: true,
    name: "admin",
    nameRules: [v => !!v || "Login is required"],
    email: "avfwfefwfwews",
    emailRules: [v => !!v || "Password is required"],
    select: null,
    checkbox: false
  }),
  methods: {
    submit() {
        const scope = this;
      setTimeout(function() {
        scope.$router.push({ path: "panel" });
      }, 2000);
    },
    clear() {
      this.$refs.form.reset();
    }
  }
};
</script>
<style lang="scss">
@import "./Login.scss";
</style>
