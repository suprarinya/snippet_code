<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
.grid-view {
  width: 50%;
  background-color: #f5f2f2;
  padding: 25px;
}

.grid-users {
  background: #f5f5f5;
  padding-bottom: 10px;
  padding-top: 10px;
  padding-right: 0px;
  padding-left: 0px;
  cursor: move;
  border: #000 1px solid;
  text-align: center;
  font-weight: bold;
}

.grid-header,
.grid-footer {
  background: #34bdeb;
  padding-bottom: 5px;
  padding-top: 5px;
  padding-right: 0px;
  padding-left: 0px;
  border: #000 1px solid;
  text-align: center;
  font-weight: bold;
}

.dashed {
  border: 2px dashed #999;
  background: #ede8e8;
  height: 35px;
}


    </style>
</head>
<body>
    <h1>Test Sort</h1>
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js"></script>

{{-- <div class="container">
  <div class="row "> 
    <div class="grid-view">
      <div class="dropzone">
        <div id="header-1" class="grid-header">Header</div>
        <div id="team-1" class="grid-users">DIV 1</div>
        <div id="team-2" class="grid-users">DIV 2</div>
        <div id="header-1" class="grid-footer">Footer</div>
      </div>
    </div>
  </div>
</div> --}}

<div id="">
    <div class="Regel" style="cursor: grab">
        <span class="ui-icon ui-icon-closethick" ></span>
	    <div><input size="23" maxlength="250"></div>
		<div><input size="23" maxlength="50" ></div>
		<div><input name="Links_Omschrijving" size="23" maxlength="100"></div>
		<div>
		    <select>
			    <option value="VerkoopAankoop">Something</option>
				<option>Onething</option>
				<option >AnotherThing</option>
			</select>
		</div>
	</div> 
  
  <br><br>
  
  <div class="Regel" style="cursor: move">
	 <span class="ui-icon ui-icon-closethick" ></span>
     AAAAAAAAAAAAAAAAAAA
  </div>
  <div class="Regel" style="cursor: move">
    <span class="ui-icon ui-icon-closethick" ></span>
    BBBBBBBBBBBBBBBBBBBBBBBBB
  </div>
    
    
    
    
    
    {{-- <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
    <script src="https://ajax.aspnetcdn.com/ajax/jquery.ui/1.8.16/jquery-ui.min.js"></script> --}}
    {{-- <script src="https://cdn.jsdelivr.net/npm/@shopify/draggable@1.0.0-beta.13/lib/draggable.bundle.js"></script>
    <script>
        const sortable = new Draggable.Sortable(document.querySelectorAll('ul'), {
        draggable: 'li'
        });
    </script> --}}
    <script>


// $(".dropzone").sortable({
//   connectWith: ".dropzone",
//   items: ':not(.grid-footer)',
//   update: function(event, ui) {},
//   placeholder: "dashed"
// });
$(".Regel").parent().sortable({});
console.log($(".Regel").parent());
    </script>
</body>
</html>