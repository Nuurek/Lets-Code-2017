const state = {
    rooms: [
        { piId: '123456789', roomName: 'Kuchnia', count: 4, max: 10},
        { piId: '223456789', roomName: 'Toaleta Męska', count: 7, max: 10},
        { piId: '323456789', roomName: 'Toaleta Damska', count: 3, max: 10}
    ]
}

const getters = {
    rooms: state => state.rooms
}

export default {
    state,
    getters
}