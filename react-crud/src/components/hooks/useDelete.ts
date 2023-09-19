import { useEffect, useState } from 'react';
import comments from "../../services/comments";


export const useDelete = (library : any) => {
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
                    setImportant(response[0].important)
                } 
            })
            .catch(error => {
                console.log("So you thought", error)
            })

    }, [])

    const deleteData = (event: any) => {
        event.preventDefault()
        comments
            .deleteComment({id, library})
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


    const handleIdSelect = (event: any) => {
        setId(event.target.value)
        const selected = data.filter((element : any) => Number(element.id) === Number(event.target.value)).map((filteredElement : any) => filteredElement)

        // Add value to input fields
        setOwner(selected[0].owner)
        setContent(selected[0].content)
        setImportant(selected[0].important === 't' ? true : false)
    }

    return {
        id, 
        handleIdSelect,
        owner, content, important, data,
        deleteData
    }
}