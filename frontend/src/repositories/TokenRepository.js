import Client from './Clients/AxiosClient';
const resource = '/auth';

export default {
    obtain(username, password) {
        var payload = {
            "username": username,
            "password": password
        }
        return Client("").post(`${resource}/obtain_token/`, payload);
    },
    revalidate(token) {
        var payload = {
            "token": token
        }
        return Client(token).post(`${resource}/refresh_token`, payload);
    },
};