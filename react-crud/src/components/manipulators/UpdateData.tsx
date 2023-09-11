import { useEffect, useState } from "react";
import Option from "../Option";
import comments from "../../services/comments";


const UpdateData = ({library} : any) => {
    const [id, setId] = useState('');
    const [owner, setOwner] = useState('');
    const [content, setContent] = useState('');
    const [data, setData] = useState<any[]>([])
    const [important, setImportant] = useState(false);

    useEffect(() => {
        let tempId:string;
        // Get all notes to display ids in dropdown
        comments
            .getAll(library)
            .then(response => {
                setData(response)
                if (response.length > 0) {
                    tempId = response[0].id
                    setId(response[0].id)
                    // Add value to input fields
                    setOwner(response[0].owner)
                    setContent(response[0].content)
                    setImportant(response[0].important ? true : false)
                } 
            })
            .catch(error => {
                console.log("So you thought", error)
            })

    }, [])

    const updateData = (event : any) => {
        event.preventDefault()

        if (owner.length < 1) {
            alert('No name has been provided!')
            return null
        }
        if (content.length < 1) {
            alert('Are you sure you want to send an empty note?')
            return null
        }
        const newComment = {
            owner: owner,
            content: content,
            important: important
        }

        comments
            .updateComment(id, newComment, library)
            .then(updatedResponse => {
                // Do something
                alert(`Updated item ${id}!`)
                // Update list of items
                setData(data.map(c => c.id !== id ? c : updatedResponse))
            })
    }

    const handleOwner = (event : any) => {
        setOwner(event.target.value)
    }
    const handleContent = (event : any) => {
        setContent(event.target.value)
    }
    const handleImportant = (event : any) => {
        setImportant(!important)
    }
    const handleIdSelect = (event : any) => {
        setId(event.target.value)
        
        const selected = data.filter((element : any) => Number(element.id) === Number(event.target.value)).map((filteredElement) => filteredElement)
        
        // Add value to input fields
        setOwner(selected[0].owner)
        setContent(selected[0].content)
        setImportant(selected[0].important ? true : false)
    }
    
    return (
        <>
            <select onChange={handleIdSelect} value={id}>
                {data.map(element => {
                    return <Option key={element.id} data={element} />
                })}
            </select>
            <form onSubmit={updateData}>
                <p>Name</p>
                <input
                    value={owner}
                    onChange={handleOwner}
                />
                <br />
                <p>Content:</p>
                <input
                    value={content}
                    onChange={handleContent}
                />
                <br />
                <br />
                Important
                <input
                    type="radio"
                    value={"Important"}
                    checked={important === true}
                    onClick={handleImportant}
                    onChange={() => {}}
                />
                <button type="submit">Update</button>
            </form>
        </>
    )
}

export default UpdateData;