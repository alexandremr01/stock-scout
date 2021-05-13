import axios from "axios";

const baseURL = "/api/";

// ALL DEFUALT CONFIGURATION HERE

export default axios.create({
    baseURL,
    headers: {
        // "Authorization": "Bearer xxxxx"
    }
});