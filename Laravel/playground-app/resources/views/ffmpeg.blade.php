<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <meta name="csrf-token" content="{{ csrf_token() }}" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">

</head>
<body>

    <div class="m-3">
        <h2>!!!Set system environment variable ชี้มายังโฟล์เดอร์ที่มี ffmpeg!!! ก่อนกดปุ่ม change bitrate</h2>
        <div>Video Input Path</div>
        <input type="text" id="videoin_path" class="form-control" placeholder="D:\laragon\htdocs\playground\laravel\playground-app\public\ffmpeg\input.mp4">
        <div>Video Output Path</div> 
        <input type="text" id="videoout_path" class="form-control" placeholder="D:\laragon\htdocs\playground\laravel\playground-app\public\ffmpeg\output.mp4">
        <div>Text Path</div>
        <input type="text" id="text_path" class="form-control" placeholder="D:\laragon\htdocs\playground\laravel\playground-app\public\ffmpeg\progress.txt">
        <div>Progress (%)</div>
        <div id="progress_text">0</div>
        <div>In Interval</div>
        <div id="interval_text">out</div>
        <button id="convert_btn" onclick="get_progress()" class="btn btn-primary mt-3">Change Bitrate</button>
    </div>


    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://code.jquery.com/jquery-3.6.0.js"></script>
    <script>
        $.ajaxSetup({headers: {'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')}});
        var progress = 0
        function get_progress(){
            $.post("{{url('test')}}",
            {
                event      : 'change_bitrate',
                vdo_input  : $('#videoin_path').val(),
                vdo_output : $('#videoout_path').val(),
                text       : $('#text_path').val()
            },
            function(data, status) {
            })

            var intervalID = setInterval(() => {
                $('#interval_text').html('in')
                if(progress < 100){
                    read_progress_text($('#videoin_path').val(), $('#text_path').val())
                } else {
                    clearInterval(intervalID)
                    $('#interval_text').html('out')
                }
            }, 1000);

        }

        function read_progress_text(file_input, text){
            $.post("{{url('test')}}",
            {
                event   : 'get_progress',
                vdo_input  : $('#videoin_path').val(),
                text       : $('#text_path').val()
            },
            function(data, status) {
                progress = data
                $('#progress_text').html(progress)
            })
        }

    </script>
</body>
</html>