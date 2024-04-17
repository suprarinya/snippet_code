<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Bootstrap demo</title>
    <meta name="csrf-token" content="{{ csrf_token() }}" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" >
  </head>
  <body>
    <main class="container">
        <div class="bg-light p-5 rounded mt-3">
            <h1>Dump table from mysql to mongodb</h1>
            <h6>- ก่อนทำการกดปุ่ม dump ทำการรันคำสั่งด้านล่างใน Command Prompt: <br> 1. pip install mysql-connector <br> 2. pip install pymongo <br> </h6>
            <h6>- ทำการสร้าง database ใน Mongodb เพื่อเตรียมรับข้อมูล</h6>
            <h6>- จะทำการ Drop และ Insert หากใน Database มี collection อยู่แล้ว</h6>
            {{-- <h6>- กรณีที่ table ใน Mysql เป็น table เปล่า collection ที่สร้างใน MongoDB จะมีค่าแรกเป็น null (MongoDB ไม่สามารถสร้าง collection เปล่าในโค้ดได้ )</h6> --}}
            <br>
            @if(Session::has('status'))
                <div class="alert alert-success">
                {{ Session::get('status')}}
                </div>
            @endif
            <form action="{{url('test2')}}" method="post">
                @csrf
                <input type="hidden" name="event" value="dump_mongo">
                <div class="mb-3">
                    <label for="db_host" class="form-label">Mysql Host</label>
                    <input type="text" name="db_host" class="form-control" id="db_host" value="127.0.0.1">
                </div>
                <div class="mb-3">
                    <label for="db_name" class="form-label">Mysql DB Name</label>
                    <input type="text" name="db_name" class="form-control" id="db_name" value="endo5">
                </div>
                <div class="mb-3">
                    <label for="mongodb_host" class="form-label">Mongodb Host</label>
                    <input type="text" name="mongodb_host" class="form-control" id="mongodb_host" value="127.0.0.1">
                </div>
                <div class="mb-3">
                    <label for="mongodb_name" class="form-label">Mongodb DB Name</label>
                    <input type="text" name="mongodb_name" class="form-control" id="mongodb_name" value="endoindex">
                </div>
                <div class="mb-3">
                    <label for="python_path" class="form-label">Python Path</label>
                    <input type="text" name="python_path"  class="form-control" id="python_path" value="C:\Users\Bright\AppData\Local\Programs\Python\Python310\python.exe">
                </div>
                <div class="mb-3">
                    <label for="script_path" class="form-label">Python Script Path</label>
                    <input type="text" name="script_path" class="form-control" id="script_path" value="D:\laragon\htdocs\endocapture5.0\public\python\mongo.py">
                </div>
                <div class="mb-3">
                    <button type="submit" class="btn btn-primary btn-sm">Dump</button>
                </div>    
            </form>

            

        </div>
      </main>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" ></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.3/jquery.min.js"></script>

  </body>

  <script>
    $.ajaxSetup({headers: {'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')}});



$.post("{{url('test2')}}",
{
    event       : 'test',
},
function(data, status) {
    let parse = JSON.parse(data)
    console.log(parse);
    // let element = parse['body']
    // console.log(element);

    // $(element).appendTo('body')

    // let div = document.getElementById('sr')
    // console.log(div);

    // html2pdf()
    // .from(div)
    // .outputPdf('datauristring')
    // .then((uristring) => {
    //     console.log(uristring);
    // });



})
  </script>
</html>