<template>
  <div id="textbox">
    <div class="form-group">
      <textarea v-model="text" v-on:keyup.enter.ctrl.exact="sendText" class="form-control"></textarea>
    </div>
    <div class="settings">
      <button v-on:click="sendText" class="btn">Send</button>
      <button v-on:click="sendLFCR" class="btn">LF/CR</button>
    </div>
    <div class="toggles">
      <div class="toggle">
        <span>Bold</span>
        <toggle-button @change="sendFormat" v-model="format.bold" :sync="true" :labels="true"/>
      </div>
      <div class="toggle">
        <span>Center</span>
        <toggle-button @change="sendFormat" v-model="format.center" :sync="true" :labels="true"/>
      </div>
      <div class="toggle">
        <span>2x Height</span>
        <toggle-button @change="sendFormat" v-model="format.height2x" :sync="true" :labels="true"/>
      </div>
      <div class="toggle">
        <span>Underline</span>
        <toggle-button @change="sendFormat" v-model="format.underline" :sync="true" :labels="true"/>
      </div>
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
      format: {
        bold: false,
        center: false,
        height2x: false,
        underline: false
      }
    };
  },
  mounted() {
    this.sendFormat();
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
    sendFormat: function() {
      HTTP.post("/format/", this.format);
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

.toggles {
  display: flex;
  justify-content: center;
  padding: 20px;
}

.toggle {
  padding-right: 20px;
}

.toggle span {
  font-size: 15pt;
  margin-right: 5px;
}
</style>