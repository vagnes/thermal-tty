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
    <br>
    <br>
    <h2>Send a barcode</h2>
    <div class="form-group">
      <textarea
        v-model="barcode.text"
        v-on:keyup.enter.ctrl.exact="sendBarcode"
        class="form-control"
      ></textarea>
    </div>
    <div class="settings">
      <button v-on:click="sendBarcode" class="btn">Send</button>
    </div>
    <multiselect v-model="barcode.selected_type" :options="barcode.types"></multiselect>
  </div>
</template>

<script>
import { HTTP } from "../main";
import Multiselect from "vue-multiselect";

export default {
  name: "Textbox",
  components: { Multiselect },
  props: {},
  data() {
    return {
      text: "",
      barcode: {
        text: "",
        selected_type: "UPC_E",
        types: [
          "UPC_A",
          "UPC_E",
          "EAN13",
          "EAN8",
          "CODE39",
          "I25",
          "CODEBAR",
          "CODE93",
          "CODE128",
          "CODE11",
          "MSI"
        ]
      },
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
    sendBarcode: function() {
      HTTP.post("/print_barcode/", {
        user_input: this.barcode.text,
        barcode_type: this.barcode.selected_type
      }).then((this.barcode.text = ""));
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