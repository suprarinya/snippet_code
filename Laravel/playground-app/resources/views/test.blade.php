<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta name="csrf-token" content="{{ csrf_token() }}" />
    <title>Document</title>
    <style>
        #accordion .glyphicon { margin-right:10px; }
        .panel-collapse>.list-group .list-group-item:first-child {border-top-right-radius: 0;border-top-left-radius: 0;}
        .panel-collapse>.list-group .list-group-item {border-width: 1px 0;}
        .panel-collapse>.list-group {margin-bottom: 0;}
        .panel-collapse .list-group-item {border-radius:0;}

        .panel-collapse .list-group .list-group {margin: 0;margin-top: 10px;}
        .panel-collapse .list-group-item li.list-group-item {margin: 0 -15px;border-top: 1px solid #ddd !important;border-bottom: 0;padding-left: 30px;}
        .panel-collapse .list-group-item li.list-group-item:last-child {padding-bottom: 0;}

        .panel-collapse div.list-group div.list-group{margin: 0;}
        .panel-collapse div.list-group .list-group a.list-group-item {border-top: 1px solid #ddd !important;border-bottom: 0;padding-left: 30px;}
        .panel-collapse .list-group-item li.list-group-item {border-top: 1px solid #DDD !important;}

        #ddForm .panel {
            margin-bottom: 0;
            margin-top: 0;
        }
        #ddForm .glyphicon {
            padding-right: 10px;
        }

        #ddForm ul li span {
            background-repeat: no-repeat;
            display: inline;
            padding: 5px 5px 5px 20px;
        }

        .bgGrey {
            background-color: #ccc;
            min-height: 800px;
        }

        #modules {
    padding: 20px;
    background: #eee;
    margin-bottom: 20px;
    z-index: 1;
    border-radius: 10px;
}

#dropzone {
    padding: 20px 0;
    background: #fff;
    /* min-height: 100px; */
    margin-bottom: 20px;
    z-index: 0;
    border-radius: 0;
}

.active {
    outline: 1px solid red;
}

.hover {
    outline: 1px solid blue;
}

.drop-item {
    cursor: pointer;
    margin-bottom: 10px;
    background-color: rgb(255, 255, 255);
    padding: 5px 10px;
    border-radius: 3px;
    /* border: 1px solid rgb(204, 204, 204); */
    position: relative;
}
.col-1,.col-2,.col-3,.col-4,.col-5,.col-6,.col-7,.col-8,.col-9,.col-10,.col-11,.col-12{transition: 0.2s;padding-top: 0;padding-bottom: 0;}
.drop-item .remove {
    position: absolute;
    top: 4px;
    right: 4px;
}
.drop-item .remove2 {
    position: absolute;
    top: 4px;
    right: 2em;
}
    </style>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" >
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" ></script>
    <script src="https://code.jquery.com/jquery-3.6.0.js"></script>
    <script src="https://code.jquery.com/ui/1.13.2/jquery-ui.js"></script>
</head>
<body>


    {{-- <div>
        <ul class="list-group">
            <li class="list-group-item draggable" aria-current="true">An active item</li>
            <li class="list-group-item draggable">A second item</li>
            <li class="list-group-item draggable">A third item</li>
            <li class="list-group-item draggable">A fourth item</li>
            <li class="list-group-item draggable">And a fifth one</li>
        </ul>
    </div> --}}

    <div class="row">
        <div class="col-lg-9 col-sm-9 col-xs-9 bgGrey sortable" id="sort_zone"></div>
        <div class="list-group col-lg-3 ms-3" id="list_menu"  style="width:250px">
            <a href="#" class="btn btn-success draggable mt-2" aria-current="true">
              The current link item
            </a>
            <a href="#" class="btn btn-success draggable mt-2">A second link item</a>
            <a href="#" class="btn btn-success draggable mt-2">A third link item</a>
            <a href="#" class="btn btn-success draggable mt-2">A fourth link item</a>
        </div>
    </div>

    <div class="form-check">
        <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" onclick="check_checked(this.id)">
        <label class="form-check-label" for="flexCheckDefault">
          Default checkbox1
        </label>
      </div>
      </div>

    


    <div id="draggable1" class="ui-widget-content">
    <p>Drag me to my target1</p>
    </div>
    <div id="draggable2" class="ui-widget-content">
        <p>Drag me to my target2</p>
        </div>
    
    <div id="droppable" class="ui-widget-header" style="width: 250px;height:250px;background: yellow">
    {{-- <p>Drop here</p> --}}
    </div>

    <iframe src="{{url('')}}/test2" frameborder="0" style="width:500px;height:500px"></iframe>

    {{-- <div class="row">
        <div class="col-sm">
            <div id="dropzone" class="row"></div>
        </div>
      <div class="col-sm-2">
        <div id="modules" class="bg-white">
          <p class="drag"><a class="btn btn-success w-100">Patients</a></p>
          <p class="drag"><a class="btn btn-success w-100">Brief History</a></p>
          <p class="drag"><a class="btn btn-success w-100">Medication</a></p>
          <p class="drag"><a class="btn btn-success w-100">GASTRIC CONTENT</a></p>
          <p class="drag"><a class="btn btn-success w-100">COMPLICATION</a></p>
          <p class="drag"><a class="btn btn-success w-100">RAPID UREASE TEST</a></p>
          <p class="drag"><a class="btn btn-success w-100">ESTIMATED BLOOD LOSS</a></p>
          <p class="drag"><a class="btn btn-success w-100">BLOOD TRANSFUSION</a></p>
          <p class="drag"><a class="btn btn-success w-100">SPECIMEN</a></p>
          <p class="drag"><a class="btn btn-success w-100">PLAN</a></p>
          <p class="drag"><a class="btn btn-success w-100">Attendant</a></p>
          <p class="drag"><a class="btn btn-success w-100">Assistant</a></p>
          <p class="drag"><a class="btn btn-success w-100">Endoscopist</a></p>
          <p class="drag"><a class="btn btn-success w-100">Finding</a></p>
          <p class="drag"><a class="btn btn-success w-100">ICD-10</a></p>

          <p class="drag"><a class="btn btn-dark w-100">New Form</a></p>
          <p><button class="btn btn-primary w-100 set-group" sub="set">Set Group</button></p>
        </div>
      </div>
    </div> --}}

      <script>
        $( "#draggable1,#draggable2" ).draggable({
            appendTo: 'body',
            helper: 'clone',
            connectToSortable: "#droppable",
        });
        $( "#droppable" ).droppable({
            // accept: ":not(.ui-sortable-helper)", // Reject clones generated by sortable
            drop: function( event, ui ) {
                let text = ui.draggable.text()
                text = text.trim()
                console.log(event, ui, text);
                if(text=='Drag me to my target1'){
                    var $el = $('<div style="background:red;width:150px;height:50px">'+'drop!'+'</div>');
                }
                $(this).append($el);
                
        }
        }).sortable({
                revert: true
        })
      </script>
    

    <script>
        $.ajaxSetup({headers: {'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')}});

        $( ".draggable" ).draggable({
            connectToSortable: "#sort_zone",
            helper: "clone",
            revert: "invalid",
            appendTo: 'body',
        });

        $("#sort_zone").sortable({
            revert: true,
            receive: function (event, ui) {      
                // console.log(event, ui);
                // alert($(ui.item).text())
                // alert("receive been triggered.");
                let text = $(ui.item).text()
                text = text.trim()
                console.log(event, ui, text);
                if(text=='The current link item'){
                    var $el = $('<div class="col-12" style="background:red;width:100%;height:50px">'+'drop!'+'</div>');
                } else if(text=='A second link item'){
                    var $el = $('<div class="col-12" style="background:yellow;width:100%;height:50px">'+'drop!'+'</div>');
                } else if(text=='A third link item'){
                    var $el = $('<div class="col-12" style="background:blue;width:100%;height:50px">'+'drop!'+'</div>');
                } else if(text=='A fourth link item'){
                    var $el = $('<div class="col-12" style="background:green;width:100%;height:50px">'+'drop!'+'</div>');
                }
                $(this).append($el);

                // delete button
                let selected = $('.ui-draggable,.ui-draggable-handle').filter(function () {
                    return $(this).text().toLowerCase().indexOf($(ui.item).text().toLowerCase()) >= 0
                })
                console.log(selected);
                selected[0].remove()
            }
        }).droppable({ });

        // $( "#sort_zone" ).droppable({
        //     activeClass: 'active',
        //     hoverClass: 'hover',
        //     // accept: ":not(.ui-sortable-helper)", // Reject clones generated by sortable
        //     drop: function( e, ui ) {
        //         console.log(e, ui);
        //     }
        // }).sortable({
        //         revert: true
        // });

        

        $( "ul, li" ).disableSelection();

        function check_checked(id){
            if ($(`#${id}`).prop('checked')) {
                console.log('checked');
                var link = $(`<a href="#" id="button05" class="btn btn-success draggable mt-2">A fifth link item</a>`)
                $('#list_menu').append(link)
                get_html_file()

                $( ".draggable" ).draggable({
                    connectToSortable: "#sort_zone",
                    helper: "clone",
                    revert: "invalid",
                    appendTo: 'body',
                });
            } else {
                console.log('unchecked');

                $('#sort_zone > #form_append01').remove()
                $('#button05').remove()
            }
        }

        function get_html_file() {
            let name_arr = ['append01','append02']
            // let random = Math.floor((Math.random()*name_arr.length))
            let name = name_arr[0]
            $.post("{{url('test')}}",
        {
            event   : 'get_file_content',
            file      : name,
        },
        function(data, status) {
            console.log(JSON.parse(data).data);
            let parse = JSON.parse(data).data
            $("#sort_zone").append(parse)
            
        })
        }
    </script>

    {{-- <script>
            $('.drag').draggable({
        appendTo: 'body',
        helper: 'clone',
        connectToSortable: "#dropzone",
    });

var count_num = 1;
$('#dropzone').droppable({
    
    activeClass: 'active',
    hoverClass: 'hover',
    accept: ":not(.ui-sortable-helper)", // Reject clones generated by sortable
    drop: function (e, ui) {
        console.log(e,ui);
        // var $el = $('<div class="drop-item"><details><summary>' + ui.draggable.text() + '</summary><div><label>More Data</label><input type="text" /></div></details></div>');
        count_num = count_num+1;
        var num_form = $("#num_form").val()
        if(ui.draggable.text()=='Patients'){
            var dt =$("#data_set #patients").html();
            var $el = $('<div class="drop-item col-10 menu-setting" id="element'+count_num+'" sub-type="patients"><div class="row">'+dt+'</div></div>');
        }else if(ui.draggable.text()=='Textarea'){
            var $el = $('<div class="drop-item col-12 menu-setting" id="element'+count_num+'" sub-type="textarea"><textarea class="form-control" name="" rows="3"></textarea></div>');
        }else if(ui.draggable.text()=='Brief History'){
            var dt =$("#data_set #brief_history").html();
            var $el = $('<div class="drop-item col-12 menu-setting" id="element'+count_num+'" sub-type="brief_history"><div class="row"><div class="col-lg-12">'+dt+'</div></div></div>');
        }else if(ui.draggable.text()=='GASTRIC CONTENT'){
            var dt =$("#data_set #gastric_content").html();
            var $el = $('<div class="drop-item col-12 menu-setting" id="element'+count_num+'" sub-type="other"><div class="row"><div class="col-lg-12">'+dt+'</div></div></div>');
        }else if(ui.draggable.text()=='Medication'){
            var dt =$("#data_set #medication").html();
            var $el = $('<div class="drop-item col-12 menu-setting" id="element'+count_num+'" sub-type="medication"><div class="row">'+dt+'</div></div>');
        }else if(ui.draggable.text()=='COMPLICATION'){
            var dt =$("#data_set #complication").html();
            var $el = $('<div class="drop-item col-12 menu-setting" id="element'+count_num+'" sub-type="medication"><div class="row">'+dt+'</div></div>');
        }else if(ui.draggable.text()=='RAPID UREASE TEST'){
            var dt =$("#data_set #rapid_urease_test").html();
            var $el = $('<div class="drop-item col-12 menu-setting" id="element'+count_num+'" sub-type="medication"><div class="row">'+dt+'</div></div>');
        }else if(ui.draggable.text()=='ESTIMATED BLOOD LOSS'){
            var dt =$("#data_set #estimated_blood_loss").html();
            var $el = $('<div class="drop-item col-12 menu-setting" id="element'+count_num+'" sub-type="medication"><div class="row">'+dt+'</div></div>');
        }else if(ui.draggable.text()=='BLOOD TRANSFUSION'){
            var dt =$("#data_set #blood_transfusions").html();
            var $el = $('<div class="drop-item col-12 menu-setting" id="element'+count_num+'" sub-type="medication"><div class="row">'+dt+'</div></div>');
        }else if(ui.draggable.text()=='SPECIMEN'){
            var dt =$("#data_set #specimens").html();
            var $el = $('<div class="drop-item col-12 menu-setting" id="element'+count_num+'" sub-type="medication"><div class="row">'+dt+'</div></div>');
        }else if(ui.draggable.text()=='PLAN'){
            var dt =$("#data_set #plans").html();
            var $el = $('<div class="drop-item col-12 menu-setting" id="element'+count_num+'" sub-type="medication"><div class="row">'+dt+'</div></div>');
        }else if(ui.draggable.text()=='Attendant'){
            var dt =$("#data_set #attendants").html();
            var $el = $('<div class="drop-item col-12 menu-setting" id="element'+count_num+'" sub-type="medication"><div class="row">'+dt+'</div></div>');
        }else if(ui.draggable.text()=='Assistant'){
            var dt =$("#data_set #assistants").html();
            var $el = $('<div class="drop-item col-12 menu-setting" id="element'+count_num+'" sub-type="medication"><div class="row">'+dt+'</div></div>');
        }else if(ui.draggable.text()=='Endoscopist'){
            var dt =$("#data_set #endoscopists").html();
            var $el = $('<div class="drop-item col-12 menu-setting" id="element'+count_num+'" sub-type="medication"><div class="row">'+dt+'</div></div>');
        }else if(ui.draggable.text()=='Finding'){
            var dt =$("#data_set #findings").html();
            var $el = $('<div class="drop-item col-12 menu-setting" id="element'+count_num+'" sub-type="medication"><div class="row">'+dt+'</div></div>');
        }else if(ui.draggable.text()=='ICD-10'){
            var dt =$("#data_set #icd10s").html();
            var $el = $('<div class="drop-item col-12 menu-setting" id="element'+count_num+'" sub-type="medication"><div class="row">'+dt+'</div></div>');
        }else if(ui.draggable.text()=='New Form'){
            var $el = $('<div class="drop-item col-12" id="element'+count_num+'" sub-type="form"><div class="row new-form" num='+num_form+'></div></div>');
        }
        $("#num_form").val(parseInt(num_form)+1)

        $el.append($('<button type="button" class="btn btn-danger btn-sm remove p-0"><i class="mdi mdi-close-thick"></i></button>').click(function () { $(this).parent().detach(); }));
        if(ui.draggable.text()!='New Form'){
            $el.append($('<button type="button" onclick="call_setting('+count_num+')" class="btn btn-primary btn-sm remove2 p-0" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight"><i class="mdi mdi-cog"></i></button>'));
        }

        $(this).append($el);
    }
    }).sortable({
    items: '.drop-item',
    sort: function() {
        $( this ).removeClass( "active" );
    }
});
    </script> --}}
    
</body>
</html>