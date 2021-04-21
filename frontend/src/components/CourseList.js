import {
    Navbar,
    Nav,
    NavDropdown,
    Form,
    FormControl,
    Button
} from "react-bootstrap";

import "bootstrap/dist/css/bootstrap.min.css";
import React, {useEffect, useState} from "react";
import axios from "axios";
import {Link, BrowserRouter as Router} from "react-router-dom";


const CourseList = () => {

    const [courses, setCourses]  = useState([])


    useEffect(() => {
        axios({
            method: 'GET',
            url: 'http://127.0.0.1:8000/api/courses/'
        }).then(response => {
            setCourses(response.data)
        })
    }, [])



    return (
        <table>
            <th>
                <td>ID</td>
                <td>Title</td>
                <td>Description</td>
                <td>Start</td>
                <td>End</td>
                <td>Join</td>
            </th>
            <tr>
                {/*{course.id}*/}
            </tr>
            <tr>
                {/*{courses.map(course => (*/}
                {/*    <Link  to={{pathname: `/course/${course.id}/`, fromDashboard: false}} key={course.id}>*/}
                {/*        {course.title}*/}
                {/*    </Link>*/}
                {/*))}*/}

            </tr>
        </table>
    );
}

export default CourseList;