import {
    Navbar,
    Nav,
    NavDropdown,
    Form,
    FormControl,
    Button, Table
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
        <Table striped bordered hover>
            <thead>
            <tr>
                <td>ID</td>
                <td>Title</td>
                <td>Description</td>
                <td>Start</td>
                <td>End</td>
                <td>Join</td>
            </tr>
            </thead>
            <tbody>

            {courses.map(course => (
                <tr>
                <td>
                    {course.id}
                </td>
                    <td>
                <Link  to={{pathname: `/course/${course.id}/`, fromDashboard: false}} key={course.id}>
                    {course.title}
                </Link>
                        </td>
                    <td>
                    {course.description}
                </td>
                    <td>
                    {course.start_date}
                </td>
                    <td>
                    {course.end_date}
                </td>
                    <td>
                    <button> Join</button>
                </td>
                </tr>
            ))}

      </tbody>
</Table>
);
}

export default CourseList;