import React, { useState, useCallback } from 'react';
import styles from './dropZone.module.css'

const DropZone = ({ onFileDrop, children}) => {
    const [isDragActive, setIsDragActive] = useState(false)

    const handleDragEnter = useCallback((e) => {
        e.preventDefault()
        e.stopPropagation()
        setIsDragActive(true)
    }, [])

    const handleDragLeave = useCallback((e) => {
        e.preventDefault()
        e.stopPropagation()
        setIsDragActive(false)
    }, [])

    const handleDragOver = useCallback((e) => {
        e.preventDefault()
        e.stopPropagation()
    }, [])

    const handleDrop = useCallback((e) => {
        e.preventDefault()
        e.stopPropagation()
        setIsDragActive(false)

        const files = e.dataTransfer.files
        if(files && files.length){
            onFileDrop(files)
        }
    }, [onFileDrop])

    return (
        <div
        className={`${styles.dropzone} ${isDragActive ? styles.active : ''}`}
        onDragEnter={handleDragEnter}
        onDragLeave={handleDragLeave}
        onDragOver={handleDragOver}
        onDrop={handleDrop}
        >
            {children}
        </div>
    )
}

export default DropZone