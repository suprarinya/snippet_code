
<!DOCTYPE html>
<!--
/*
 * jQuery File Upload Demo
 * https://github.com/blueimp/jQuery-File-Upload
 *
 * Copyright 2010, Sebastian Tschan
 * https://blueimp.net
 *
 * Licensed under the MIT license:
 * https://opensource.org/licenses/MIT
 */
-->
<html lang="en">
  <head>
    <!-- Force latest IE rendering engine or ChromeFrame if installed -->
    <!--[if IE]>
      <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <![endif]-->
    <meta charset="utf-8" />
    <title>jQuery File Upload Demo</title>
    <meta
      name="description"
      content="File Upload widget with multiple file selection, drag&amp;drop support, progress bars, validation and preview images, audio and video for jQuery. Supports cross-domain, chunked and resumable file uploads and client-side image resizing. Works with any server-side platform (PHP, Python, Ruby on Rails, Java, Node.js, Go etc.) that supports standard HTML form file uploads."
    />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!-- Bootstrap styles -->
    <link
      rel="stylesheet"
      href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
      integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u"
      crossorigin="anonymous"
    />
    <!--[if gte IE 9]><!-->
    {{-- <!-- Carbon Ads styles -->
    <link rel="stylesheet" href="css/vendor/carbon.css" />
    <!-- Pintura Image Editor styles -->
    <link rel="stylesheet" href="css/vendor/pintura.min.css" /> --}}
    <!--<![endif]-->
    <!-- Generic page styles -->
    <link rel="stylesheet" href="{{url('selfupload/css/bootstrap.min.css')}}">
    <link rel="stylesheet" href="{{url('selfupload/css/style.css')}}">
    <link rel="stylesheet" href="{{url('selfupload/css/blueimp-gallery.min.css')}}">
    <link rel="stylesheet" href="{{url('selfupload/css/jquery.fileupload.css')}}">
    <link rel="stylesheet" href="{{url('selfupload/css/jquery.fileupload-ui.css')}}">
    <link href="{{url('')}}/css/font-awesome.min.css" rel="stylesheet" type="text/css"/>
    <link href="{{url('')}}/css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
    <noscript><link rel="stylesheet" href="{{url('selfupload/css/jquery.fileupload-noscript.css')}}"></noscript>
    <noscript><link rel="stylesheet" href="{{url('selfupload/css/jquery.fileupload-ui-noscript.css')}}"></noscript>
    <style>
      #navigation {
        margin: 10px 0;
      }
      @media (max-width: 767px) {
        #title,
        #description {
          display: none;
        }
      }
    </style>
    <!-- blueimp Gallery styles -->
    <link
      rel="stylesheet"
      href="https://blueimp.github.io/Gallery/css/blueimp-gallery.min.css"
    />
    <!-- CSS to style the file input field as button and adjust the Bootstrap progress bars -->
    <link rel="stylesheet" href="{{url('')}}/css/jquery.fileupload.css" />
    <link rel="stylesheet" href="{{url('')}}/css/jquery.fileupload-ui.css" />
    <!-- CSS adjustments for browsers with JavaScript disabled -->
    <noscript
      ><link rel="stylesheet" href="public/css/jquery.fileupload-noscript.css"
    /></noscript>
    <noscript
      ><link rel="stylesheet" href="public/css/jquery.fileupload-ui-noscript.css"
    /></noscript>
  </head>
  <body>
    <p>{{url('')."/css/bootstrap.min.css"}}</p>
    <p>{{url('selfupload/css/bootstrap.min.css')}}</p>
    <div class="container">
      <ul class="nav nav-tabs" id="navigation">
        <li>
          <a href="https://github.com/blueimp/jQuery-File-Upload">Project</a>
        </li>
        <li class="active">
          <a href="#">Demo</a>
        </li>
        <li>
          <a href="https://github.com/blueimp/jQuery-File-Upload/wiki">Wiki</a>
        </li>
        <li>
          <a href="https://blueimp.net">Author</a>
        </li>
      </ul>
      <h1 id="title">jQuery File Upload Demo</h1>
      <blockquote id="description">
        <p>
          File Upload widget with multiple file selection, drag&amp;drop
          support, progress bars, validation and preview images, audio and video
          for jQuery.<br />
          Supports cross-domain, chunked and resumable file uploads and
          client-side image resizing.<br />
          Works with any server-side platform (PHP, Python, Ruby on Rails, Java,
          Node.js, Go etc.) that supports standard HTML form file uploads.
        </p>
      </blockquote>
      <!-- The file upload form used as target for the file upload widget -->
      <form
        id="fileupload"
        action="https://jquery-file-upload.appspot.com/"
        method="POST"
        enctype="multipart/form-data"
      >
        <!-- Redirect browsers with JavaScript disabled to the origin page -->
        <noscript
          ><input
            type="hidden"
            name="redirect"
            value="https://blueimp.github.io/jQuery-File-Upload/"
        /></noscript>
        <!-- The fileupload-buttonbar contains buttons to add/delete files and start/cancel the upload -->
        <div class="row fileupload-buttonbar">
          <div class="col-lg-7">
            <!-- The fileinput-button span is used to style the file input field as button -->
            <span class="btn btn-success fileinput-button">
              <i class="glyphicon glyphicon-plus"></i>
              <span>Add files...</span>
              <input type="file" name="files[]" multiple />
            </span>
            <button type="submit" class="btn btn-primary start">
              <i class="glyphicon glyphicon-upload"></i>
              <span>Start upload</span>
            </button>
            <button type="reset" class="btn btn-warning cancel">
              <i class="glyphicon glyphicon-ban-circle"></i>
              <span>Cancel upload</span>
            </button>
            <button type="button" class="btn btn-danger delete">
              <i class="glyphicon glyphicon-trash"></i>
              <span>Delete selected</span>
            </button>
            <input type="checkbox" class="toggle" />
            <!-- The global file processing state -->
            <span class="fileupload-process"></span>
          </div>
          <!-- The global progress state -->
          <div class="col-lg-5 fileupload-progress fade">
            <!-- The global progress bar -->
            <div
              class="progress progress-striped active"
              role="progressbar"
              aria-valuemin="0"
              aria-valuemax="100"
            >
              <div
                class="progress-bar progress-bar-success"
                style="width: 0%;"
              ></div>
            </div>
            <!-- The extended global progress state -->
            <div class="progress-extended">&nbsp;</div>
          </div>
        </div>
        <!-- The table listing the files available for upload/download -->
        <table role="presentation" class="table table-striped">
          <tbody class="files"></tbody>
        </table>
      </form>
      <!--[if gte IE 9]><!-->
      <!-- Carbon Ads -->
      {{-- <p>
        <script
          async
          type="text/javascript"
          src="//cdn.carbonads.com/carbon.js?serve=CKYIL53M&placement=blueimpgithubio"
          id="_carbonads_js"
        ></script>
      </p> --}}
      <!-- Pintura Image Editor info -->
      {{-- <div class="panel panel-default">
        <div class="panel-heading">
          <h3 class="panel-title">
            <a href="https://gumroad.com/a/75084915"
              ><img
                src="img/vendor/pintura-logo.svg"
                alt="Pintura"
                style="max-width: 150px;"
            /></a>
          </h3>
        </div>
        <div class="panel-body">
          <p>
            <a href="https://gumroad.com/a/75084915">Pintura Image Editor</a>
            integrates smoothly with
            <a href="https://github.com/blueimp/jQuery-File-Upload"
              >jQuery File Upload</a
            >
            and creates a super fast image editing experience for your users.
          </p>
          <ul>
            <li>Five Minute Install</li>
            <li>Set Crop Masks and Guides</li>
            <li>Define Aspect Ratio Options</li>
            <li>Rotate, Resize, and Flip Images</li>
            <li>Add Markup and Annotations</li>
            <li>Color Adjustment Controls</li>
            <li>Apply Filter Effects</li>
          </ul>
          <p><a href="https://gumroad.com/a/75084915">Learn more</a></p>
        </div>
      </div>
      <!--<![endif]-->
      <div class="panel panel-default">
        <div class="panel-heading">
          <h3 class="panel-title">Demo Notes</h3>
        </div>
        <div class="panel-body">
          <ul>
            <li>
              The maximum file size for uploads in this demo is
              <strong>999 KB</strong> (default file size is unlimited).
            </li>
            <li>
              Only image files (<strong>JPG, GIF, PNG</strong>) are allowed in
              this demo (by default there is no file type restriction).
            </li>
            <li>
              Uploaded files will be deleted automatically after
              <strong>5 minutes or less</strong> (demo files are stored in
              memory).
            </li>
            <li>
              You can <strong>drag &amp; drop</strong> files from your desktop
              on this webpage (see
              <a
                href="https://github.com/blueimp/jQuery-File-Upload/wiki/Browser-support"
                >Browser support</a
              >).
            </li>
            <li>
              Please refer to the
              <a href="https://github.com/blueimp/jQuery-File-Upload"
                >project website</a
              >
              and
              <a href="https://github.com/blueimp/jQuery-File-Upload/wiki"
                >documentation</a
              >
              for more information.
            </li>
            <li>
              Built with the
              <a href="https://getbootstrap.com/">Bootstrap</a> CSS framework
              and Icons from <a href="https://glyphicons.com/">Glyphicons</a>.
            </li>
          </ul>
        </div>
      </div>
    </div>
    <!-- The blueimp Gallery widget -->
    <div
      id="blueimp-gallery"
      class="blueimp-gallery blueimp-gallery-controls"
      aria-label="image gallery"
      aria-modal="true"
      role="dialog"
      data-filter=":even"
    >
      <div class="slides" aria-live="polite"></div>
      <h3 class="title"></h3>
      <a
        class="prev"
        aria-controls="blueimp-gallery"
        aria-label="previous slide"
        aria-keyshortcuts="ArrowLeft"
      ></a>
      <a
        class="next"
        aria-controls="blueimp-gallery"
        aria-label="next slide"
        aria-keyshortcuts="ArrowRight"
      ></a>
      <a
        class="close"
        aria-controls="blueimp-gallery"
        aria-label="close"
        aria-keyshortcuts="Escape"
      ></a>
      <a
        class="play-pause"
        aria-controls="blueimp-gallery"
        aria-label="play slideshow"
        aria-keyshortcuts="Space"
        aria-pressed="false"
        role="button"
      ></a>
      <ol class="indicator"></ol>
    </div> --}}
    <!-- The template to display files available for upload -->
    <script id="template-upload" type="text/x-tmpl">
      {% for (var i=0, file; file=o.files[i]; i++) { %}
          <tr class="template-upload fade{%=o.options.loadImageFileTypes.test(file.type)?' image':''%}">
              <td>
                  <span class="preview"></span>
              </td>
              <td>
                  <p class="name">{%=file.name%}</p>
                  <strong class="error text-danger"></strong>
              </td>
              <td>
                  <p class="size">Processing...</p>
                  <div class="progress progress-striped active" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0"><div class="progress-bar progress-bar-success" style="width:0%;"></div></div>
              </td>
              <td>
                  {% if (!o.options.autoUpload && o.options.edit && o.options.loadImageFileTypes.test(file.type)) { %}
                    <button class="btn btn-success edit" data-index="{%=i%}" disabled>
                        <i class="glyphicon glyphicon-edit"></i>
                        <span>Edit</span>
                    </button>
                  {% } %}
                  {% if (!i && !o.options.autoUpload) { %}
                      <button class="btn btn-primary start" disabled>
                          <i class="glyphicon glyphicon-upload"></i>
                          <span>Start</span>
                      </button>
                  {% } %}
                  {% if (!i) { %}
                      <button class="btn btn-warning cancel">
                          <i class="glyphicon glyphicon-ban-circle"></i>
                          <span>Cancel</span>
                      </button>
                  {% } %}
              </td>
          </tr>
      {% } %}
    </script>
    <!-- The template to display files available for download -->
    <script id="template-download" type="text/x-tmpl">
      {% for (var i=0, file; file=o.files[i]; i++) { %}
          <tr class="template-download fade{%=file.thumbnailUrl?' image':''%}">
              <td>
                  <span class="preview">
                      {% if (file.thumbnailUrl) { %}
                          <a href="{%=file.url%}" title="{%=file.name%}" download="{%=file.name%}" data-gallery><img src="{%=file.thumbnailUrl%}"></a>
                      {% } %}
                  </span>
              </td>
              <td>
                  <p class="name">
                      {% if (file.url) { %}
                          <a href="{%=file.url%}" title="{%=file.name%}" download="{%=file.name%}" {%=file.thumbnailUrl?'data-gallery':''%}>{%=file.name%}</a>
                      {% } else { %}
                          <span>{%=file.name%}</span>
                      {% } %}
                  </p>
                  {% if (file.error) { %}
                      <div><span class="label label-danger">Error</span> {%=file.error%}</div>
                  {% } %}
              </td>
              <td>
                  <span class="size">{%=o.formatFileSize(file.size)%}</span>
              </td>
              <td>
                  {% if (file.deleteUrl) { %}
                      <button class="btn btn-danger delete" data-type="{%=file.deleteType%}" data-url="{%=file.deleteUrl%}"{% if (file.deleteWithCredentials) { %} data-xhr-fields='{"withCredentials":true}'{% } %}>
                          <i class="glyphicon glyphicon-trash"></i>
                          <span>Delete</span>
                      </button>
                      <input type="checkbox" name="delete" value="1" class="toggle">
                  {% } else { %}
                      <button class="btn btn-warning cancel">
                          <i class="glyphicon glyphicon-ban-circle"></i>
                          <span>Cancel</span>
                      </button>
                  {% } %}
              </td>
          </tr>
      {% } %}
    </script>
    <script
      src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"
      integrity="sha384-nvAa0+6Qg9clwYCGGPpDQLVpLNn0fRaROjHqs13t4Ggj3Ez50XnGQqc/r8MhnRDZ"
      crossorigin="anonymous"
    ></script>
    <!-- The jQuery UI widget factory, can be omitted if jQuery UI is already included -->
    <script src="{{url('')}}/js/jquery.ui.widget.js"></script>
    <!-- The Templates plugin is included to render the upload/download listings -->
    <script src="https://blueimp.github.io/JavaScript-Templates/js/tmpl.min.js"></script>
    <!-- The Load Image plugin is included for the preview images and image resizing functionality -->
    <script src="https://blueimp.github.io/JavaScript-Load-Image/js/load-image.all.min.js"></script>
    <!-- The Canvas to Blob plugin is included for image resizing functionality -->
    <script src="https://blueimp.github.io/JavaScript-Canvas-to-Blob/js/canvas-to-blob.min.js"></script>
    <!-- blueimp Gallery script -->
    <script src="https://blueimp.github.io/Gallery/js/jquery.blueimp-gallery.min.js"></script>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://code.jquery.com/jquery-3.6.0.js"></script>

    <script src="{{url('selfupload/js/vendor/jquery.ui.widget.js')}}"></script>
    <script src="{{url('selfupload/js/tmpl.min.js')}}"></script>
    <script src="{{url('selfupload/js/load-image.all.min.js')}}"></script>
    <script src="{{url('selfupload/js/canvas-to-blob.min.js')}}"></script>
    {{-- <script src="{{url('public/selfupload/js/bootstrap.min.js')}}"></script> --}}
    <script src="{{url('selfupload/js/jquery.blueimp-gallery.min.js')}}"></script>
    <script src="{{url('selfupload/js/jquery.iframe-transport.js')}}"></script>
    <script src="{{url('selfupload/js/jquery.fileupload.js')}}"></script>
    <script src="{{url('selfupload/js/jquery.fileupload-process.js')}}"></script>
    <script src="{{url('selfupload/js/jquery.fileupload-image.js')}}"></script>
    <script src="{{url('selfupload/js/jquery.fileupload-audio.js')}}"></script>
    <script src="{{url('selfupload/js/jquery.fileupload-video.js')}}"></script>
    <script src="{{url('selfupload/js/jquery.fileupload-validate.js')}}"></script>
    <script src="{{url('selfupload/js/jquery.fileupload-ui.js')}}"></script>
    <script src="{{url('selfupload/js/main.js')}}"></script>
    <!-- The XDomainRequest Transport is included for cross-domain file deletion for IE 8 and IE 9 -->
    <!--[if (gte IE 8)&(lt IE 10)]>
      <script src="js/cors/jquery.xdr-transport.js"></script>
    <![endif]-->
    <script type="module">
      // import Pintura Image Editor functionality:
      import { openDefaultEditor } from './js/vendor/pintura.min.js';
      $(function () {
        $('#fileupload').fileupload('option', {
          // When editing a file use Pintura Image Editor:
          edit: function (file) {
            return new Promise((resolve, reject) => {
              const editor = openDefaultEditor({
                src: file,
                imageCropAspectRatio: 1,
              });
              editor.on('process', ({ dest }) => {
                resolve(dest);
              });
              editor.on('close', () => {
                resolve(file);
              });
            });
          }
        });
      });
    </script>       
  </body>
</html>
