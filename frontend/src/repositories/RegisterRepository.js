import Client from './Clients/AxiosClient'
const resource = 'api/register/'

export default {
    register(username, email, password) {
        var payload = {
            "username": username,
            "email": email,
            "password": password
        }
        return Client("").post(`${resource}`, payload);
    }
};
