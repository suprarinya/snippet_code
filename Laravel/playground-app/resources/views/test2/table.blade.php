<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" >
  </head>
  <body>
    <main class="container">
        <div class="row"><button type="button" class="btn btn-primary" onclick="htmlTableToExcel()">Export</button></div>
        <br>
        {{-- <div class="bg-light p-5 rounded mt-3"> --}}
            <table class="table" id="data_table">
                @php
                @endphp
                <thead>
                  <tr>
                    <th scope="col">#</th>
                    <th scope="col">Date Register</th>
                    <th scope="col">Time Register</th>
                    {{-- <th scope="col">Case Json</th> --}}
                    @foreach ($head as $h)
                        <th scope="col">{{@$h}}</th>
                    @endforeach
                  </tr>
                </thead>
                <tbody>
                @php
                    $i = 1;
                @endphp
                  @foreach (isset($tb_case)?$tb_case:[] as $case)
                  @php
                      $case_json = isset($case->case_json) ? json_decode($case->case_json, true) : [];
                      $datetime  = isset($case->case_dateregister) ? explode(' ', $case->case_dateregister) : [];
                      $date = $datetime[0];
                      $time = $datetime[1];
                  @endphp
                    <tr>
                        <th scope="row">{{$i}}</th>
                        <td scope="col">{{@$date}}</td>
                        <td scope="col">{{@$time}}</td>
                        {{-- <td scope="col">{{$case->case_json}}</td> --}}

                        @foreach ($head as $h)
                        @php
                            $val = '';
                            try{
                                $val = $case_json[$h];
                            } catch(\Exception $e) {}
                            if(isset($val)){
                                if(gettype($val) != 'string'){
                                    $val = json_encode($val);
                                } 
                            } else {
                                $val = '';
                            }
                        @endphp
                            <td scope="col">{{@$val}}</td>
                        @endforeach
                    </tr>
                    @php
                        $i++;
                    @endphp
                  @endforeach
                </tbody>
              </table>

            

        {{-- </div> --}}
      </main>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" ></script>
    <script src="https://cdn.jsdelivr.net/npm/xlsx@0.18.5/dist/xlsx.full.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.30.1/moment.min.js"></script>
        {{-- <script src="{{asset('public/js/moment.min.js')}}"></script> --}}
        {{-- <script src="{{asset('public/js/dist_xlsx.full.min.js')}}"></script> --}}

    <script>
        // export excel file
    function htmlTableToExcel(){
        // let export_type = $('#export_type').val()
        // let summary_id  = $('#summary_type_id').val()
        let to_export = 'data_table'

        // if(export_type == 'summary'){
        //     if(summary_id == 'rd_user'){
        //         multiple_tables(type)
        //         return
        //     }
        // }

        // let filename = $('#export_type').val()
        var data = document.getElementById(to_export);
        // var excelFile = XLSX.utils.table_to_book(data, {sheet: "sheet1"});
        // XLSX.write(excelFile, { bookType: `${type}`, bookSST: true, type: 'base64' });
        // XLSX.writeFile(excelFile, `${filename} data.${type}`);

        let first_ws = XLSX.utils.table_to_sheet(data)

        
        let json = XLSX.utils.sheet_to_json(first_ws, { header: 1, raw: false })
        console.log(json);
        // if(export_type == 'summary'){
        //     if(!summary_id.includes('scope')){
        //         json = show_month(json)
        //     } else {
        //         json.forEach(row => {
        //             let datetime = row[5] != '' ? row[5] : ''
        //             let exp = datetime.split('/')
        //             let date = exp[0] != undefined && exp[0] != '' ? exp[0] : ''
        //             let month = exp[1] != undefined && exp[1] != '' ? exp[1] : ''
        //             let year = exp[2] != undefined && exp[2] != '' && !exp[2].includes('20') ? '20'+exp[2] : exp[2]
        //             let full = `${date}/${month}/${year}`
        //             row[5] = full
        //         });
        //     }
        // }
        let worksheet = XLSX.utils.json_to_sheet(json, { skipHeader: true })
        const new_workbook = XLSX.utils.book_new()
        XLSX.utils.book_append_sheet(new_workbook, worksheet, "worksheet")
        XLSX.writeFile(new_workbook, `data.xlsx`)
    }
    </script>
  </body>
</html>