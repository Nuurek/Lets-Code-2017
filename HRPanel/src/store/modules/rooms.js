import axios from 'axios'

const state = {
    rooms: [
        { piId: '123456789', roomName: 'Kuchnia', count: 4, max: 10 },
        { piId: '223456789', roomName: 'Toaleta Męska', count: 7, max: 10 },
        { piId: '323456789', roomName: 'Toaleta Damska', count: 3, max: 10 }
    ]
}

const getters = {
    rooms: state => state.rooms
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
        debugger;
        axios
            .post('https://officelink.herokuapp.com/api/rooms/', {
                "name": room.roomName,
                "camera": room.deviceId,
                "maximum_capacity": room.capacity
            })
            .then(function (response) {
                console.log(response);
            })
            .catch(function (error) {
                console.log(error);
            });
    }
}

const mutations = {

}

export default {
    state,
    getters,
    actions,
    mutations
}