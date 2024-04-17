<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <form action="file-echo2.php" method="post" enctype="multipart/form-data">
        <input type="file" name="myfile"><br>
        <input type="submit" value="Upload File to Server">
    </form>
    
    <div class="progress">
        <div class="bar"></div >
        <div class="percent">0%</div >
    </div>
    
    <div id="status"></div>

    <img src="" data-src="aaa.png" alt="" width="200" height="200" onerror="keep_checking_img('aaa.png', this)">

    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>

    <script>
        function keep_checking_img(this_datasrc, elem){
            $(elem).css('display', 'none')
            let r = (Math.random() + 1).toString(36).substring(7);
            fetch('{{url('')}}/images/lc-images/'+this_datasrc, {method: 'HEAD'})
            .then(res => {
                if(res.ok){
                    $(elem).css('display', 'block')
                    $(elem).attr('src', '{{url('')}}/images/lc-images/'+this_datasrc+`?rand=${r}`)
                } else {
                    keep_checking_img(this_datasrc)
                }
            }).catch(err => {
                keep_checking_img(this_datasrc)
            })

        }

        let text = "http://localhost/ScreenRecord/64fe93f5e8ffb22aa705e484_0_testtest09_23091112250383_1.jpg";
        let name_arr = text.split("/");
        let new_namearr = text.split("/").slice(-1)
        let datetime_arr = new_namearr[0].split('_')
        let datetime = datetime_arr[datetime_arr.length - 2]
        let new_datetime = parseInt(datetime) - 1

        datetime_arr[datetime_arr.length - 2] = new_datetime
        let new_name = datetime_arr.join('_')
        name_arr[name_arr.length - 1] = new_name
        let new_url = name_arr.join('/')
        // let join = name_arr.join('/')
        console.log(datetime, new_datetime);
    </script>

    {{-- <script>
        var bar = $('.bar');
        var percent = $('.percent');
        var status = $('#status');

        $('form').ajaxForm({
            beforeSend: function() {
                status.empty();
                var percentVal = '0%';
                bar.width(percentVal);
                percent.html(percentVal);
            },
            uploadProgress: function(event, position, total, percentComplete) {
                var percentVal = percentComplete + '%';
                bar.width(percentVal);
                percent.html(percentVal);
            },
            complete: function(xhr) {
                status.html(xhr.responseText);
            }
        });

                        //     all_files.forEach((file, i) => {

                //     var formData = new FormData()
                //     formData.append('files', file)
                //     formData.append('scope_id', scope_id)
                //     formData.append('event', 'upload_photo')
                //     formData.append('_id', '{{@$case_id}}')
                //     formData.append('hn', '{{@$hn}}')
                //     formData.append('index', i)

                    

                //     $.ajax({
                //         xhr: function() {
                //             var xhr = new window.XMLHttpRequest();
                //             xhr.upload.addEventListener("progress", function(evt) {
                //                 console.log(evt.total, evt.loaded);
                //                 if (evt.lengthComputable) {
                //                     var percentComplete = evt.loaded / evt.total;
                //                     percentComplete = parseInt(percentComplete * 100);
                //                     $(`#pg_${div_id[i]}`).css('width', `${percentComplete}%`).html(`${percentComplete}%`)
                                    
                //                     console.log(percentComplete);

                //                     if (percentComplete === 100) {
                //                         // alert('iii')
                //                     }

                //                 }
                //             }, false);

                //             return xhr;
                //         },
                //         url  : '{{ url("api") }}/photo',
                //         type : 'POST',
                //         data : formData,
                //         processData: false,  // tell jQuery not to process the data
                //         contentType: false,  // tell jQuery not to set contentType
                //         enctype: 'multipart/form-data',
                //         async: true,
                //         cache: false,
                //     })
                //     .done((res) => {
                //         $(`#${div_id[i]}`).remove()
                //         count_file = $('.file-upload').length
                //         swal.close()
                //     }).fail((res) => {
                //         count_file = $('.file-upload').length
                //         swal.close()
                //     });

                // })
    </script> --}}
</body>
</html>