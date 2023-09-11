import { Link, BrowserRouter, useMatch, useNavigate } from "react-router-dom";
import AddData from "./manipulators/AddData";
import DisplayData from "./manipulators/DisplayData";
import { useState } from "react";
import displaySelector from "../services/displaySelector";

/**
 * Main program to display data from servers
 * 
 * @returns UI components for user interaction
 */
const Playground = () => {
    const [buttonView, setButtonView] = useState('');

    const navigate = useNavigate()

    const match = useMatch('/playground/:library')
    const library = match?.params.library
    
    const buttonHandler = (option:string) => {
        setButtonView(option)
    }
    return (
        <>
        <div className="banner">
            <Link to={library === "sqlalchemy" ? "https://www.sqlalchemy.org/" : "https://pypi.org/project/psycopg2/"} target="_blank">
                {library}
            </Link>
            <Link to={"/"} style={{marginLeft: 100}}>
                Home
            </Link>
        </div>
        <div className="content">
            <button className="button" onClick={() => buttonHandler('add')}>Add comment</button>
            <button className="button" onClick={() => buttonHandler('view')}>View comments</button>
            <button className="button" onClick={() => buttonHandler('update')}>Update comment</button>
            <button className="button" onClick={() => buttonHandler('delete')}>Delete comment</button>
        </ div>

        <div className="content">
            {displaySelector(buttonView, library)}
        </div>
        </>
    )
}

export default Playground;