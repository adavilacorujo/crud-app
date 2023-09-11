import { useState } from "react";
import comments from "../../services/comments";

const AddData = ({library} : any) => {
    const [owner, setOwner] = useState('');
    const [content, setContent] = useState('');
    const [important, setImportant] = useState(false);

    const addData = (event : any) => {
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
            .createComment(library, newComment)
            .then(data => {
                // Add data to list of content
                alert(`Data added with id ${data.id}`)
                setOwner('')
                setContent('')
                setImportant(false)
            })
            .catch(error => {
                console.log("so you thought", error);
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

    return (
        <>
            <form onSubmit={addData}>
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
                <button type="submit">Add</button>
            </form>
        </>
    )
}

export default AddData;