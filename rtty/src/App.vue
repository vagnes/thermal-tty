<template>
<div id="app">
  <head>
    <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
      integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO"
      crossorigin="anonymous"
    >
  </head>
  <Header headline="RTTY" subtitle="The thermal printer communicator"/>
  <Textbox/>
</div>
</template>

<script>
import Header from "./components/Header.vue";
import Textbox from "./components/Textbox.vue";

export default {
  name: "app",
  components: {
    Header,
    Textbox
  }
};
</script>

<style>
#app {
  font-family: monospace;
  text-align: center;
  color: #2c3e50;
  margin-top: 50px;
}
</style>
