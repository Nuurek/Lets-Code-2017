const state = {
    rooms: [
        { piId: '123456789', roomName: 'Kuchnia', count: 0},
        { piId: '223456789', roomName: 'Toaleta Męska', count: 0},
        { piId: '323456789', roomName: 'Toaleta Damska', count: 0}
    ]
}

const getters = {
    rooms: state => state.rooms
}

export default {
    state,
    getters
}