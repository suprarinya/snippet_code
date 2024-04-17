<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"/>
    <title>Krajee JQuery Plugins - Bootstrap 5.x - &copy; Kartik</title>
    
    <link rel="stylesheet" href="{{url('')}}/fileinput/bootstrap.min.css" crossorigin="anonymous">
    <link rel="stylesheet" href="{{url('')}}/fileinput/bootstrap-icons.min.css" crossorigin="anonymous">
    <link href="{{url('')}}/fileinput/css/fileinput.css"  rel="stylesheet" type="text/css"/>
    <link rel="stylesheet" href="{{url('')}}/fileinput/all.css" crossorigin="anonymous">
    <link href="{{url('')}}/fileinput/themes/explorer-fa5/theme.css" rel="stylesheet" type="text/css"/>
    <script src="{{url('')}}/fileinput/jquery-3.6.0.min.js" crossorigin="anonymous"></script>
    <script src="{{url('')}}/fileinput/js/plugins/buffer.min.js" type="text/javascript"></script>
    <script src="{{url('')}}/fileinput/js/plugins/filetype.min.js" type="text/javascript"></script>
    <script src="{{url('')}}/fileinput/js/plugins/piexif.js" type="text/javascript"></script>
    <script src="{{url('')}}/fileinput/js/plugins/sortable.js" type="text/javascript"></script>
    <meta name="csrf-token" content="{{ csrf_token() }}" />
</head>
<body>
<div class="container my-4">
<p>{{url('').'/fileinput/all.css'}}</p>
    <form method="POST" action="{{url('')}}/test" enctype="multipart/form-data">
        @csrf

        <input type="text" name="event" value="upload_files">
        <input type="text" name="hn" value="TEST">

        
        <div class="file-loading">
            <input id="kv-explorer" name="files[]" type="file" onchange="test()" multiple data-min-file-count="1" data-preview-file-type="text">
        </div>
        <br>
        {{-- <div class="file-loading">
            <input id="file-0a" class="file" type="file" multiple data-min-file-count="1">
        </div>
        <br> --}}
        <button type="submit" class="btn btn-primary submitbtn">Submit</button>
        <button type="reset" class="btn btn-outline-secondary">Reset</button>
    </form>
    <hr>
    
</div>
    <script src="{{url('')}}/fileinput/bootstrap.bundle.min.js" crossorigin="anonymous"></script>
    <script src="{{url('')}}/fileinput/js/fileinput.js" type="text/javascript"></script>
    <script src="{{url('')}}/fileinput/js/locales/fr.js" type="text/javascript"></script>
    <script src="{{url('')}}/fileinput/js/locales/es.js" type="text/javascript"></script>
    <script src="{{url('')}}/fileinput/themes/fa5/theme.js" type="text/javascript"></script>
    <script src="{{url('')}}/fileinput/themes/explorer-fa5/theme.js" type="text/javascript"></script>
    <script>
        $.ajaxSetup({headers: {'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')}});
    
        $("#kv-explorer").fileinput({
                'theme': 'explorer-fa5',
                'uploadUrl': '{{url('')}}/test',
                overwriteInitial: false,
                initialPreviewAsData: true,
                allowedFileExtensions: ['jpg', 'png', 'gif', 'mp4', 'wav'],
                    uploadExtraData: function () {
                    return {
                        event: $("input[name='event']").val(),
                        hn   : $("input[name='hn']").val(),
                    };
                }
            }).on('fileuploaded', function(e, params) {
                console.log('file uploaded', e, params, params.response, params.files[0].name);
                if(params.response == 'done'){
                    let file_name = params.files[0].name
                    let div = $('.file-preview-thumbnails').find('.file-preview-success')
                    let lg = div.length
                    for(i=0; i<lg;i++){
                        div[i].remove()
                    }
                    console.log(file_name, div);
                }
            })
    
            $('.submitbtn').on('click', function(e) {
                e.preventDefault()
                $('.fileinput-upload-button').click()
            })
    </script>
</body>

</html>