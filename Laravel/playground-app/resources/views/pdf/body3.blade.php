<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <meta name="csrf-token" content="{{ csrf_token() }}" />
    <style>
        @font-face{
            font-family: 'THSarabunNew';
            font-style: normal;
            font-weight: normal;
            src: "{{url('')}}/public/fonts/THSarabunNew.ttf"  format("truetype");
        }
        @font-face{
            font-family: 'THSarabunNew';
            font-style: normal;
            font-weight: bold;
            src: "{{url('')}}/public/fonts/THSarabunNew Bold.ttf" format("truetype");
        }
        @font-face{
            font-family: 'THSarabunNew';
            font-style: italic;
            font-weight: normal;
            src: "{{url('')}}/public/fonts/THSarabunNew Italic.ttf" format("truetype");
        }
        @font-face{
            font-family: 'THSarabunNew';
            font-style: italic;
            font-weight: bold;
            src: "{{url('')}}/public/fonts/THSarabunNew BoldItalic.ttf" format("truetype");
        }

        *{
            font-family: "THSarabunNew";
        }
        html{
            padding: 0;
            margin: 0
        }
        td{
            padding: 0px 5px;
        }
        body{
            padding: 0px 25px;
            margin-top: 30px;
        }
        table{
            width: 100%;
        }

        .head tr{
            line-height: 10px !important;
        }
        .head tr:first-child td{
            font-size: 26px;
            font-weight: bold;
            vertical-align: bottom;
            padding-left: 0;
        }
        .head tr:last-child td{
            font-size: 24px;
            vertical-align: top;
            padding: 0 !important;
            padding-top: 15px !important;
        }
        .head tr td img{
            width: 80px;
        }
        .sub-head tr td{
            line-height: 12px;
            width: 50%;
        }

        .border-bottom{
            border-bottom: 1px solid gray;
        }
        .text-right{
            width: fit-content;
            text-align: right;
        }
        .vb{
            vertical-align: bottom !important;
        }
        .vt{
            vertical-align: top !important;
        }
        .text-center{
            text-align: center !important;
        }
        .text-right{
            text-align: right !important;
        }
        .table_body tr td:first-child{
            width: 20%;
        }

        .text-blue{
            color:dodgerblue;
        }
        .table-line,.table-line td,.table-line th {
            border: 1px solid grey;
        }

        .table-line {
            border-collapse: collapse;
            width: 100%;
        }
        .table-border{
            border: 1px solid grey;
        }
        .w-35{
            width: 35%;
        }
        ul{
            padding-left: 15px;
        }
        ul li{
            font-size: small;
            padding-left: 0;
        }
        .chart{
            width: 25%;
            margin: auto;
        }
        #tb_chart td{
            height: 150px;
            text-align: center;
        }
        .p-0{padding: 0 !important;}
        .data-body tr td:first-child{
            width: 500px;
        }
        .data-body tr td{
            vertical-align: top !important;
        }
        .form-git{
            width: 100%;
            display: flex;
            margin-top: 200px !important;
        }
        #content{
            width: 500px;
            position: absolute;
        }
        #sub_content{
            /* padding-top: 120px !important; */
            width: 100%;
            /* position: absolute; */
        }
        .list-new-page{
            padding-top: 0px;
        }
        .list-img{
            /* padding-top: 200px !important; */
            position: absolute;
            top: 200px;
            right: 0px;
            /* margin-right: -25px; */
            width: 210px;
        }
        .text-blue{color: #295EA9;}
        .text-green{color: #267631;}
        .data-list tr td{line-height: 10px;}
        .table-list, .table-list td ,.table-fetal, .table-fetal td,.table-teral, .table-teral td{
            /* border: 1px solid #F3F6F9; */

            vertical-align: middle;
        }
        .table-list td, .table-fetal td,.table-teral td{
            padding-bottom: 3px;
        }
        .table-list,.table-fetal,.table-teral{
            border: 1px solid black !important;
        }
        .table-list td,.table-fetal td,.table-teral td{
            line-height: 10px;
            /* border-collapse: collapse; */
        }
        .table-list td:nth-child(2),.table-list td:nth-child(4),.table-list td:nth-child(5),.table-fetal tr td:nth-child(2),.table-fetal tr td:nth-child(3),.table-fetal tr td:nth-child(4),.sub-head1 tr td:nth-child(2),.sub-head1 tr td:nth-child(4){
            text-align: center;
        }
        .sub-head1 tr td{width: 20%;}
        .table-list tr td{
            width: 15%;
            line-height: 16px;
        }
        .table-list tr td:nth-child(3){
            width: 40%;
        }
        .table-fetal tr td{width: 15%;}
        .table-fetal tr td:last-child{width: 40%;}
        .table-list tr:first-child td{background: #F3F6F9;text-align: center;}
        .bg-select{
            background: #2F4B5E;color: #fff;
        }
        .table-general{
            width: 100%;
        }
        .table-general tr td:first-child{
            width: 25%;
        }
        .w-25per tr td:first-child{
            width: 25%;
        }
        .table-general td{line-height: 10px;}
        .sub-head1 tr td{
            line-height: 12px;
        }
        .img-pdf{
            width: 180px;
            height: 180px;
        }
        .pl-15px{padding-left: 15px;}

        #header { position: fixed; left: 25px; top: 0px; right: 25px; height: 130px; background-color: white; text-align: center; }
        #footer { position: fixed; left: 10px; bottom: 20px; right: 10px; height: 30px;}
        .page-break {
            page-break-after: always;
        }
        .form-git{
            display: flex;
        }
        .lh10px{
            line-height: 10px !important;
        }
        .w-left{
            width: 70%;
        }

    </style>
    <style>

    </style>
</head>
<body id="needrender" style="height:297mm;width:210mm;">
    <div id="header">
        {{-- id="header"  --}}
        {{-- <table class="head border-bottom">
            <tr>
                <td>{{@$hospital->hospital_name}}</td>
                <td rowspan="2" class="text-right vt p-0"><img src="{{fileconfig($hospital->hospital_picture)}}" alt=""></td>
            </tr>
            <tr>
                <td>{{@$hospital->hospital_address}}</td>
            </tr>
        </table> --}}
        @php
            $hospital->hospital_pic = $hospital->hospital_picture;

            $data['this_json']  = jsonDecode($case_json);
            $data['casedata']   = $case;
            $data['hospital']   = $hospital;
            $data['totaltime']  = $totaltime;
            $data['doctor']     = $doctor;
            $data['scopeall']   = $scopeall;
            $data['folderdate'] = $folderdate;
            // dd($data);
        @endphp
        {{-- @component('pdfhead.a.pdf_head01',$data)@endcomponent --}}
        {{-- header --}}
        <table class="sub-head1 border-bottom" style="display:none">
            <tr>
                <td><b>Procedure</b></td>
                <td><b>PID</b></td>
                <td><b>Name</b></td>
                <td><b>Age</b></td>
                <td><b>Date</b></td>
            </tr>
            <tr>
                <td class="text-green">{{@$case->procedure_name}}</td>
                <td>{{@$case->case_hn}}</td>
                <td>{{@$case->prefix}} {{@$case->firstname}} {{@$case->middlename}} {{@$case->lastname}} ({{@$case->gender_name[0]}}) </td>
                <td>{{age_form_bd($case->birthdate)}} </td>
                <td>{{$date}}</td>
            </tr>
        </table>
        {{-- <div style="height:90%">ghhhh</div> --}}
    </div>

    <div id="sub_content" style="visibility: hidden">
        <table class="sub-head border-bottom">
            <tr>
                <td><b>Treatment Coverage :</b> - </td>
                <td><b>Ward :</b> -</td>
            </tr>
            <tr>
                <td><b>Interventionist Fellow :</b> -</td>
                <td></td>
            </tr>

        </table>
    </div>

    {{-- <div class="form-git">
        <div id="content"> --}}



            {{--  --}}
        @foreach ($sr_data as $key=>$data)
            @if ($key == 'Data')
                @foreach ($data as $subkey=>$subdata)
                    <div class="row">
                        {{-- <div class="col p-2 my-2">
                            <b class="h4" style="font-weight: bold;">{{@$subkey}}</b>
                        </div> --}}
                        <table class="data-list w-left" style="margin-bottom: 10px">
                            <tr><b class="text-blue">{{@strtoupper($subkey)}}</b> : </tr>
                        </table>
                    </div>

                    @foreach ($subdata as $head=>$inner)

                        @if (is_array($inner))

                            @foreach ($inner as $subhead=>$subinner)

                                @if ($subhead == 'Fetus ID')
                                    <div class="col-lg-12 my-2 h6" style="font-weight: bold;margin-bottom: 10px">{{$subhead.' : '.$subinner}}</div>
                                    @php
                                        $fetal_id = $subinner;
                                        continue;
                                    @endphp
                                @endif
                                @if ($subhead == 'Derivation' || $subhead == 'Equation' || $subhead == 'Selection Status')
                                    @php continue; @endphp
                                @endif

                                @if (is_array($subinner))
                                    @foreach ($subinner as $subsubhead=>$subsubinner)

                                        @if ($subsubhead == 'Fetus ID')
                                            <div class="col-lg-12 my-2 h6" style="font-weight: bold;margin-bottom: 10px">{{$subsubhead.' : '.$subsubinner}}</div>
                                            @php
                                                $fetal_id = $subsubinner;
                                                continue;
                                            @endphp
                                        @endif
                                        @if ($subsubhead == 'Derivation' || $subsubhead == 'Equation' || $subsubhead == 'Selection Status')
                                            @php continue; @endphp
                                        @endif

                                        @if (is_array($subsubinner))

                                            @foreach ($subsubinner as $subsubsubhead=>$subsubsubinner)

                                                @if ($subsubsubhead == 'Fetus ID')
                                                    <div class="col-lg-12 my-2 h6" style="font-weight: bold;margin-bottom: 10px">{{$subsubsubhead.' : '.$subsubsubinner}}</div>
                                                    @php
                                                        $fetal_id = $subsubsubinner;
                                                        continue;
                                                    @endphp
                                                @endif
                                                @if ($subsubsubhead == 'Derivation' || $subsubsubhead == 'Equation' || $subsubsubhead == 'Selection Status')
                                                    @php continue; @endphp
                                                @endif

                                                <table class="data-list w-left" style="margin-bottom: 10px">
                                                    <tr>
                                                        <td style="width:75%"><b>{{@$subsubsubhead}}: </b></td>
                                                        <td>{{@ltrim($subsubsubinner)}}</td>
                                                        <td></td>
                                                        <td></td>
                                                        <td></td>
                                                    </tr>
                                                </table>

                                            @endforeach
                                        @else

                                            <table class="data-list w-left" style="margin-bottom: 10px">
                                                <tr>
                                                    <td style="width:75%"><b>{{@$subsubhead}}: </b></td>
                                                    <td>{{@ltrim($subsubinner)}}</td>
                                                    <td></td>
                                                    <td></td>
                                                    <td></td>
                                                </tr>
                                            </table>
                                        @endif

                                    @endforeach

                                @else

                                    <table class="data-list w-left" style="margin-bottom: 10px">
                                        <tr>
                                            <td style="width:75%"><b>{{@$subhead}}: </b></td>
                                            <td>{{@ltrim($subinner)}}</td>
                                            <td></td>
                                            <td></td>
                                            <td></td>
                                        </tr>
                                    </table>
                                @endif
                            @endforeach
                        @else

                            <table class="data-list w-left" style="margin-bottom: 10px">
                                <tr>
                                    <td style="width:75%"><b>{{@$head}}: </b></td>
                                    <td>{{@ltrim($inner)}}</td>
                                    <td></td>
                                    <td></td>
                                    <td></td>
                                </tr>
                            </table>
                        @endif
                    @endforeach
                @endforeach
            @endif
        @endforeach
        {{--  --}}



    {{-- <h1>Test PDF</h1>
    <p>test test test test test</p> --}}
    <iframe id="iframe_pv" src="" frameborder="0" style="width: 90vh;height:1000px;z-index:9999"></iframe>
    <div id="header" style="display: none; height:297mm;width:210mm;"></div>
    <div id="footer" style="display: none; height:297mm;width:210mm;"></div>
    <button onclick="get_preview()" style="margin-buttom:20px">Preview</button>

    <script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.3/jquery.min.js"></script>
    <script src="https://unpkg.com/jspdf@latest/dist/jspdf.umd.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.6.347/pdf.min.js"></script>

    <script>
        $.ajaxSetup({headers: {'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')}});

        window.jsPDF = window.jspdf.jsPDF;

        var pdfjsLib = window['pdfjs-dist/build/pdf'];
        pdfjsLib.GlobalWorkerOptions.workerSrc = "{{asset('public/js/pdf.worker.js')}}";

        // var doc = new jsPDF();

        // // Use the addHTML method to add the entire document to the PDF
        // doc.html(document.body, {x: 0, y: 0, width: 297, height: 210}, function() {
        // // Once the document has been added, you can save the PDF
        //     // doc.output("dataurlnewwindow");
        //     doc.save("test.pdf");

        // });


        var header_uri = null
        var footer_uri = null


        $.post("{{url('test')}}", {
            event       : 'get_form',
        }, function (data) {
            // console.log(data);
            let parse = JSON.parse(data)

            $('#header').append(parse['header'])
            $('#footer').append(parse['footer'])

            to_datauri('header', get_header_footer)
            to_datauri('footer', get_header_footer)

        })

        function get_preview(){
            if(header_uri != null && footer_uri != null){
                to_preview(set_src)
            } else {
                alert('NULL!!!')
            }
        }



        // setTimeout(() => {
        //     to_preview(set_src)
        // }, 10);

    //     $.post("{{url('test')}}",
    //     {
    //         event       : 'get_form',
    //     },
    //     function(data, status) {
    //         let parse = JSON.parse(data)
    //         console.log(parse);

    //         $('#render2pdf').append(parse['body'])
    //         $('#header').append(parse['header'])
    //         $('#footer').append(parse['footer'])

    //         // html2canvas(document.querySelector("#header"), { 
    //         //     scale: 1
    //         // }).then(canvas => {
    //         //     var pdf = new jsPDF('p', 'mm', [297, 210]);
    //         //     pdf.addImage(canvas.toDataURL("image/jpeg"), "JPEG", 0, 0, 290, 50/2);
    //         //     let pdf_src = pdf.output('datauristring')
    //         //     $('#iframe_pv').attr('src', pdf_src)

    //         //     // pdf.save("header.pdf");
    //         // });

    //         // header_uri = parse['header']
    //         // footer_uri = parse['footer']

    //         // // // get header and footer datauri
    //         // to_datauri('header', get_header_footer)
    //         // to_datauri('footer', get_header_footer)
    //         // // console.log(header_uri, footer_uri);

    //         // // create preview
    //         setTimeout(() => {
    //             to_preview(set_src)
    //         }, 500);

    //         // // download image in diff folder
    //         // // to_preview(to_image, true)
    //         setTimeout(() => {
    //             // $('#render2pdf').empty()
    //         }, 500);

    //     }
    // )

    function set_src(pdf_src){
        setTimeout(() => {
            // console.log('gen');
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
        let srcwidth = document.getElementById(id).scrollWidth;
        //  595.26 / srcwidth
        html2canvas(document.querySelector(`#${id}`),{ useCORS: true, allowTaint: true, scrollY: 0, scale:0.3,} ).then(canvas => {
            let dataURI = canvas.toDataURL()
            callback(id, dataURI)
        });
    }

    function get_header_footer(id, dataURI){
        if(id == 'header'){
            header_uri = dataURI
        } else if(id == 'footer'){
            footer_uri = dataURI
        }
        // console.log(dataURI);
        document.getElementById(`${id}`).style.display = "none"
    }

    function to_preview(callback) {
        console.log('start');
        var url = "{{url('')}}"
        url = url.replace("terralink", "")

        let input = document.querySelector("#needrender")

        let srcwidth = document.getElementById('needrender').scrollWidth;
        // document.getElementById('render2pdf').style.display = "block"

        html2canvas(input, { useCORS: true, allowTaint: true, scrollY: 0, scale: 1.0,}).then((canvas) => {

            const image = { type: 'jpeg', quality: 1 };
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
            var nPages = Math.ceil(pxFullHeight / pxPageHeight);
            // console.log('PxPageHeight: ', pxPageHeight, pxFullHeight);

            // set how much space at the bottom of page
            // ปรับขนาด height ของ footer
            var footerHeight = 1 // need change
            var headerHeight = 1.5
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
            var pdf = new jspdf.jsPDF('p', 'in', [8.5, 11]);

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

                


                // pdf.addImage(header_uri, 'jpeg', margin[1], 0.1, innerPageWidth, 0.8);

                pdf.addImage(imgData, image.type, margin[1], 1.5, innerPageWidth, pageHeight);
                console.log('pageHeight: ', pageHeight, 'marginY-body: ', 0.9, 'body-sum', pageHeight+0.9, 'max-height: ', 11);

                // pdf.addImage(footer_uri, 'jpeg', margin[1], 10.5, innerPageWidth, 0.2);

            }

            // console.log('after text');



            // pdf.save();
            let data = pdf.output('datauristring')
            // console.log(data);
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
