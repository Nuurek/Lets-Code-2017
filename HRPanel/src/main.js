// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import Vuetify from 'vuetify'
import Notifications from 'vue-notification'

import 'vue-awesome/icons'
import Icon from 'vue-awesome/components/Icon'

import 'animate.css/animate.min.css'
import VModal from 'vue-js-modal'

Vue.component('icon', Icon)
Vue.use(VModal)
Vue.use(Vuetify)
Vue.use(Notifications)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
