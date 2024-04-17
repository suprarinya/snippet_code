<!doctype html>
<html>
  <head>
    <title>Literally Canvas</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, user-scalable=no" />
    <link rel="stylesheet" href="http://localhost/playground/laravel/playground-app/public/css/literallycanvas.css ">

    <style type="text/css">
      body {
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        margin: 0;
        background-color: gray;
        height: 2000px;
      }

      .fs-container {
       width: 1000px;
       margin: 50px;
      }

      .literally {
        width: 100%;
        height: 100%;
      }

      .literally img.background, .literally > canvas {
        position: absolute;
      }

      .toolset {
        margin: 1rem;
      }

      .tool {
        background: hsla(199, 26%, 44%, 0.5);
        padding: 0.25rem;
        margin: 0.25rem;
        border-radius: 0.25rem;
        color: #000;
        text-align: center;
        text-decoration: none;
        position: relative; // give after context later
      }

      .tool.current {
        color: #fff;
        background: hsla(199, 26%, 44%, 1);
      }

      .tool:hover {
        text-decoration: underline;
        background: hsla(199, 26%, 44%, 0.75);
      }

      .toolLabel {
        font-size: 1.25rem;
      }

      #tools-sizes.disabled {
        pointer-events: none;
      }

      #tools-sizes.disabled .tool:after {
        content: ' ';
        background: hsla(0, 100%, 100%, 0.75);
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        border-radius: 0.25rem;
      }

    .literally .lc-drawing{left:0px;bottom:0px;}    
    .literally .lc-picker{z-index:-1;}
    .literally .lc-options{z-index:-2;}


    </style>
  </head>

  <body>
    <div class="fs-container">
      <div class="literally"></div>

      <div class="toolset">
        <span class='toolLabel'>Actions:</span>
        <a href="javascript:void(0);" class='tool' id="open-image">Open image</a>
        <a href="javascript:void(0);" class='tool' id="change-size">Change size</a>
        <a href="javascript:void(0);" class='tool' id="reset-size">Reset size</a>
        <a href="javascript:void(0);" class='tool' id="hide-lc">Teardown</a>
        <a href="javascript:void(0);" class='tool' id="show-lc">Setup</a>
        <a href="javascript:void(0);" class='tool' id="clear-lc">Clear</a>
      </div>

      <div class="toolset">
        <span class='toolLabel'>Tools:</span>
        <a href="javascript:void(0);" class='tool' id="tool-pencil">Pencil</a>
        <a href="javascript:void(0);" class='tool' id="tool-eraser">Eraser</a>
        <a href="javascript:void(0);" class='tool' id="tool-text">Text</a>
        <a href="javascript:void(0);" class='tool' id="tool-line">Line</a>
        <a href="javascript:void(0);" class='tool' id="tool-arrow">Arrow</a>
        <a href="javascript:void(0);" class='tool' id="tool-dashed">Dashed Line</a>
        <a href="javascript:void(0);" class='tool' id="tool-ellipse">Ellipse</a>
        <a href="javascript:void(0);" class='tool' id="tool-rectangle">Rectangle</a>
        <a href="javascript:void(0);" class='tool' id="tool-polygon">Polygon</a>
        <a href="javascript:void(0);" class='tool' id="tool-select">Select</a>
      </div>

      <div class="toolset" id="tools-colors">
        <span class='toolLabel'>Colors:</span>
        <a href="javascript:void(0);" class='tool' id="colorTool-black">Black</a>
        <a href="javascript:void(0);" class='tool' id="colorTool-blue">Blue</a>
        <a href="javascript:void(0);" class='tool' id="colorTool-red">Red</a>
      </div>

      <br>
      <div class="svg-container"
          style="display: inline-block; border: 1px solid yellow"></div>
    </div>

    {{-- <script src="../_js_libs/jquery-1.8.2.js"></script>
    <script src="../_js_libs/literallycanvas-core.js"></script> --}}
    <script src="https://code.jquery.com/jquery-3.6.0.js"></script>
    <script src="//cdnjs.cloudflare.com/ajax/libs/react/0.14.7/react-with-addons.js"></script>
    <script src="//cdnjs.cloudflare.com/ajax/libs/react/0.14.7/react-dom.js"></script>
    {{-- <script src="{{url('')}}/js/literallycanvas.js"></script> --}}
    <script src="http://localhost/playground/laravel/playground-app/public/js/literallycanvas.js"></script>




    <script type="text/javascript">
        var lc = null;
        var tools;
        var strokeWidths;
        var colors;

        var setCurrentByName;
        var findByName;

        // the only LC-specific thing we have to do
        var containerOne = document.getElementsByClassName('literally')[0];

        var backgroundImage = new Image()
        backgroundImage.src = 'http://localhost//store//TEST20230829//2023-08-29//64ed6a179d27d246a5031d40_0_TEST20230829_04092309450207_1.png';

        var showLC = function() {
            lc = LC.init(containerOne, {
            snapshot: JSON.parse(localStorage.getItem('drawing')),
            defaultStrokeWidth: 10,
            strokeWidths: [10, 20, 50],
            secondaryColor: 'transparent',
            });
            window.demoLC = lc;

            scale = 1
            if(lc.canvas.width < defaultWidth || lc.canvas.height < defaultHeight){
                //which dimension has the greatest difference and scale based on that
                if( (lc.canvas.width / defaultWidth) < (lc.canvas.height / defaultHeight) ){
                    scale *= (lc.canvas.width / defaultWidth).toFixed(3);
                }else{
                    scale *= (lc.canvas.height / defaultHeight).toFixed(3);
                }
            }

            //attempt to adjust the annotation wrapper to match the scaled image size
            document.getElementById('annotation').style.width = Math.ceil(scale * wrapperWidth) +'px';

            //this will be the new background
            backgroundImageObj = LC.createShape('Image', {x: 0, y: 0, image: img, scale: scale});

            //apply the shape to the canvas
            lc.saveShape(backgroundImageObj);

            // lc.saveShape(LC.createShape('Image', {x: 0, y: 0, image: backgroundImage}));

            // $('.horz-toolbar').remove()
            // $('.lc-picker').remove()

            var save = function() {
                localStorage.setItem('drawing', JSON.stringify(lc.getSnapshot()));
            }

            lc.on('drawingChange', save);
            lc.on('pan', save);
            lc.on('zoom', save);

            $("#open-image").click(function() {
            window.open(lc.getImage({
                scale: 1, margin: {top: 10, right: 10, bottom: 10, left: 10}
            }).toDataURL());
            });

            $("#change-size").click(function() {
            lc.setImageSize(null, 200);
            });

            $("#reset-size").click(function() {
            lc.setImageSize(null, null);
            });

            $("#clear-lc").click(function() {
            lc.clear();
            });

        // Set up our own tools...
        tools = [
          {
            name: 'pencil',
            el: document.getElementById('tool-pencil'),
            tool: new LC.tools.Pencil(lc)
          },{
            name: 'eraser',
            el: document.getElementById('tool-eraser'),
            tool: new LC.tools.Eraser(lc)
          },{
            name: 'text',
            el: document.getElementById('tool-text'),
            tool: new LC.tools.Text(lc)
          },{
            name: 'line',
            el: document.getElementById('tool-line'),
            tool: new LC.tools.Line(lc)
          },{
            name: 'arrow',
            el: document.getElementById('tool-arrow'),
            tool: function() {
              arrow = new LC.tools.Line(lc);
              arrow.hasEndArrow = true;
              return arrow;
            }()
          },{
            name: 'dashed',
            el: document.getElementById('tool-dashed'),
            tool: function() {
              dashed = new LC.tools.Line(lc);
              dashed.isDashed = true;
              return dashed;
            }()
          },{
            name: 'ellipse',
            el: document.getElementById('tool-ellipse'),
            tool: new LC.tools.Ellipse(lc)
          },{
            name: 'tool-rectangle',
            el: document.getElementById('tool-rectangle'),
            tool: new LC.tools.Rectangle(lc)
          },{
            name: 'tool-polygon',
            el: document.getElementById('tool-polygon'),
            tool: new LC.tools.Polygon(lc)
          },{
            name: 'tool-select',
            el: document.getElementById('tool-select'),
            tool: new LC.tools.SelectShape(lc)
          }
        ];

        strokeWidths = [
          {
            name: 10,
            el: document.getElementById('sizeTool-1'),
            size: 10
          },{
            name: 20,
            el: document.getElementById('sizeTool-2'),
            size: 20
          },{
            name: 50,
            el: document.getElementById('sizeTool-3'),
            size: 50
          }
        ];

        colors = [
          {
            name: 'black',
            el: document.getElementById('colorTool-black'),
            color: '#000000'
          },{
            name: 'blue',
            el: document.getElementById('colorTool-blue'),
            color: '#0000ff'
          },{
            name: 'red',
            el: document.getElementById('colorTool-red'),
            color: '#ff0000'
          }
        ];

        setCurrentByName = function(ary, val) {
          ary.forEach(function(i) {
            $(i.el).toggleClass('current', (i.name == val));
          });
        };

        findByName = function(ary, val) {
          var vals;
          vals = ary.filter(function(v){
            return v.name == val;
          });
          if ( vals.length == 0 )
            return null;
          else
            return vals[0];
        };

        // Wire tools
        tools.forEach(function(t) {
          $(t.el).click(function() {
            var sw;

            lc.setTool(t.tool);
            setCurrentByName(tools, t.name);
            setCurrentByName(strokeWidths, t.tool.strokeWidth);
            $('#tools-sizes').toggleClass('disabled', (t.name == 'text'));
          });
        });
        setCurrentByName(tools, tools[0].name);

        // Wire Stroke Widths
        // NOTE: This will not work until the stroke width PR is merged...
        strokeWidths.forEach(function(sw) {
          $(sw.el).click(function() {
            lc.trigger('setStrokeWidth', sw.size);
            setCurrentByName(strokeWidths, sw.name);
          })
        })
        setCurrentByName(strokeWidths, strokeWidths[0].name);

        // Wire Colors
        colors.forEach(function(clr) {
          $(clr.el).click(function() {
            lc.setColor('primary', clr.color)
            setCurrentByName(colors, clr.name);
          })
        })
        setCurrentByName(colors, colors[0].name);

      };

      $(document).ready(function() {
        // disable scrolling on touch devices so we can actually draw
        $(document).bind('touchmove', function(e) {
          if (e.target === document.documentElement) {
            return e.preventDefault();
          }
        });
        showLC();
      });

      $('#hide-lc').click(function() {
        if (lc) {
          lc.teardown();
          lc = null;
        }
      });

      $('#show-lc').click(function() {
        if (!lc) { showLC(); }
      });
    </script>
  </body>
</html>
