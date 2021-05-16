import Client from './Clients/AxiosClient'
const resource = 'api/register/'

export default {
    register(email, password) {
        var payload = {
            "email": email,
            "password": password
        }
        return Client("").post(`${resource}`, payload);
    }
};
