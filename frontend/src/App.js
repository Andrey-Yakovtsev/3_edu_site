import './App.css';
import React from 'react';
import CourseList from "./components/courses";
import axios from "axios";



class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            courses: [],
        }
    }

    getCoursesInfo() {
        axios.get('http://127.0.0.1:8000/api/courses/')
            .then((response) => this.setState({courses: response.data}))
            .catch(error => console.log(error)
            )
        console.log('courses ==>', this.state.typeof) //пытался понять что там в Стейте сохранилось - пока ничего
    }

    render() {
        return(
            <div className={App}>
                <button onClick={() => this.getCoursesInfo()}>
                    Получить список курсов
                </button>
                <CourseList items={this.state.courses} />
            </div>
        );
    }
}
export default App;
