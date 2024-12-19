import { createApp } from "vue";
import App from "./App.vue";
import "./index.css";
import Vuetify from "vuetify";
import "vuetify/styles";

const app = createApp(App);

app.use(Vuetify);

app.mount("#app");
