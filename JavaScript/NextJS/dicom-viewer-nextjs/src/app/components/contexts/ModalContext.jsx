import React from "react"; 
import { useContext } from "react";
import { useState, createContext } from "react";

const ModalContext = createContext()

export const useModal = () => useContext(ModalContext)

export const ModalProvider = ({ children }) => {
    const [isOpen, setIsOpen] = useState(false)

    const toggleModal = () => setIsOpen(!isOpen)

    return (
        // value={{isOpen, toggleModal}}
        <ModalContext.Provider value={{ isOpen, toggleModal }}>
            {children}
        </ModalContext.Provider>
    )
}
