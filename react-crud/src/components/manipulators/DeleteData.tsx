import Option from "../Option";
import { useDelete } from "../hooks/useDelete";

const DeleteData = ({library} : any) => {
    const del = useDelete(library)

    return (
        <>
            <select onChange={del.handleIdSelect} value={del.id}>
                { del.data.length > 0 ?
                del.data.map((element: any) => {
                    return <Option key={element.id} data={element} />
                }) 
                : ''
                }
            </select>
            <form onSubmit={del.deleteData}>
                <p>Name</p>
                <input
                    value={del.owner}
                    disabled
                />
                <br />
                <p>Content:</p>
                <input
                    value={del.content}
                    disabled
                />
                <br />
                <br />
                Important
                <input
                    type="radio"
                    value={"Important"}
                    checked={del.important === true}
                    onChange={() => {}}
                    disabled
                />
                <button type="submit">Delete</button>
            </form>
        </>
    )
}

export default DeleteData;