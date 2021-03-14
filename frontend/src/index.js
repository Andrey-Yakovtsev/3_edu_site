import axios from "axios";

const courses_url = 'http://127.0.0.1:8000/api/courses/';

function getCoursesInfo(cb) {
  axios ({
    method: 'get',
    courses_url
  }).then((response)=> cb(response.data));
}

const modules_url = 'http://127.0.0.1:8000/api/modules/';

function getModulesInfo(cb) {
  fetch(modules_url)
  .then((response)=> response.json())
      .then((data) => cb(data));
}

getCoursesInfo(console.log.bind(console, 'getCoursesInfo'));
getModulesInfo(console.log.bind(console, 'getModulesInfo'));