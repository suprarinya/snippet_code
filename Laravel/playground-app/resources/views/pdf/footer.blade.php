<div class="cardcode col-12" style="padding: 0;display:none">
    View : <a style="color:red;" href="{{url("autoit?run=visualcode_open\\endo.exe&path=pdf_footer")}}">pdf_footer</a>
    <br><br>
</div>
<table border="0" width="100%">
    <tr>
        <td align="left" width="400">
            
            <font size="2">
            @if(true)
                Signature___________________________, aaa
            @else
                Signature 
                <img src='' width="140" style="position: absolute;border-bottom: 1px solid black;">
                {{nbsp(50)}}
                aaa
            @endif
            </font>
        </td>
        <td align="right" valign="bottom">
            <font size="2">Reported by EndoCapture</font>
        </td>
    </tr>
</table>
