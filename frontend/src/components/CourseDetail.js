import React, {useState, useEffect} from "react";
import axios from "axios";

function CourseDetail({match}){

    const [course, setCourse] = useState([])
    const id = match.params.id

    useEffect(() => {
        axios({
            method: 'GET',
            url: `http://127.0.0.1:8000/api/course/${id}`
        }).then(response => {
            setCourse(response.data)
        })
    }, [id])

    return (
        <div>
            These are {course.title} details:
            <p>Course ID: {course.id}</p>
            <p>Course description: {course.description}</p>
            <p>Course start date: {course.start_date}</p>
        </div>
    )
}

export default CourseDetail;