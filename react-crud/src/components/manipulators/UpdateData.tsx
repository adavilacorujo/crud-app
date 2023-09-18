import Option from "../Option";
import { useUpdate } from "../hooks/useUpdate";


const UpdateData = ({library} : any) => {
    const update = useUpdate(library)    
    return (
        <>
            <select onChange={update.handleIdSelect} value={update.id}>x
                {update.data.length > 0 ? update.data.map((element: any) => {
                    return <Option key={element.id} data={element} />
                })
                :
                ''
                }
            </select>
            <form onSubmit={update.updateData}>
                <p>Name</p>
                <input
                    value={update.owner}
                    onChange={update.handleOwner}
                />
                <br />
                <p>Content:</p>
                <input
                    value={update.content}
                    onChange={update.handleContent}
                />
                <br />
                <br />
                Important
                <input
                    type="radio"
                    value={"Important"}
                    checked={update.important === true}
                    onClick={update.handleImportant}
                    onChange={() => {}}
                />
                <button type="submit">Update</button>
            </form>
        </>
    )
}

export default UpdateData;