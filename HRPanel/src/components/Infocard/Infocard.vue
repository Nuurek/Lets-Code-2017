<template>
  <div class="infocard__container">
      <div class="infocard__header infocard__section">{{ header }}</div>
      <div class="infocard__icon infocard__section">
          <icon :name="iconName" scale="5"></icon>
      </div>
      <div class="infocard__content infocard__section">{{ content }}</div>
  </div>
</template>
<script>
export default {
  name: "infocard",
  props: {
    header: "",
    content: "",
    iconName: ""
  }
};
</script>
<style lang="scss">
@import "./Infocard.scss";
</style>
