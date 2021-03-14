import axios from "axios";

const url = 'http://127.0.0.1:8000/api/courses/';

function getCoursesInfo(cb) {
  axios ({
    method: 'get',
    url
  }).then((response)=> cb(response.data));
}

getCoursesInfo(console.log.bind(console, 'getCoursesInfo'));