import { useEffect, useState } from "react";
import Option from "../Option";
import comments from "../../services/comments";

const DeleteData = ({library} : any) => {
    const [id, setId] = useState('');
    const [owner, setOwner] = useState('');
    const [content, setContent] = useState('');
    const [data, setData] = useState<any[]>([])
    const [important, setImportant] = useState(false);

    useEffect(() => {
        // Get all notes to display ids in dropdown
        comments
            .getAll(library)
            .then(response => {
                setData(response)
                if (response.length > 0) {
                    setId(response[0].id)
                    // Add value to input fields
                    setOwner(response[0].owner)
                    setContent(response[0].content)
                    setImportant(response[0].important)
                } 
            })
            .catch(error => {
                console.log("So you thought", error)
            })

    }, [])

    const deleteData = (event : any) => {
        event.preventDefault()
        comments
            .deleteComment(id, library)
            .then(updatedComments => {
                // Do something
                alert(`Deleted item ${id}!`)
                // Update list of items
                setData(updatedComments)
                setId(updatedComments.length > 0 ? updatedComments[0].id : '')
                setOwner(updatedComments.length > 0 ? updatedComments[0].owner : '')
                setContent(updatedComments.length > 0 ? updatedComments[0].content : '')
                setImportant(updatedComments.length > 0 ? updatedComments[0].important : '')
            })
            .catch(error => {
                if (error.message.includes('404')) {
                    alert(`Are you sure item ${id} exists?`)
                }
            })
    }


    const handleIdSelect = (event : any) => {
        setId(event.target.value)
        const selected = data.filter((element : any) => Number(element.id) === Number(event.target.value)).map((filteredElement) => filteredElement)

        // Add value to input fields
        setOwner(selected[0].owner)
        setContent(selected[0].content)
        setImportant(selected[0].important === 't' ? true : false)
    }
    
    return (
        <>
            <select onChange={handleIdSelect} value={id}>
                { data.length > 0 ?
                data.map(element => {
                    return <Option key={element.id} data={element} />
                }) 
                : ''
                }
            </select>
            <form onSubmit={deleteData}>
                <p>Name</p>
                <input
                    value={owner}
                    disabled
                />
                <br />
                <p>Content:</p>
                <input
                    value={content}
                    disabled
                />
                <br />
                <br />
                Important
                <input
                    type="radio"
                    value={"Important"}
                    checked={important === true}
                    onChange={() => {}}
                    disabled
                />
                <button type="submit">Delete</button>
            </form>
        </>
    )
}

export default DeleteData;