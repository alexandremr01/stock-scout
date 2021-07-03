import Client from './Clients/AxiosClient';
const resource = '/api/simulations';

export default {
    get(token) {
        return Client(token).get(`${resource}`);
    },
    getPost(id, token) {
        return Client(token).get(`${resource}/${id}`);
    },
    create(payload, token) {
        return Client(token).post(`${resource}`, payload);
    },
    update(payload, id, token) {
        return Client(token).put(`${resource}/${id}`, payload);
    },
    delete(id, token) {
        return Client(token).delete(`${resource}/${id}`)
    },
};