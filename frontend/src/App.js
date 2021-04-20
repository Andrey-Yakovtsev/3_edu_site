import React, {useState, useEffect} from "react";
import Header from "./components/Header";
import CourseDetail from "./components/CourseDetail";
import 'bootstrap/dist/css/bootstrap.min.css'
import {Link, BrowserRouter as Router, Switch, Route} from "react-router-dom";

function App() {

    return (
        <div className='container'>

            <Router>
                <Switch>
                    <Header />
                    <Route path='/course/:id' exact={CourseDetail} />
                    <CourseDetail/>
                </Switch>
            </Router>
        </div>
    );
}
export default App;


