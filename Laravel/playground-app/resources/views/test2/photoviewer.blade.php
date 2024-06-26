<!DOCTYPE html>
<html lang="zh-CN">

<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>PhotoViewer Examples</title>
  <!-- Bootstrap -->
  <link href="https://cdn.bootcss.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
  <link href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
  {{-- <link href="../dist/photoviewer.css" rel="stylesheet"> --}}
  <link href      ="{{url('css/photoviewer.css')}}" rel="stylesheet" type="text/css">
  <link rel="stylesheet" href="http://localhost/playground/laravel/playground-app/">
  <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
  <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
  <!--[if lt IE 9]>
    <script src="https://cdn.bootcss.com/html5shiv/3.7.3/html5shiv.min.js"></script>
    <script src="https://cdn.bootcss.com/respond.js/1.4.2/respond.min.js"></script>
  <![endif]-->
  <style>
    .photoviewer-modal {
      background-color: transparent;
      border: none;
      border-radius: 0;
      box-shadow: 0 0 6px 2px rgba(0, 0, 0, .3);
    }

    .photoviewer-header .photoviewer-toolbar {
      background-color: rgba(0, 0, 0, .5);
    }

    .photoviewer-stage {
      top: 0;
      right: 0;
      bottom: 0;
      left: 0;
      background-color: rgba(0, 0, 0, .85);
      border: none;
    }

    .photoviewer-footer .photoviewer-toolbar {
      background-color: rgba(0, 0, 0, .5);
      border-top-left-radius: 5px;
      border-top-right-radius: 5px;
    }

    .photoviewer-header,
    .photoviewer-footer {
      border-radius: 0;
      pointer-events: none;
    }

    .photoviewer-title {
      color: #ccc;
    }

    .photoviewer-button {
      color: #ccc;
      pointer-events: auto;
    }

    .photoviewer-header .photoviewer-button:hover,
    .photoviewer-footer .photoviewer-button:hover {
      color: white;
    }
  </style>
</head>

<body dir="ltr">
  <div class="container">
    <div class="image-set">
      <a data-gallery="photoviewer" data-title="Slipping Away by Jerry Fryer" data-group="a"
         href="https://farm1.staticflickr.com/313/31812080833_297acfbbd9_z.jpg">
        <img src="https://farm1.staticflickr.com/313/31812080833_297acfbbd9_s.jpg" alt="">
      </a>
      <a data-gallery="photoviewer" data-title="Mi Fuego by albert dros" data-group="a"
         href="https://farm4.staticflickr.com/3804/33589584740_b0fbdcd4aa_z.jpg">
        <img src="https://farm4.staticflickr.com/3804/33589584740_b0fbdcd4aa_s.jpg" alt="">
      </a>
      <a data-gallery="photoviewer" data-title="Winter Fairytale by Achim Thomae" data-group="a"
         href="https://farm1.staticflickr.com/470/31340603494_fb7228020d_z.jpg">
        <img src="https://farm1.staticflickr.com/470/31340603494_fb7228020d_s.jpg" alt="">
      </a>

      <a data-gallery="photoviewer"
         href="https://farm5.staticflickr.com/4267/34162425794_1430f38362_z.jpg" data-group="b">
        <img src="https://farm5.staticflickr.com/4267/34162425794_1430f38362_s.jpg" alt="">
      </a>
      <a data-gallery="photoviewer"
         href="https://farm1.staticflickr.com/4160/34418397675_18de1f7b9f_z.jpg" data-group="b">
        <img src="https://farm1.staticflickr.com/4160/34418397675_18de1f7b9f_s.jpg" alt="">
      </a>
      <a data-gallery="photoviewer"
         href="https://farm1.staticflickr.com/512/32967783396_a6b4babd92_z.jpg" data-group="b">
        <img  src="https://farm1.staticflickr.com/512/32967783396_a6b4babd92_s.jpg" alt="">
      </a>
<!-- 
      <a href="">
        
      </a> -->
      <img data-title="test" data-gallery="photoviewer" src="https://images.unsplash.com/photo-1498462440456-0dba182e775b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8c3BsYXNofGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60" alt="">
    </div>
  </div>
  <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
  <script src="https://cdn.bootcss.com/jquery/1.12.4/jquery.min.js"></script>
  <script src="https://cdn.bootcss.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <!-- Include all compiled plugins (below), or include individual files as needed -->
  {{-- <script src="../dist/photoviewer.js"></script> --}}
    <script src     ="{{url('js/photoviewer.min.js')}}"></script>
  <script>
    // initialize manually with a list of links
    $('[data-gallery=photoviewer]').click(function (e) {
      console.log($(this).index());
      e.preventDefault();

      var items = [],
        options = {
          index: $(this).index(),
        };

      $('[data-gallery=photoviewer]').each(function () {
        items.push({
          src: $(this).attr('href'),
          title: $(this).attr('data-title')
        });
      });

      new PhotoViewer(items, options);

    });
  </script>
</body>

</html>
