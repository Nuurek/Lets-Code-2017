import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/Hello'

import Panel from '@/views/Panel/Panel'
import Rooms from '@/views/Rooms/Rooms'
import Survey from '@/views/Survey/Survey'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'panel',
      component: Panel
    },
    {
      path: '/panel',
      name: 'Panel',
      component: Panel
    },
    {
      path: '/rooms',
      name: 'Rooms',
      component: Rooms
    },
    {
      path: '/survey',
      name: 'Survey',
      component: Survey
    }
  ]
})
