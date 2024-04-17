import React from 'react';
import Image from 'next/image';
import styles from './DicomViewer.module.css'; 
import DicomMain from '../dicomMain/DicomMain';
import DicomFooter from '../dicomFooter/DicomFooter';
import Layout from '../layout/Layout';
import { Quicksand } from "next/font/google";
import dynamic from 'next/dynamic';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import Footer from '../footer/Footer';
// import { ModalContext } from '../modal/Modal';
// import Toolbar from '../toolbar/Toolbar';

const quicksand = Quicksand({ subsets: ["latin"] });
const Toolbar = dynamic(() => import('../toolbar/Toolbar'), {
    ssr: false,
    loading: () => <p>Loading...</p>,
  });

const DicomViewer = () => {
    const router = useRouter();

    const handleClickRefresh = () => {
        window.location.reload()
    }

  return (
        <div className={quicksand.className}>
            {/* <ModalContext> */}
                <div className={styles.dicomViewer}>
                    <div className={styles.topBar}>                    
                        <p className={quicksand.className}>Topbar</p>
                        <button onClick={handleClickRefresh} className={styles.acceptButton}>Clear</button>
                    </div>
                    <div className='row p-0 m-0'>
                        <div className='col-11 p-0 m-0'>
                            <DicomMain />
                        </div>
                        <div className='col-1 p-0 m-0'>
                            <div className={styles.toolBar}>
                                <Toolbar />
                            </div>
                        </div>
                    </div>
                    <div className={styles.footer}>
                        < DicomFooter/>
                    </div>
                </div>
            {/* </ModalContext> */}
        </div>
  );
};

export default DicomViewer;
