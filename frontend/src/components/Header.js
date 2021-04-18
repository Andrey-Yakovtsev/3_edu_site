

const Header = (props) => {
    return (
        <header style={ headingStyle }>
            {props.title}
        </header>
    )
}

Header.defaultProps = {
    title: 'Otus diplom course app'
}

const headingStyle = {
    color: 'red',
    backgroundColor: 'lightblue'
}

export default Header