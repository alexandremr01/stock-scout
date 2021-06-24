import Client from './Clients/AxiosClient'
const resource = 'api/register/'

export default {
    register(profile) {
        var payload = {
            "email": profile.email,
            "password": profile.password,
            "first_name": profile.firstName,
            "last_name": profile.lastName,
            "phone_number": profile.phoneNumber
        }
        return Client("").post(`${resource}`, payload);
    }
};
