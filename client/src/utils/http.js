import Axios from "axios";
import router from "@/router";

// Set config defaults when creating the axios
let axios = Axios.create({
  baseURL: process.env.BASE_URL
});

axios.interceptors.request.use(
  config => {
    let token = localStorage.getItem("USER_ID");

    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  err => {
    return Promise.reject(err);
  }
);

axios.interceptors.response.use(
  response => {
    return response;
  },
  error => {
    console.log("error=", error);
    if (error.response) {
      switch (error.response.status) {
        case 400:
          // Handle the token expired issue here.
          break;

        case 401:
          // 401: clear token and go to login page.
          router.replace({
            name: "Login",
            query: {
              redirect: router.currentRoute.fullPath
            }
          });
      }
    }

    return Promise.reject(error.response ? error.response.data : error); // return error message directly
  }
);

export const post = (url, data, axiosOptions) => {
  return axios({
    method: "post",
    url: url,
    data: data,
    transformRequest: [
      data => {
        // Do whatever you want to transform the data
        let ret = "";
        for (let it in data) {
          ret +=
            encodeURIComponent(it) + "=" + encodeURIComponent(data[it]) + "&";
        }
        return ret;
      }
    ],
    headers: {
      "Content-Type": "application/x-www-form-urlencoded"
    },
    ...axiosOptions
  });
};

export const postJSON = (url, params, axiosOptions) => {
  return axios({
    method: "post",
    url: url,
    data: params,
    headers: {
      "Content-Type": "application/json"
    },
    ...axiosOptions
  });
};

export const uploadFile = (url, data) => {
  return axios({
    method: "post",
    url: url,
    data: data,
    headers: {
      "Content-Type": "multipart/form-data"
    }
  });
};
export const put = (url, params) => {
  return axios({
    method: "put",
    url: url,
    data: params,
    transformRequest: [
      data => {
        // Do whatever you want to transform the data
        let ret = "";
        for (let it in data) {
          ret +=
            encodeURIComponent(it) + "=" + encodeURIComponent(data[it]) + "&";
        }
        return ret;
      }
    ],
    headers: {
      "Content-Type": "application/x-www-form-urlencoded"
    }
  });
};
export const deleteRequest = url => {
  return axios({
    method: "delete",
    url: url
  });
};
export const get = (url, params) => {
  return axios({
    method: "get",
    params: params,
    url: url
  });
};