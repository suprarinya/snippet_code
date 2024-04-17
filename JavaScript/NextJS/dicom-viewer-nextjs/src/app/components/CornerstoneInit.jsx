import { useEffect } from 'react';
import { init }  from '@cornerstonejs/core';
// import { initializeImageLoader } from '@cornerstonejs/dicom-image-loader';
// import cornerstoneDICOMImageLoader from '@cornerstonejs/dicom-image-loader';
import cornerstoneWebImageLoader from 'cornerstone-web-image-loader';
import cornerstoneWADOImageLoader from 'cornerstone-wado-image-loader'
import dicomParser from 'dicom-parser';
import cornerstone from "cornerstone-core";
import * as cornerstoneMath from "cornerstone-math";
import * as cornerstoneTools from "cornerstone-tools";
import Hammer from 'hammerjs';

// cornerstoneDICOMImageLoader.external.cornerstone = cornerstone;
cornerstoneWADOImageLoader.external.cornerstone = cornerstone;
cornerstoneWebImageLoader.external.cornerstone  = cornerstone;
cornerstoneWADOImageLoader.external.dicomParser = dicomParser;
cornerstoneTools.external.Hammer = Hammer;
cornerstoneTools.external.cornerstone = cornerstone;
cornerstoneTools.external.cornerstoneMath = cornerstoneMath;
// cornerstoneTools.external.Hammer = Hammer;
// cornerstoneTools.external.cornerstoneMath = cornerstoneMath;
console.log(cornerstoneTools, 'aaa');
// cornerstoneTools.init();
// cornerstoneTools.enableLogger();

// cornerstoneTools.init({
//   mouseEnabled: true,
//   touchEnabled: true,
//   globalToolSyncEnabled: false,
//   showSVGCursors: false,
// });

const baseUrl = 'https://tools.cornerstonejs.org/examples/'
const webWorkerPath = `${baseUrl}assets/image-loader/cornerstoneWADOImageLoaderWebWorker.js`
const codecsPath = `${baseUrl}assets/image-loader/cornerstoneWADOImageLoaderCodecs.js`


cornerstoneWADOImageLoader.configure({
  beforeSend: function(xhr) {
    // Configure XHR headers if needed
  },
});

cornerstoneWADOImageLoader.webWorkerManager.initialize({
  webWorkerPath: webWorkerPath,
  taskConfiguration: {
    'decodeTask': {
      loadCodecsOnStartup: true,
      codecsPath: codecsPath,
      usePDFJS: false,
    },
  },
});

// Register the WADO image loader
cornerstone.registerImageLoader('wadouri', cornerstoneWADOImageLoader.loadImage);
cornerstone.registerImageLoader('webimage', cornerstoneWebImageLoader.loadImage);

localStorage.setItem("debug", "cornerstoneTools")


// initializeImageLoader();

const CornerstoneInit = () => {
  useEffect(() => {
    init(); // Initialize CornerstoneJS
    console.log('CornerstoneJS initialized');
    // You can add more setup code here if needed
  }, []);

  return null; // This component doesn't need to render anything
};

export default CornerstoneInit;
