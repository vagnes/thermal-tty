<template>
  <div id="textbox">
    <div class="form-group">
      <textarea
        v-model="text"
        v-on:keyup.enter.ctrl.exact="sendText"
        v-class="{active: toggleBold}"
        class="form-control"
      ></textarea>
    </div>
    <div class="settings">
      <button v-on:click="sendText" class="btn">Send</button>
      <button v-on:click="sendLFCR" class="btn">LF/CR</button>
      <toggle-button
        @change="toggleBold"
        :sync="true"
        :labels="{unchecked: 'bold off', checked: 'bold on'}"
        :width="80"
      />
    </div>
  </div>
</template>

<script>
import { HTTP } from "../main";

export default {
  name: "Textbox",
  props: {},
  data() {
    return {
      text: "",
      bold: false
    };
  },
  methods: {
    sendText: function() {
      HTTP.post("/print_text/", {
        user_input: this.text
      }).then((this.text = ""));
    },
    sendLFCR: function() {
      HTTP.get("/lfcr/");
    },
    toggleBold: function(e) {
      HTTP.post("/bold/", {
        bold: e.value
      });
    }
  }
};
</script>

<style scoped>
.btn {
  margin: 5px;
}
textarea {
  width: 40vw;
  display: block;
  margin-left: auto;
  margin-right: auto;
  /* text-align: center; */
}
</style>