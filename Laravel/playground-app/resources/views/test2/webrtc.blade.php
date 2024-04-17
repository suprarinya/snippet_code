
<html>
    <head>
        <title>PeerConnection server test page</title>
    </head>
    <script src="https://webrtc.github.io/adapter/adapter-latest.js"></script>

<html lang="en">
    <head>

        <meta name="viewport" content="width=device-width, minimum-scale=1.0, initial-scale=1.0, user-scalable=yes">
        <meta itemprop="name" content="simpl.info: simplest possible examples of HTML, CSS and JavaScript">
        <meta itemprop="image" content="/images/icons/icon192.png">
        <meta name="mobile-web-app-capable" content="yes">
        <meta id="theme-color" name="theme-color" content="#fff">

        <base target="_blank">

        <title>RTCPeerConnection</title>
    
        <style>
            * {
                //border: solid;
            }
            .control_panel {
                margin-top: 10px ;
            }
            video {
                background: #222;
                margin-top: 20px;
            }            
        </style>

    </head>

    <body>

        <table>
            <tr class="server">
                <td style="text-align:left; width:32%;"><font>Server:</font></td>
                <td>
                    <span>
                        <input type="text" id="server" value="http://127.0.0.1:8081" />
                    </span>
                </td>
            </tr>
            <tr class="your_name">
                <td style="text-align:left; width:32%;"><font>Your name:</font></td>
                <td>
                    <span>
                        <input type="text" id="local" value="myclient" />
                        <!-- <input type="text" id="local1" value="myclient1" /> -->
                    </span>
                </td>
            </tr>

        </table>

        <div class="control_panel">
            <!-- <button onclick="addVideo()">ADD</button> -->
            <!-- <button onclick="removeVideo()">REMOVE</button> -->
            <button id="run" onclick="run_process();">Run</button>
            <button id="connect" onclick="OnBtnConnectClick();">Connect</button>
            <button disabled="true" id="disconnect" onclick="OnBtnDisconnectClick();">Disconnect</button>
            <!-- <button onclick="document.getElementById('debug').innerHTML='';">Clear log</button> -->
            <button id="capture" onclick="capture();">Capture</button>

            <button id="rec_start" onclick="rec_start();">Record Start</button>

            <button id="rec_stop" onclick="rec_stop();">Record Stop</button>


        </div>

        <div id="container">
            <video id="remoteVideo" width=1500 height=1000></video> <!--autoplay-->
        </div>
    </body>
</html>
{{-- 
<script src="gaa.js"></script>
<script src="webrtc.js"></script> --}}

<script src="http://localhost/playground/laravel/playground-app/public/js/gaa.js"></script>
<script src="http://localhost/playground/laravel/playground-app/public/js/webrtc.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>

<script src="http://localhost:3000/socket.io/socket.io.js"></script>

    


<script> 

webrtc = new WebrtcClient();
//webrtc2 = new WebrtcClient();

function OnBtnConnectClick()
{
    strLocalName = document.getElementById("local").value.toLowerCase() ;

    if (strLocalName.length == 0) {
        alert("Please input name!");
        document.getElementById("local").focus();

        return ;
    }

    webrtc.connect( strLocalName, document.getElementById("server").value.toLowerCase(), "remoteVideo" );
    //webrtc2.connect( strLocalName, document.getElementById("server1").value.toLowerCase(), "remoteVideo1" );

    document.getElementById("connect").disabled = true;
    document.getElementById("disconnect").disabled = false;
}

function OnBtnDisconnectClick()
{
    webrtc.disconnect();
    //webrtc2.disconnect();

    document.getElementById("connect").disabled = false;
    document.getElementById("disconnect").disabled = true;    
}

// Dennis todo: it doesn't work, since DOMs are released.
window.onbeforeunload = function() { 
    log_info("window.onbeforeunload()");
    webrtc.disconnect();
    //webrtc2.disconnect();
}

var socket = io.connect('http://localhost:3000');


function run_process(){
    // test socket
    socket.emit('chat message', "test_socket")
    // !!!need to kill python from last open!!!
    setTimeout(()=>{socket.emit('chat message', 'kill_camera')}  ,1000);
    // click connect button on html
    setTimeout(()=>{$('#connect').click()}  ,3000);
    // click login button on pyqt5
    setTimeout(()=>{socket.emit('chat message', 'click_login_btn')}  ,5000);
    // click disconnect before start to click connect again, video should show
    setTimeout(()=>{$('#disconnect').click()}  ,6000);
    setTimeout(()=>{$('#connect').click()}  ,7000);
    // prevent sending value to socket twice
    $('#run').prop('disabled', true)
}

function capture(){
    socket.emit('chat message', 'capture')
}

function rec_start(){
    socket.emit('chat message', 'vdo_start')
}

function rec_stop(){
    socket.emit('chat message', 'vdo_stop')
}

</script>

<script>


</script>