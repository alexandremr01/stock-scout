import axios from "axios";

const baseURL = "";

// ALL DEFAULT CONFIGURATION HERE

export default (token = "") => axios.create({
    baseURL,
    headers: {
        "Authorization": "Bearer " + token
    }
});