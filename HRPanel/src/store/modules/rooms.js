import axios from 'axios'
import { error } from 'util';

const state = {
    rooms: [
        { piId: '123456789', roomName: 'Kitchen', count: 4, max: 10 },
        { piId: '223456789', roomName: 'WC_1', count: 7, max: 10 },
        { piId: '323456789', roomName: 'WC_2', count: 3, max: 10 }
    ],
    users: []
}

const getters = {
    rooms: state => state.rooms,
    users: state => state.users
}

const actions = {
    getRooms({ commit, state }) {
        const rooms = [...state.rooms];
        axios
            .get('https://officelink.herokuapp.com/api/rooms/')
            .then((response) => {
                console.log(response);
            })
            .catch((error) => {
                console.log(error);
            })

        // commit('');
    },

    addRoom({ commit, state }, room) {
        return new Promise((resolve, reject) => {
            axios
                .post('https://officelink.herokuapp.com/api/rooms/', {
                    "name": room.roomName,
                    "camera": room.deviceId,
                    "maximum_capacity": room.capacity
                })
                .then(function (response) {
                    resolve(response);
                })
                .catch(function (error) {
                    reject(error);
                });
        });

    },

    getUsers({ commit, state }) {
        axios
            .get('http://surveysbackendapp.azurewebsites.net/Users/Workers/')
            .then((response) => {
                commit('SET_GUESTS', response.data);
            })
            .catch((error) => {

            })
    },

    addIndividualSurvey({ commit, state }, survey) {
        return new Promise((resolve, reject) => {
            axios
                .post('http://surveysbackendapp.azurewebsites.net/Surveys/CreateIndividual', {
                    type: survey.type,
                    text: survey.text,
                    username: survey.username
                })
                .then((response) => {
                    resolve(response);
                })
                .catch((error) => {
                    reject(error);
                });
        });
    },

    addGroupSurvey({ commit, state }, survey) {
        return new Promise((resolve, reject) => {
            axios
                .post('http://surveysbackendapp.azurewebsites.net/Surveys/CreateGroup', {
                    type: survey.type,
                    text: survey.text
                })
                .then((response) => {
                    resolve(response);
                })
                .catch((error) => {
                    reject(error);
                });
        });

    }
}

const mutations = {
    SET_GUESTS(state, guests) {
        Vue.set(state, 'users', guests);
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}