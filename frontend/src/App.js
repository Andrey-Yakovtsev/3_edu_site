import React, {useState, useEffect} from "react";
import Header from "./components/Header";
import axios from "axios";
import 'bootstrap/dist/css/bootstrap.min.css'
import {Link, BrowserRouter as Router, Switch} from "react-router-dom";

function App() {

    const [courses, setCourses] = useState([])

    useEffect(() => {
        axios({
            method: 'GET',
            url: 'http://127.0.0.1:8000/api/courses/'
        }).then(response => {
            setCourses(response.data)
        })
    }, [])

    return (
        <div className='container'>
            <Header title = 'These are our courses' />
            <hr/>
            <Router>
                <ul>
                    {courses.map(course => (
                        <li>
                            <Link to={{pathname: `/course/${course.id}/`, fromDashboard: false}}>
                                {course.title}
                            </Link>
                        </li>
                    ))}
                </ul>
            </Router>
        </div>
    );
}
export default App;


