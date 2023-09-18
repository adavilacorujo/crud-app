import { useState } from "react";
import comments from "../../services/comments";
import { useForm } from "../hooks/useForm";

const AddData = ({library} : any) => {

    const form = useForm(library);

    return (
        <>
            <form onSubmit={form.addData}>
                <p>Name</p>
                <input
                    value={form.owner}
                    onChange={form.handleOwner}
                />
                <br />
                <p>Content:</p>
                <input
                    value={form.content}
                    onChange={form.handleContent}
                />
                <br />
                <br />
                Important
                <input
                    type="radio"
                    value={"Important"}
                    checked={form.important === true}
                    onClick={form.handleImportant}
                    onChange={() => {}}
                />
                <button type="submit">Add</button>
            </form>
        </>
    )
}

export default AddData;