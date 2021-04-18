import React, {useState, useEffect} from "react";
import Header from "./components/Header";
import axios from "axios";
import 'bootstrap/dist/css/bootstrap.min.css'


function App() {
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
            <ul>
                {courses.map(course => (
                    <li key={course.id}>
                        {course.title}
                    </li>
                ))}
            </ul>
        </div>
    );
}
export default App;

//
//
// class App extends React.Component {
//     constructor(props) {
//         super(props)
//         this.state = {
//             courses: [],
//         }
//     }
//
//
//
//     render() {
//         return(
//             <div className={App}>
//                 <button onClick={() => this.getCoursesInfo()}>
//                     Получить список курсов
//                 </button>
//                 <CourseList items={this.state.courses} />
//             </div>
//         );
//     }
//
//     componentDidUpdate() {
//         console.log('Перерисовался успешно. Можно что-то поделать ТУТ!!!')
//     }
// }
// export default App;
