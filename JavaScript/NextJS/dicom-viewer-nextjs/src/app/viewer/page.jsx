// import DicomViewer from "../components/dicomViewer/DicomViewer"
"use client"
import { DicomProvider } from "../components/contexts/DicomContext";
import { ImageProvider } from "../components/contexts/ImageContext";
import { ModalProvider } from "../components/contexts/ModalContext";
import Layout from "../components/layout/Layout"
import dynamic from "next/dynamic";


const DicomViewer = dynamic(
    () => import('../components/DicomViewer/DicomViewer'), 
    { ssr: false }
  );

  const CornerstoneInit = dynamic(() => import('../components/CornerstoneInit'), {
    ssr: false,
});

const viewer = () => {
    return (
        <Layout>
            <CornerstoneInit />
            <DicomProvider>
                <ModalProvider>
                    <ImageProvider>
                        <DicomViewer />
                    </ImageProvider>
                </ModalProvider>
            </DicomProvider>
        </Layout>
    )
}

export default viewer