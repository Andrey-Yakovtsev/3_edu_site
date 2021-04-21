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


const Header = () => {

    const [courses, setCourses]  = useState([])
    const [categories, setCategories]  = useState([])


    useEffect(() => {
        axios({
            method: 'GET',
            url: 'http://127.0.0.1:8000/api/courses/'
        }).then(response => {
            setCourses(response.data)
        })
    }, [])

    useEffect(() => {
        axios({
            method: 'GET',
            url: 'http://127.0.0.1:8000/api/categories/'
        }).then(response => {
            setCategories(response.data)
        })
    }, [])

    return (
            <Navbar bg="light" expand="lg">
                <Navbar.Brand href="#home">Educational Platform</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="mr-auto">
                        <Nav.Link href="/courses/">Our courses</Nav.Link>
                        <NavDropdown title="Categories" id="basic-nav-dropdown">
                            {categories.map(category => (
                                <NavDropdown.Item >
                                    <Link to={{pathname: `/category/${category.id}/`, fromDashboard: false}} key={category.id}>
                                        {category.title}
                                    </Link>
                                </NavDropdown.Item>
                            ))}
                        </NavDropdown>
                        <NavDropdown title="Courses" id="basic-nav-dropdown">
                            {courses.map(course => (
                                <NavDropdown.Item >
                                    <Link  to={{pathname: `/course/${course.id}/`, fromDashboard: false}} key={course.id}>
                                       {course.title}
                                    </Link>
                                </NavDropdown.Item>
                            ))}
                        </NavDropdown>
                    </Nav>
                    <Form inline>
                        <FormControl type="text" placeholder="Search" className="mr-sm-2" />
                        <Button variant="outline-success">Search</Button>
                    </Form>
                </Navbar.Collapse>
            </Navbar>
    );
}

export default Header;