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
<body >
    <h1>Test PDF22</h1>
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
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"
      integrity="sha512-GsLlZN/3F2ErC5ifS5QtgpiJtWd43JWSuIgh7mbzZ8zBps+dvLusV+eNQATqgA/HdeKFVgA5v3S/cIrLF7QnIg=="
      crossorigin="anonymous"
      referrerpolicy="no-referrer"
    ></script>
    
    <script>
        $.ajaxSetup({headers: {'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')}});

        window.jsPDF = window.jspdf.jsPDF;

        var pdfjsLib = window['pdfjs-dist/build/pdf'];
        pdfjsLib.GlobalWorkerOptions.workerSrc = "{{asset('public/js/pdf.worker.js')}}";

        var doc = new jsPDF();

        $.post("{{url('test')}}",
        {
            event       : 'get_form_html',
        },
        function(data, status) {
            let parse = JSON.parse(data)
            console.log(parse);
            let element = parse['body']
            console.log(element);

            $(element).appendTo('body')

            let div = document.getElementById('sr')
            console.log(div);

            html2pdf()
            .from(div)
            .outputPdf('datauristring')
            .then((uristring) => {
                console.log(uristring);
            });



        }
    )


    </script>

    <script>
        const button = document.getElementById("download-button");

        function generatePDF() {
        // Choose the element that your content will be rendered to.
        const element = document.getElementById("invoice");
        // Choose the element and save the PDF for your user.
        // html2pdf().from(element).save();
        
        html2pdf().from(div_str, 'string').save();
        }

        // button.addEventListener("click", generatePDF);
    </script>
</body>
</html>