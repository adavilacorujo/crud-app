import { useEffect, useState } from "react";
import Data from "../Data";
import comments from "../../services/comments";

const DisplayData = ({library} : any) => {
    const [content, setContent] = useState<any[]>([])
    const dataPrefix = 'data_prefix_'

    useEffect(() => {
        comments
            .getAll(library)
            .then(response => {
                setContent(content.concat(response))
            })
            .catch(error => {
                console.log("So you thought", error)
            })
    }, [])

    const table = (
        <table>
            <thead>
            <tr>
                <th>ID</th>
                <th>Owner</th>
                <th>Content</th>
                <th>Created Date</th>
                <th>Important</th>
            </tr>
            </thead>
            <tbody>
            {
                content.length > 0 ?
            content.map(element => 
                <tr key={element.id}>
                    <Data key={dataPrefix + element.id} data={element} />
                </tr>
            )
            :
            ''
            }
            </tbody>
        </ table>
    )

    return (
        <>
            {content.length > 0 ? table : "No data to display"}
        </>
    )
}

export default DisplayData;