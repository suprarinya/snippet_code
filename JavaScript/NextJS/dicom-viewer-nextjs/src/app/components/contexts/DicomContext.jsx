"use client"
import { createContext, useRef, useContext } from 'react' 


const DicomContext = createContext()

export const useDicomContext = () => useContext(DicomContext)

export const DicomProvider = ({children}) =>{
    const imageRef = useRef(null)

    return (
        <DicomContext.Provider value={{imageRef}}>
            {children}
        </DicomContext.Provider>
    )
}