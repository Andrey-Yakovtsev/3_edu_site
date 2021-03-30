import React from 'react'

const CourseItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.title}</td>
            <td>{item.description}</td>
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
            </tr>
            {/*{items.map((item) => <CourseItem item={item} />)}*/}
        </table>
    )
}


export default CourseList