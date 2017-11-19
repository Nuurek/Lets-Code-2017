import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/Hello'

import Panel from '@/views/Panel/Panel'
import Rooms from '@/views/Rooms/Rooms'
import Survey from '@/views/Survey/Survey'
import Login from '@/views/login/Login'
import SingleSurvey from '@/views/singleSurvey/SingleSurvey'
import GroupSurvey from '@/views/groupSurvey/GroupSurvey'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: Login
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
    },
    {
      path: '/survey/single',
      name: 'SingleSurvey',
      component: SingleSurvey
    },
        {
      path: '/survey/group',
      name: 'GroupSurvey',
      component: GroupSurvey
    }
  ]
})
