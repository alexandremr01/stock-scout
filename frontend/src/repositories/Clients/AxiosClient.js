import axios from "axios";

const baseURL = "";

// ALL DEFUALT CONFIGURATION HERE

export default (token = "") => axios.create({
    baseURL,
    headers: {
        "Authorization": "Bearer " + token
    }
});