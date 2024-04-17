<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta name="csrf-token" content="{{ csrf_token() }}" />
    <title>Document</title>
    <style>
        iframe{
        width: 100%;
        height: 75vh;
    }
    </style>
</head>
<body>
    <h1>Test PDF</h1>
    <p>test test test test test</p>
    <iframe id="iframe_pv" src="" frameborder="0"></iframe>

    <div id="header" style="display: block"></div>
    <div id="render2pdf" style="display: block;background: white; padding: 15px;"></div>
    <div id="footer" style="display: block"></div>

    <script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.3/jquery.min.js"></script>
    <script src="https://unpkg.com/jspdf@latest/dist/jspdf.umd.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.6.347/pdf.min.js"></script>

    {{-- <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/1.4.0/jspdf.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/rasterizehtml/1.3.0/rasterizeHTML.allinone.js"></script> --}}
    
    
    <script>
        $.ajaxSetup({headers: {'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')}});

        window.jsPDF = window.jspdf.jsPDF;

        var pdfjsLib = window['pdfjs-dist/build/pdf'];
        pdfjsLib.GlobalWorkerOptions.workerSrc = "{{asset('public/js/pdf.worker.js')}}";

        var doc = new jsPDF();

        // Use the addHTML method to add the entire document to the PDF
        doc.html(document.body, {x: 0, y: 0, width: 297, height: 210}, function() {
        // Once the document has been added, you can save the PDF
            // doc.output("dataurlnewwindow");
            doc.save("test.pdf");

        });


        var header_uri = null
        var footer_uri = null

        $.post("{{url('test')}}",
        {
            event       : 'get_form',
        },
        function(data, status) {
            let parse = JSON.parse(data)
            console.log(parse);

            $('#render2pdf').append(parse['body'])
            $('#header').append(parse['header'])
            $('#footer').append(parse['footer'])

            // html2canvas(document.querySelector("#header"), { 
            //     scale: 1
            // }).then(canvas => {
            //     var pdf = new jsPDF('p', 'mm', [297, 210]);
            //     pdf.addImage(canvas.toDataURL("image/jpeg"), "JPEG", 0, 0, 290, 50/2);
            //     let pdf_src = pdf.output('datauristring')
            //     $('#iframe_pv').attr('src', pdf_src)

            //     // pdf.save("header.pdf");
            // });

            // header_uri = parse['header']
            // footer_uri = parse['footer']

            // // // get header and footer datauri
            to_datauri('header', get_header_footer)
            to_datauri('footer', get_header_footer)
            // // console.log(header_uri, footer_uri);

            // // create preview
            setTimeout(() => {
                // to_preview(set_src)
            }, 500);

            // // download image in diff folder
            // // to_preview(to_image, true)
            setTimeout(() => {
                // $('#render2pdf').empty()
            }, 500);

        }
    )

    function set_src(pdf_src){
        setTimeout(() => {
            console.log('gen');
            $('#iframe_pv').attr('src', pdf_src)
        }, 100);
    }

    function to_image(datauri, page){
        let url = datauri
        var loadingTask = pdfjsLib.getDocument(url);
        loadingTask.promise.then(function(pdf) {
            var pageNumber;
            for (let i = 1; i <= page; i++) {
                pageNumber = i
                pdf.getPage(pageNumber).then(function(page) {
                    var viewport = page.getViewport({ scale: 4 });
                    var canvas = document.createElement('canvas');
                    var ctx = canvas.getContext('2d');
                    var renderContext = { canvasContext: ctx, viewport: viewport };

                    canvas.height = viewport.height;
                    canvas.width = viewport.width;

                    page.render(renderContext).promise.then(() => {
                        var dataUrl   = canvas.toDataURL();
                        // download_image(dataUrl)
                        // save image
                        // save_in_folder(canvas)
                    });
                });
            }
        }, function (reason) {
            // PDF loading error
            console.error(reason);
        });
    }

    function to_datauri(id, callback) {
        document.getElementById(`${id}`).style.display = "block"
        html2canvas(document.querySelector(`#${id}`), ).then(canvas => {
            let dataURI = canvas.toDataURL()
            callback(id, dataURI)
        });
        // document.getElementById(`${id}`).style.display = "none"
    }

    function get_header_footer(id, dataURI){
        if(id == 'header'){
            header_uri = dataURI
        } else if(id == 'footer'){
            footer_uri = dataURI
        }
    }

    function to_preview(callback) {
        var url = "{{url('')}}"
        url = url.replace("terralink", "")

        let input = document.querySelector("#render2pdf")
        document.getElementById('render2pdf').style.display = "block"

        html2canvas(input, { useCORS: true, allowTaint: true, scrollY: 0}).then((canvas) => {

            const image = { type: 'jpeg', quality: 0.98 };
            const margin = [0.9, 0.9]; // มีผลกับ height ของ header
            const filename = 'myfile.pdf';

            var imgWidth = 8.5;
            var pageHeight = 11;

            var innerPageWidth = imgWidth - margin[0] * 2;
            var innerPageHeight = pageHeight - margin[1] * 2;

            // need below for image height per page
            // (มีกรณีที่ภาพตัดทีตัวอักษร ปรับที่ innerHeight เพื่อปรับความยาวของภาพที่ต้องการจะตัดขึ้นหน้าใหม่)
            var innerHeight = 30 // need change

            // Calculate the number of pages.
            var pxFullHeight = canvas.height;
            var pxPageHeight = Math.floor(canvas.width * (pageHeight / imgWidth)) - innerHeight + 0.5;
            var nPages = Math.ceil(pxFullHeight / pxPageHeight) + 3;
            // console.log('PxPageHeight: ', pxPageHeight, pxFullHeight);

            // set how much space at the bottom of page
            // ปรับขนาด height ของ footer
            var footerHeight = 1 // need change
            var headerHeight = 1
            var footerMargin = 1
             // Define pageHeight separately so it can be trimmed on the final page.
            var pageHeight = innerPageHeight - footerHeight;
            // console.log('PageHeight: ', pageHeight);

            // Create a one-page canvas to split up the full image.
            var pageCanvas = document.createElement('canvas');
            var pageCtx = pageCanvas.getContext('2d');
            pageCanvas.width = canvas.width;
            pageCanvas.height = pxPageHeight;
            // Initialize the PDF.
            var pdf = new jsPDF('p', 'in', [8.5, 11]);

            let x_key = 0.3
            let x_value = 3.3
            let y_body = 2.3
            let y_picture = 2.3
            let x_picture = 5.5
            let line_num = 0
            let line_fix = 35
            let pic_num = 0
            let pic_fix = 3
            let new_pageheight = pageHeight + 1

            for (var page = 0; page < nPages; page++) {
                console.log('page:' , page);
                // Trim the final page to reduce file size.
                if (page === nPages - 1 && pxFullHeight % pxPageHeight !== 0) {
                    pageCanvas.height = pxFullHeight % pxPageHeight;
                    pageHeight = (pageCanvas.height * innerPageWidth) / pageCanvas.width;
                }

                y_body = 2.3

                // Display the page.
                var w = pageCanvas.width;
                var h = pageCanvas.height;
                pageCtx.fillStyle = 'white';
                pageCtx.fillRect(0, 0, w, h);
                pageCtx.drawImage(canvas, 0, page * pxPageHeight, w, h, 0, 0, w, h);

                // Add the page to the PDF.
                if (page > 0) pdf.addPage();
                // debugger;
                var imgData = pageCanvas.toDataURL('image/' + image.type, image.quality);

                console.log(header_uri);

                // pdf.addImage(header_uri, 'jpeg', 0, 0, innerPageWidth, 0.2);

                pdf.addImage(imgData, image.type, margin[1], 0.9, innerPageWidth, pageHeight);

                pdf.addImage(footer_uri, 'jpeg', margin[1], 10.5, innerPageWidth, 0.2);

            }

            // console.log('after text');



            // pdf.save();
            let data = pdf.output('datauristring')
            callback(data, nPages)
            // let data = pdf.output('bloburl')
            // callback(data)
            // if(to_image == false){
            //     let data = pdf.output('bloburl')
            //     callback(data)
            // } else {
            //     let datauri = pdf.output('datauristring')
            //     // console.log(datauri);
            //     callback(datauri, npages)
            // }



        })

        // document.getElementById('render2pdf').style.display = "none"
    }
        
        // var doc = new jsPDF();

        // var url = "http://localhost/store/29111820220517/2022-11-11/chart01.jpg"
        // var url1 = "http://localhost/store/29111820220517/2022-11-11/221116145746.png"
        // var url2 = "http://localhost/store/29111820220517/2022-11-11/221111110703.png"

        // doc.setFontSize(40);
        // doc.text("Octonyan loves jsPDF", 35, 25);
        // doc.addImage(url, "JPEG", 15, 40, 60, 100);
        // doc.addImage(url1, "png", 15, 120, 60, 100);
        // doc.addImage(url, "png", 15, 180, 60, 100);
 
        // let datauri = doc.output('datauristring')
        // $('#iframe_pv').attr('src', datauri)


    </script>
</body>
</html>