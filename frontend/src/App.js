import {useState, useEffect} from "react";
import Header from "./components/Header";
import axios from "axios";


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
