<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="{{url('')}}/css/literallycanvas.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>Document</title>
</head>
<body>
    <h1>Drawing</h1>

    <div class="row">
        <div class="col-4 px-0 h-100"  >
            <div class="mt-3 " id="edit_area">
                <div class="row p-0" style="border: 1px solid #325684;" >
                    <h5 class="text-sort-blue">DRAWING</h5>
                    <div class="col-12 mt-3" >
                        <div class="row">
                            <div class="col-3">
                                <button id="pen_btn" title="Pen" type="button" class="btn btn-edit-photo drawing">
                                    <i class="ri-pencil-fill big-icon"></i>
                                </button>
                            </div>
                            <div class="col-3">
                                <button id="arrow_btn" title="Arrow" type="button" class="btn btn-edit-photo drawing" style="">
                                    <i class="ri-arrow-left-down-fill big-icon"></i>
                                </button>
                            </div>
                            <div class="col-3">
                                <button id="circle_btn" title="Circle" type="button" class="btn btn-edit-photo drawing">
                                    <i class="ri-checkbox-blank-circle-line big-icon"></i>
                                </button>
                            </div>
                            <div class="col-3">
                                <button id="rect_btn" title="Rectangle" type="button" class="btn btn-edit-photo drawing">
                                    <i class=" ri-checkbox-blank-line big-icon"></i>
                                </button>
                            </div>
                            <div class="col-3 mt-4">
                                <button id="text_btn" title="Add Text" type="button" class="btn btn-edit-photo drawing">
                                    <i class=" ri-text big-icon"></i>
                                </button>
                            </div>
                            <div class="col-3 mt-4">
                                <button id="undo_btn" title="Undo" type="button" class="btn btn-edit-photo drawing">
                                    <i class="ri-arrow-go-back-line big-icon"></i>
                                </button>
                            </div>
                            <div class="col-3 mt-4">
                                <button id="redo_btn" title="Redo" type="button" class="btn btn-edit-photo drawing">
                                    <i class="ri-arrow-go-forward-line big-icon"></i>
                                </button>
                            </div>
                            <div class="row " style="padding-top: 379px">
                                <div class="col-6 " >
                                    <div>
                                        {{-- <p>ffffjyjm</p> --}}
                                        <label for="basiInput" class="form-label m-0 mt-2 p-0 text-soft-blue">Width </label>
                                        <input type="range" class="form-range mt-2" id="width_inp"   min="0" max="150" value="36">
                                        <span class="example-val mt-2" id="slider1-span">36</span>
                                        {{-- <input type="number" class="form-control" id="width_inp" placeholder="กำหนดขนาดของเส้น" value="18" oninput="validity.valid||(value='');"> --}}
                                    </div>
                                </div>
                                <div class="col-6 ">
                                    <div>
                                        <label for="basiInput" class="form-label m-0 mt-2 p-0 text-soft-blue">Color</label>
                                        <input type="color" class="form-control form-control-color w-100" id="color_inp" value="#FF0000" placeholder="#3255788" >
                                    </div>
                                </div>
                                <div class="row p-3">
                                    <div class="col-6  text-end">
                                        <button class="btn btn-danger btn-label waves-effect right waves-light w-lg">Undo <i class="ri-arrow-go-back-line label-icon align-middle fs-16 ms-2"></i></button>
                                    </div>
                                    <div class="col-6 ">
                                        <button class="btn btn-success btn-label waves-effect right waves-light w-lg">Reset <i class=" ri-refresh-line label-icon align-middle fs-16 ms-2"></i></button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-7 p-3 m-0">
            <div class="my-drawing" style="height: 100%"></div>
        </div>
    </div>



    <!-- Button trigger modal -->
{{-- <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
    Launch static backdrop modal
</button> --}}

<button type="button" onclick="open_modal('staticBackdrop')" class="btn- btn-info">open</button>
  
<!-- Modal -->
<div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
<div class="modal-dialog">
    <div class="modal-content">
    <div class="modal-header">
        <h5 class="modal-title" id="staticBackdropLabel">Modal title</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
    </div>
    <div class="modal-body">
        <div class="drawing" style="z-index: 9999"></div>  
    </div>
    <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Understood</button>
    </div>
    </div>
</div>
</div>


    

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://code.jquery.com/jquery-3.6.0.js"></script>

    <!-- dependency: React.js -->
    <script src="//cdnjs.cloudflare.com/ajax/libs/react/0.14.7/react-with-addons.js"></script>
    <script src="//cdnjs.cloudflare.com/ajax/libs/react/0.14.7/react-dom.js"></script>
    <script src="{{url('')}}/js/literallycanvas.js"></script>

    <script>
        LC.init(
            document.getElementsByClassName('my-drawing')[0],
            {imageURLPrefix: '{{url('')}}/images/lc-images'}
        );

        

        function open_modal(modal_id) {
            $(`#${modal_id}`).modal('show')
            setTimeout(() => {
                LC.init(
                    document.getElementsByClassName('drawing')[0],
                    {imageURLPrefix: '{{url('')}}/images/lc-images'}
                );
            }, 200);
            
        }
    </script>

</body>
</html>