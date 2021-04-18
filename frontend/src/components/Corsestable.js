import React from 'react'
import axios from "axios";
import {useState} from "react";

const CourseItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.title}</td>
            <td>{item.description}</td>
            <td>{item.start_date}</td>
        </tr>
    )
}

const CourseList = ({items}) => {
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>TITLE</th>
                <th>DESCRIPTION</th>
                <th>STARTED AT</th>

            </tr>
            {items.map((item) => <CourseItem item={item} />)}
        </table>
    )
}

const courses = {}


function getCoursesInfo() {
        axios.get('http://127.0.0.1:8000/api/courses/')
            .then((response) => setState({courses: response.data}))
            .catch(error => console.log(error)
            )
    }

const Coursestable = (props) => {
     return (
            <div className={App}>
                <button onClick={() => this.getCoursesInfo()}>
                    Получить список курсов
                </button>
                <CourseList items={state.courses} />
            </div>
        )
}

export default Coursestable