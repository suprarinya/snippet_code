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

    @php
        $file = "http://localhost:5000/video?source=0&hn=29111820220517&caseuniq=220923142459&cid=1";
        // $image = ;

        // try {
        //     $file_headers = get_headers($file);
        //     if($file_headers && $file_headers[0] != 'HTTP/1.1 404 Not Found') {
        //         $exists = true;
        //     }
        // } catch (\Throwable $th) {
        //     $exists = false;
        // }

    @endphp
    <img id="image1" src="{{$file}}" class="col-lg-12 h-100 p-0" crossorigin="anonymous" width="300px" height="300px">


    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://code.jquery.com/jquery-3.6.0.js"></script>
    <script>
        $.ajaxSetup({headers: {'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')}});


    </script>
</body>
</html>