import { useEffect, useState } from "react";
import comments from "../../services/comments";

export const useUpdate = (library : any) => {
    const [id, setId] = useState('');
    const [owner, setOwner] = useState('');
    const [content, setContent] = useState('');
    const [data, setData] = useState<any>([])
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
            .updateComment({id, newComment, library})
            .then(updatedResponse => {
                // Do something
                alert(`Updated item ${id}!`)
                // Update list of items
                setData(data.map((c : any) => c.id !== id ? c : updatedResponse))
                if (updatedResponse) setId(updatedResponse.id)
            })
            .catch(error => {
                if (error.message.includes('404')) {
                    alert(`Are you sure item ${id} exists?`)
                }
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
        
        const selected = data.filter((element: any ) : any => Number(element.id) === Number(event.target.value)).map((filteredElement : any) => filteredElement)
        
        // Add value to input fields
        setOwner(selected[0].owner)
        setContent(selected[0].content)
        setImportant(selected[0].important ? true : false)
    }

    return {
        id, handleIdSelect, 
        data, updateData, 
        owner, handleOwner,
        content, handleContent,
        important, handleImportant
    }
}