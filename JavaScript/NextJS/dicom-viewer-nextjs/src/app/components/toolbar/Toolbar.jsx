"use client"
import dynamic from 'next/dynamic';
import { useDicomContext } from '../contexts/DicomContext';
import styles from './Toolbar.module.css'; // Adjust the import path to match your file structure
import * as cornerstoneTools from "cornerstone-tools";
import { useEffect, useState } from 'react';
import cornerstone from "cornerstone-core";


// const CornerstoneInit = dynamic(() => import('../CornerstoneInit'), {
//     ssr: false,
// });

const Toolbar = () => {

    const { imageRef } = useDicomContext()


    const [activeTool, setActiveTool] = useState('');

    useEffect(() => {

        if (imageRef.current) {
            cornerstone.enable(imageRef.current)

            cornerstoneTools.mouseInput.enable(imageRef.current)
            cornerstoneTools.touchInput.enable(imageRef.current)
            cornerstoneTools.mouseWheelInput.enable(imageRef.current);

        }
      }, [imageRef]);

    const handleScrollTool = () => {
        disableAllTools()
        cornerstoneTools.stackScroll.activate(imageRef.current, 1);
        cornerstoneTools.stackScrollWheel.activate(imageRef.current);
        setActiveTool('scroll')
    };

    const handlePanTool = () => {
        disableAllTools()
        cornerstoneTools.pan.activate(imageRef.current, 1)
        setActiveTool('pan')
    };

    const handleZoomTool = () => {
        disableAllTools()
        cornerstoneTools.zoom.activate(imageRef.current, 1)
        setActiveTool('zoom')
    };

    const handleWwwcTool = () => {
        disableAllTools()
        cornerstoneTools.wwwc.activate(imageRef.current, 1)
        setActiveTool('wwwc')
    };

    const handleFreeHandTool = () => {
        disableAllTools()
        cornerstoneTools.freehand.activate(imageRef.current, 1)
        setActiveTool('freehand')
    };

    const handleRotateTool = () => {
        disableAllTools()
        cornerstoneTools.rotate.activate(imageRef.current, 1)
        setActiveTool('rotate')
    };

    const handleClearTool = () => {
        disableAllTools()
        const enabledElem = cornerstone.getEnabledElement(imageRef.current);
        const image = enabledElem.image;
        const viewport = cornerstone.getDefaultViewportForImage(imageRef.current, image);
        cornerstone.setViewport(imageRef.current, viewport);

        cornerstoneTools.clearToolState(imageRef.current, 'freehand');
        cornerstone.updateImage(imageRef.current);
        setActiveTool('clear')
    }

    const handlePenTool = (e) => {
        disableAllTools()
        setActiveTool('pen')
        const canvas = document.getElementsByClassName('cornerstone-canvas')[0];
        console.log(document.getElementsByClassName('cornerstone-canvas')[0], 'a');
        const ctx = canvas.getContext('2d');
        let drawing = false;

        // onmousemove = function(e){console.log("mouse location:", e.clientX, e.clientY)}

      
        const startDrawing = (e) => {
          drawing = true;
          draw(e); // This will place the initial dot.
        };
      
        const stopDrawing = () => {
          drawing = false;
          ctx.beginPath(); // Begin a new path (to not connect dots from different strokes).
        };
      
        const draw = (e) => {
          if (!drawing) return;
          const rect = canvas.getBoundingClientRect();


            // Calculate adjusted position
            const adjustedX = e.clientX - rect.left;
            const adjustedY = e.clientY - rect.top;

            var offsetX = canvas.offsetLeft;
            var offsetY = canvas.offsetTop;

            // Log raw cursor position and adjusted position
            console.log(`Raw cursor position: (${e.clientX}, ${e.clientY})`);
            console.log(`Rect position: (${rect.left}, ${rect.top})`);
            console.log(`Offset position: (${offsetX}, ${offsetY})`);
            // console.log(`Adjusted cursor position: (${adjustedX}, ${adjustedY})`);

            ctx.lineWidth = 3; // Set the line width
            ctx.lineCap = 'round'; // Set the line cap
            console.log('line to', e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
            // ctx.lineTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop); // Move to mouse position
            ctx.lineTo(e.clientX+200, e.clientY+200);
            ctx.stroke();
            // ctx.beginPath(); // Begin a new path
            // ctx.moveTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop); // Move to mouse position
        };
      
        canvas.addEventListener('mousedown', startDrawing);
        canvas.addEventListener('mouseup', stopDrawing);
        canvas.addEventListener('mousemove', draw);
    }

    const disableAllTools = () => {
        cornerstoneTools.pan.deactivate(imageRef.current, 1);
        cornerstoneTools.zoom.deactivate(imageRef.current, 1);
        cornerstoneTools.wwwc.deactivate(imageRef.current, 1);
        cornerstoneTools.freehand.deactivate(imageRef.current, 1);
        cornerstoneTools.rotate.deactivate(imageRef.current, 1);
        cornerstoneTools.stackScroll.deactivate(imageRef.current, 1);
        cornerstoneTools.stackScrollWheel.deactivate(imageRef.current);
        // ctools.length.deactivate(element, 1);
        // ctools.ellipticalRoi.deactivate(element, 1);
        // ctools.rectangleRoi.deactivate(element, 1);
        // ctools.angle.deactivate(element, 1);
        // ctools.highlight.deactivate(element, 1);
        // ctools.probe.deactivate(element, 1);

    }

  return (
    <nav className={styles.toolbar}>
        {/* <CornerstoneInit /> */}
        {/* <button onClick={handleScrollTool} className={ activeTool !== 'scroll' ? `${styles.tool}` : `${styles.tool} ${styles.selected}`}>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-stack" viewBox="0 0 16 16">
                <path d="m14.12 10.163 1.715.858c.22.11.22.424 0 .534L8.267 15.34a.6.6 0 0 1-.534 0L.165 11.555a.299.299 0 0 1 0-.534l1.716-.858 5.317 2.659c.505.252 1.1.252 1.604 0l5.317-2.66zM7.733.063a.6.6 0 0 1 .534 0l7.568 3.784a.3.3 0 0 1 0 .535L8.267 8.165a.6.6 0 0 1-.534 0L.165 4.382a.299.299 0 0 1 0-.535z"/>
                <path d="m14.12 6.576 1.715.858c.22.11.22.424 0 .534l-7.568 3.784a.6.6 0 0 1-.534 0L.165 7.968a.299.299 0 0 1 0-.534l1.716-.858 5.317 2.659c.505.252 1.1.252 1.604 0z"/>
            </svg>
            <span className={styles.icon}>Scroll</span>
        </button> */}
        <button onClick={handlePanTool} className={ activeTool !== 'pan' ? `${styles.tool}` : `${styles.tool} ${styles.selected}`}>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-arrows-move" viewBox="0 0 16 16">
                <path fillRule="evenodd" d="M7.646.146a.5.5 0 0 1 .708 0l2 2a.5.5 0 0 1-.708.708L8.5 1.707V5.5a.5.5 0 0 1-1 0V1.707L6.354 2.854a.5.5 0 1 1-.708-.708zM8 10a.5.5 0 0 1 .5.5v3.793l1.146-1.147a.5.5 0 0 1 .708.708l-2 2a.5.5 0 0 1-.708 0l-2-2a.5.5 0 0 1 .708-.708L7.5 14.293V10.5A.5.5 0 0 1 8 10M.146 8.354a.5.5 0 0 1 0-.708l2-2a.5.5 0 1 1 .708.708L1.707 7.5H5.5a.5.5 0 0 1 0 1H1.707l1.147 1.146a.5.5 0 0 1-.708.708zM10 8a.5.5 0 0 1 .5-.5h3.793l-1.147-1.146a.5.5 0 0 1 .708-.708l2 2a.5.5 0 0 1 0 .708l-2 2a.5.5 0 0 1-.708-.708L14.293 8.5H10.5A.5.5 0 0 1 10 8"/>
            </svg>
            <span className={styles.icon}>Pan</span>
        </button>
        <button onClick={handleZoomTool} className={ activeTool !== 'zoom' ? `${styles.tool}` : `${styles.tool} ${styles.selected}`}>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-zoom-in" viewBox="0 0 16 16">
                <path fillRule="evenodd" d="M6.5 12a5.5 5.5 0 1 0 0-11 5.5 5.5 0 0 0 0 11M13 6.5a6.5 6.5 0 1 1-13 0 6.5 6.5 0 0 1 13 0"/>
                <path d="M10.344 11.742q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1 6.5 6.5 0 0 1-1.398 1.4z"/>
                <path fillRule="evenodd" d="M6.5 3a.5.5 0 0 1 .5.5V6h2.5a.5.5 0 0 1 0 1H7v2.5a.5.5 0 0 1-1 0V7H3.5a.5.5 0 0 1 0-1H6V3.5a.5.5 0 0 1 .5-.5"/>
            </svg>
            <span className={styles.icon}>Zoom</span>
        </button>
        <button onClick={handleRotateTool} className={ activeTool !== 'rotate' ? `${styles.tool}` : `${styles.tool} ${styles.selected}`}>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-bootstrap-reboot" viewBox="0 0 16 16">
                <path d="M1.161 8a6.84 6.84 0 1 0 6.842-6.84.58.58 0 1 1 0-1.16 8 8 0 1 1-6.556 3.412l-.663-.577a.58.58 0 0 1 .227-.997l2.52-.69a.58.58 0 0 1 .728.633l-.332 2.592a.58.58 0 0 1-.956.364l-.643-.56A6.8 6.8 0 0 0 1.16 8z"/>
                <path d="M6.641 11.671V8.843h1.57l1.498 2.828h1.314L9.377 8.665c.897-.3 1.427-1.106 1.427-2.1 0-1.37-.943-2.246-2.456-2.246H5.5v7.352zm0-3.75V5.277h1.57c.881 0 1.416.499 1.416 1.32 0 .84-.504 1.324-1.386 1.324z"/>
            </svg>
            <span className={styles.icon}>Rotate</span>
        </button>
        <button onClick={handleWwwcTool} className={ activeTool !== 'wwwc' ? `${styles.tool}` : `${styles.tool} ${styles.selected}`}>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-circle-half" viewBox="0 0 16 16">
                <path d="M8 15A7 7 0 1 0 8 1zm0 1A8 8 0 1 1 8 0a8 8 0 0 1 0 16"/>
            </svg>
            <span className={styles.icon}>Contrast</span>
        </button>
        <button onClick={handleFreeHandTool} className={ activeTool !== 'freehand' ? `${styles.tool}` : `${styles.tool} ${styles.selected}`}>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-pencil" viewBox="0 0 16 16">
                <path d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325"/>
            </svg>
            <span className={styles.icon}>Free Hand</span>
        </button>
        <button onClick={handlePenTool} className={ activeTool !== 'pen' ? `${styles.tool}` : `${styles.tool} ${styles.selected}`}>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-pencil" viewBox="0 0 16 16">
                <path d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325"/>
            </svg>
            <span className={styles.icon}>Pen</span>
        </button>
        <button onClick={handleClearTool} className={ activeTool !== 'clear' ? `${styles.tool}` : `${styles.tool} ${styles.selected}`}>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-arrow-counterclockwise" viewBox="0 0 16 16">
                <path fillRule="evenodd" d="M8 3a5 5 0 1 1-4.546 2.914.5.5 0 0 0-.908-.417A6 6 0 1 0 8 2z"/>
                <path d="M8 4.466V.534a.25.25 0 0 0-.41-.192L5.23 2.308a.25.25 0 0 0 0 .384l2.36 1.966A.25.25 0 0 0 8 4.466"/>
            </svg>
            <span className={styles.icon}>Reset</span>
        </button>
    </nav>
  );
};

export default Toolbar;
