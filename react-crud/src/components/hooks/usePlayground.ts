import { useState } from 'react';


export const usePlayground = (initialState: any) => {
    const [buttonView, setButtonView] = useState(initialState);

    const buttonHandler = (option: any) => {
        setButtonView(option)
    }

    return [buttonView, buttonHandler]
}