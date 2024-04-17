"use client"
import NextImage from 'next/image';
import styles from './DicomFooter.module.css'; 
import { useState } from 'react';
import Modal from '../modal/Modal';
import { Quicksand } from 'next/font/google';
import { useModal } from '../contexts/ModalContext';
import cornerstoneWADOImageLoader from 'cornerstone-wado-image-loader';
import * as cornerstoneTools from "cornerstone-tools";
import ThumbnailAddButton from '../thumbnailAddButton/ThumbnailAddButton';
import { useImageContext } from '../contexts/ImageContext';


const quicksand = Quicksand({ subsets: ["latin"] });

const Footer = () => {

    const [isModalOpen, setIsModalOpen] = useState(false)
    const {toggleModal} = useModal()
    const {images, imageCount, setImageData} = useImageContext()
    console.log(images, 'images');
    console.log(imageCount, 'imageCount');

    const openModal = () => setIsModalOpen(true)
    const closeModal = () => setIsModalOpen(false)

    const import_file = () => {
        document.getElementById('dicom_inp').click()
    }

    const getURL = (base64img) => {
        const img = new Image();
        img.onload = function() {
            let cv = document.getElementsByClassName('cornerstone-canvas')[0]
            let ctx = cv.getContext('2d') 
            cv.width = img.width;
            cv.height = img.height;
            ctx.drawImage(img, 0, 0);
        };
        img.src = base64img;
    }

    const openUploadModal = () => {
        toggleModal()
        setIsModalOpen(false)
    };

    const handleFileChange = (e) => {
        let file = e.target.files[0]
        if (file) {
            processAndRenderDicomFile(file);
        }
    }

    return (
        <div className={quicksand.className}>
            <div className={styles.footer}>
                <div className={styles.container} >
                    {
                        images.map((imageId, index)=>(
                            <div key={index} url={imageId} className={styles.imageContainer} onClick={() => getURL(imageId)} >
                                <NextImage src={imageId} alt="Second" className={styles.image} fill />
                                <span className={styles.imageLabel}>{imageCount[index]}</span>
                            </div>
                        ))
                    }
                    {
                        images.length > 0 ? (
                            <div className={styles.addButton} onClick={openModal} >
                        <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" className="bi bi-plus" viewBox="0 0 16 16">
                            <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4"/>
                        </svg>
                    </div>
                        ) : null
                    }
                    {/* <ThumbnailAddButton /> */}
                </div>
                <Modal isOpen={isModalOpen} onClose={closeModal}>
                    <div className={styles.modalOverlay} onClick={e => e.stopPropagation()}>
                        <div className={styles.modal}>
                            <input type="file" id="dicom_inp" style={{ display: 'none' }} onChange={handleFileChange} />
                            <h2>Import files</h2>
                            <p>Supported format: JPEG, DICOM or ZIP</p>
                            <div className={styles.import_actions}>
                                <button className={styles.btn_import} onClick={import_file}>Import a file</button>
                                <button className={styles.btn_import} onClick={openUploadModal}>Import from url</button>
                                <button className={styles.btn_demo}>Open a demonstration case</button>
                            </div>
                            <div className={styles.buttonGroup}>
                                <button id='close_btn' className={styles.btn_cancel} onClick={closeModal}>Cancel</button>
                            </div>
                        </div>
                    </div>
                </Modal>
            </div>
        </div>
        

        
    );
};

export default Footer;
