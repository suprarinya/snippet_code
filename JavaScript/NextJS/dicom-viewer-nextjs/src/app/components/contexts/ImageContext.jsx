import { useState, createContext, useContext } from "react";

const ImageContext = createContext()

export const ImageProvider = ({children}) => {
    const [images, setImages] = useState([])
    const [imageCount, setImageCount] = useState([])
    const [imageData, setImageData] = useState("") 

    const addImage = (imageId) => {
        setImages((prevImages) => [...prevImages, imageId])
    }

    const addImageCount = (imageCount) => {
        setImageCount((prevCount) => [...prevCount, imageCount])
    }


    const clearImage = () => {
        setImages([])
    }

    return (
        <ImageContext.Provider value={{images, imageCount, imageData, addImage, clearImage, addImageCount, setImageData}}>
            {children}
        </ImageContext.Provider>
    )
}

export const useImageContext = () => useContext(ImageContext)
