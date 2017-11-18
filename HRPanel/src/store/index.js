import Vue from 'vue'
import Vuex from 'vuex'

// import * as actions from './actions'
// import * as getters from './getters'

import rooms from './modules/rooms'

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        rooms
    }
})