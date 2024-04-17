"use client"
// import Image from "next/image"
import styles from './DicomMain.module.css'; 
import { Quicksand } from "next/font/google";
import React, { useState, useRef, useEffect, createContext, useContext } from "react";
import Modal from "../modal/Modal";
import DropZone from "../dropZone/dropZone";
import cornerstone from "cornerstone-core";
// import cornerstoneDICOMImageLoader from '@cornerstonejs/dicom-image-loader';
// import dicomParser from 'dicom-parser';
import cornerstoneWADOImageLoader from 'cornerstone-wado-image-loader';
import cornerstoneWebImageLoader from 'cornerstone-web-image-loader';
import * as cornerstoneTools from "cornerstone-tools";
// import { RenderingEngine } from "@cornerstonejs/core";
import dynamic from "next/dynamic";
import { useDicomContext } from "../contexts/DicomContext";
import dicomParser from 'dicom-parser';
import { useModal } from "../contexts/ModalContext";
import { useImageContext } from "../contexts/ImageContext"


const quicksand = Quicksand({ subsets: ["latin"] });

// export const ModalContext = createContext()

// export function useModal() {
//   return useContext(ModalContext)
// }

const DicomMain = () => {

    // const imageRef = useRef(null)
    const { imageRef } = useDicomContext()
    const { addImage, addImageCount, images, imageCount, imageData } = useImageContext()
    // console.log(useImageContext(), 'asdmaj');

    const [isModalOpen, setIsModalOpen] = useState(false)
    const [warningMsg, setWarningMsg] = useState('')
    const [haveDicom, setHaveDicom] = useState(false)
    const [imageContainerHeight, setImageContainerHeight] = useState('0%');
    const [currentFrameIndex, setCurrentFrameIndex] = useState(1)
    const [totalFrames, setTotalFrames] = useState(1)
    const { isOpen, toggleModal } = useModal()

    useEffect(() => {
        if(imageRef.current){
            cornerstone.enable(imageRef.current)
        }

        console.log(imageRef.current);

        const onNewImage = (e) => {
            const stackData = cornerstoneTools.getToolState(imageRef.current, 'stack')
            if(stackData && stackData.data && stackData.data.length > 0){
                const stack = stackData.data[0]
                setCurrentFrameIndex(stack.currentImageIdIndex + 1)
                setTotalFrames(stack.imageIds.length)
            }
        }

        imageRef.current.addEventListener('cornerstonenewimage', onNewImage)

        // return () => {
        //     imageRef.current.removeEventListener('cornerstonenewimage', onNewImage)
        // }


    }, [haveDicom])

    const openModal = () => {
        // setIsModalOpen(true)
        toggleModal()
    }
    const closeModal = () => {
        // setIsModalOpen(false)
        toggleModal()
        setWarningMsg('')
    }

    const import_file = () => document.getElementById('dicom_inp').click()

    const handleFileChange = (e) => {
        let file = e.target.files[0]
        if (file) {
            processAndRenderDicomFile(file, addImage);
        }
    }

    const handleFileDrop = (files) => {
        let file = files[0]
        if (file) {
            processAndRenderDicomFile(file, addImage);
        }
    }

    const post_url = async (e) => {
        e.preventDefault()
        let url = e.target.url.value.trim()
        if(url==''){
            setWarningMsg('URL cannot be empty.')
            return 
        } else if (!isValidUrl(url)) {
            setWarningMsg('Please enter a valid URL.')
            return 
        }
        setWarningMsg('')

        let imageId;
        if(url.endsWith('.dcm') || url.endsWith('.DCM')){
            imageId = `wadouri:${url}`
        } else {
            imageId = url
        } 
        // else if (url.match(/\.(jpeg|jpg|png)$/)){
        //     imageId = `webimage:${url}`
        //     imageId = `${process.env.NEXT_PUBLIC_NEXT_URI}/api/proxy?imageUrl=${url}`
        // } else {
        //     console.error('Unsupported file type');
        //     return
        // }
        loadImage(imageId, imageRef.current)
        // setIsModalOpen(false)
        toggleModal()
    }

    const isValidUrl = (urlString) => {
        try {
            new URL(urlString);
            return true;
        } catch (e) {
            return false;
        }
    };

    const processAndRenderDicomFile = async (file, addImage) => {
        let imageId;
        const formData = new FormData()
            formData.append("file", file)
            let url = `${process.env.NEXT_PUBLIC_NEXT_URI}/api/upload`
            const res = await fetch(url, {
                credentials: 'include',
                method: 'POST',
                body:formData,
            })
            .then(response  => response.json())
            .then(data => {
                let path = data.message
                imageId = (file.type === 'application/dicom' || file.name.toLowerCase().endsWith('.dcm')) ?
                    cornerstoneWADOImageLoader.wadouri.fileManager.add(file) : 
                    `${process.env.NEXT_PUBLIC_NEXT_URI}/${path}`
                loadImage(imageId, imageRef.current)
            }).catch(error => console.error(error))
    }

    const loadImage = (imageId, imageContainer) => {
        setImageContainerHeight('100%')
        cornerstone.loadAndCacheImage(imageId).then((image) => {
        // cornerstone.loadImage(imageId).then((image) => {
            cornerstone.displayImage(imageContainer, image);
            console.log(image);
            if(image.data != undefined){
                const numFrames = image.data.intString('x00280008');
                addImageCount(numFrames)

                if (numFrames > 1) {
                    const imageIds = Array.from({ length: numFrames }, (_, index) => `${imageId}?frame=${index}`);
                    const stack = {
                        currentImageIdIndex: 0,
                        imageIds
                    };

                    setCurrentFrameIndex(stack.currentImageIdIndex + 1)
                    setTotalFrames(stack.imageIds.length)

                    cornerstoneTools.addStackStateManager(imageContainer, ['stack']);
                    cornerstoneTools.addToolState(imageContainer, 'stack', stack);

                    cornerstoneTools.stackScroll.activate(imageContainer, 1);
                    cornerstoneTools.stackScrollWheel.activate(imageContainer);

                    setTimeout(() => {
                        let canvas = document.getElementsByTagName('canvas')[0];
                        if (canvas) {
                            let dataUrl = canvas.toDataURL('image/png');
                            addImage(dataUrl)
                        }
                    }, 1000);
                }
            } else {
                addImageCount(1)
                getImageUrl(image.imageId)
            }
            setHaveDicom(true)
            try{
            document.getElementById('close_btn').click()

            } catch(err){}
        }).catch(err => {
            console.error(err);
            setHaveDicom(false)
        });
    }

    const getImageUrl = (imageId) => {
        console.log(imageId);
        const img = new Image()
        img.crossOrigin = "anonymous"
        img.onload = function () {
            const canvas = document.getElementsByTagName('canvas')[0]
            const ctx = canvas.getContext('2d')
            ctx.drawImage(img, 0, 0)

            const dataurl = canvas.toDataURL('image/png')
            addImage(dataurl)
            // clearImage()
        }
        img.src = imageId
    }

    return (
        <DropZone onFileDrop={handleFileDrop} >

        <div className={quicksand.className}>
        {/* <CornerstoneInit /> */}

            <div className={styles.dicom_viewer_container}>
                <div className={styles.dicom_viewer_header} style={{display: haveDicom ? 'none' : 'block'}}></div>
                <div className={styles.dicom_viewer_content} style={{display: haveDicom ? 'none' : 'block'}} >
                    <input type="file" id="dicom_inp" style={{ display: 'none' }} onChange={handleFileChange} />
                    <p className="fs-2 text-light">Drag and drop files here</p>
                    <p className="fs-5 text-light">Supported format: JPEG, DICOM or ZIP</p>
                    <div className={styles.dicom_viewer_actions}>
                        <button onClick={import_file}>Import a file</button>
                        <button onClick={openModal}>Import from url</button>
                    </div>
                </div>
                {/* <div className={styles.test} style={{visibility: haveDicom ? 'visible' : 'hidden'}}>have dicom</div> */}
                <div ref={imageRef} tabIndex="0"  className={styles.dicom_image} style={{visibility: haveDicom ? 'visible' : 'hidden', height: imageContainerHeight}}>
                    {haveDicom && (
                        <div className={styles.frameIndicator}>
                            Frame {currentFrameIndex} of {totalFrames}
                        </div>
                    )}
                </div>
            </div>

                {/* <Modal isOpen={isModalOpen} onClose={closeModal} > */}
                <Modal isOpen={isOpen} onClose={toggleModal} >
                    <div className={styles.modalOverlay}>
                        <form onSubmit={post_url}>
                            <div className={styles.modal}>
                                <h4 className={styles.modalTitle}>Import from URL</h4>
                                <label htmlFor="urlInput" className={styles.urlLabel}>Your URL</label>
                                <input type="text" name="url" id="urlInput" className={styles.urlInput} placeholder="http://example.com/file.dcm" />
                                {warningMsg && <div className={styles.msgWarning}>{warningMsg}</div>}
                                <div className={styles.buttonGroup}>
                                    <button onClick={closeModal} className={styles.cancelButton}>Cancel</button>
                                    <button type="submit" className={styles.loadButton}>Load</button>
                                </div>
                            </div>
                        </form>
                    </div>
                </Modal>
        </div>
    </DropZone>

    )
}

export default DicomMain