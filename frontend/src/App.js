
import Header from "./components/Header";
import CourseDetail from "./components/CourseDetail";
import CourseList from "./components/CourseList";

import 'bootstrap/dist/css/bootstrap.min.css'
import { BrowserRouter as Router, Switch, Route} from "react-router-dom";

function App() {

    return (
        <div className='container'>

            <Router>
                <Header />
                <Switch>

                    <Route path='/courses/' exact component={CourseList} />
                    <Route path='/course/:id' exact component={CourseDetail} />
                </Switch>
            </Router>
        </div>
    );
}
export default App;


