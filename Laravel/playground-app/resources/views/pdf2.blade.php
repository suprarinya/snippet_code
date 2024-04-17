<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Invoice</title>

    <style>
      @font-face {
        font-family: "Inter";
        src: "url('')/public/html2pdf/Inter-Regular.ttf" format("truetype");
        font-weight: 400;
        font-style: normal;
      }

      @font-face {
        font-family: "Inter";
        src: "url('')/public/html2pdf/Inter-Medium.ttf" format("truetype");
        font-weight: 500;
        font-style: normal;
      }

      @font-face {
        font-family: "Inter";
        src: "url('')/public/html2pdf/Inter-Bold.ttf" format("truetype");
        font-weight: 700;
        font-style: normal;
      }

      @font-face {
        font-family: "Space Mono";
        src: "url('')/public/html2pdf/SpaceMono-Regular.ttf" format("truetype");
        font-weight: 400;
        font-style: normal;
      }

      body {
        font-size: 0.75rem;
        font-family: "Inter", sans-serif;
        font-weight: 400;
        color: #000000;
        margin: 0 auto;
        position: relative;
      }

      #pspdfkit-header {
        font-size: 0.625rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-weight: 400;
        color: #717885;
        margin-top: 2.5rem;
        margin-bottom: 2.5rem;
        width: 100%;
      }

      .header-columns {
        display: flex;
        justify-content: space-between;
        padding-left: 2.5rem;
        padding-right: 2.5rem;
      }

      .logo {
        height: 1.5rem;
        width: auto;
        margin-right: 1rem;
      }

      .logotype {
        display: flex;
        align-items: center;
        font-weight: 700;
      }

      h2 {
        font-family: "Space Mono", monospace;
        font-size: 1.25rem;
        font-weight: 400;
      }

      h4 {
        font-family: "Space Mono", monospace;
        font-size: 1rem;
        font-weight: 400;
      }

      .page {
        /* margin-left: 5rem;
        margin-right: 5rem; */
      }

      .intro-table {
        display: flex;
        justify-content: space-between;
        margin: 3rem 0 3rem 0;
        border-top: 1px solid #000000;
        border-bottom: 1px solid #000000;
      }

      .intro-form {
        display: flex;
        flex-direction: column;
        border-right: 1px solid #000000;
        width: 50%;
      }

      .intro-form:last-child {
        border-right: none;
      }

      .intro-table-title {
        font-size: 0.625rem;
        margin: 0;
      }

      .intro-form-item {
        padding: 1.25rem 1.5rem 1.25rem 1.5rem;
      }

      .intro-form-item:first-child {
        padding-left: 0;
      }

      .intro-form-item:last-child {
        padding-right: 0;
      }

      .intro-form-item-border {
        padding: 1.25rem 0 0.75rem 1.5rem;
        border-bottom: 1px solid #000000;
      }

      .intro-form-item-border:last-child {
        border-bottom: none;
      }

      .form {
        display: flex;
        flex-direction: column;
        margin-top: 6rem;
      }

      .no-border {
        border: none;
      }

      .border {
        border: 1px solid #000000;
      }

      .border-bottom {
        border: 1px solid #000000;
        border-top: none;
        border-left: none;
        border-right: none;
      }

      .signer {
        display: flex;
        justify-content: space-between;
        gap: 2.5rem;
        margin: 2rem 0 2rem 0;
      }

      .signer-item {
        flex-grow: 1;
      }

      input {
        color: #4537de;
        font-family: "Space Mono", monospace;
        text-align: center;
        margin-top: 1.5rem;
        height: 4rem;
        width: 100%;
        box-sizing: border-box;
      }

      input#date,
      input#notes {
        text-align: left;
      }

      input#signature {
        height: 8rem;
      }

      .intro-text {
        width: 60%;
      }

      .table-box table,
      .summary-box table {
        width: 100%;
        font-size: 0.625rem;
      }

      .table-box table {
        padding-top: 2rem;
      }

      .table-box td:first-child,
      .summary-box td:first-child {
        width: 50%;
      }

      .table-box td:last-child,
      .summary-box td:last-child {
        text-align: right;
      }

      .table-box table tr.heading td {
        border-top: 1px solid #000000;
        border-bottom: 1px solid #000000;
        height: 1.5rem;
      }

      .table-box table tr.item td,
      .summary-box table tr.item td {
        border-bottom: 1px solid #d7dce4;
        height: 1.5rem;
      }

      .summary-box table tr.no-border-item td {
        border-bottom: none;
        height: 1.5rem;
      }

      .summary-box table tr.total td {
        border-top: 1px solid #000000;
        border-bottom: 1px solid #000000;
        height: 1.5rem;
      }

      .summary-box table tr.item td:first-child,
      .summary-box table tr.total td:first-child {
        border: none;
        height: 1.5rem;
      }

      #pspdfkit-footer {
        font-size: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 500;
        color: #717885;
        margin-top: 2.5rem;
        bottom: 2.5rem;
        position: absolute;
        width: 100%;
      }

      .footer-columns {
        display: flex;
        justify-content: space-between;
        padding-left: 2.5rem;
        padding-right: 2.5rem;
      }
    </style>

    <!-- html2pdf CDN link -->
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"
      integrity="sha512-GsLlZN/3F2ErC5ifS5QtgpiJtWd43JWSuIgh7mbzZ8zBps+dvLusV+eNQATqgA/HdeKFVgA5v3S/cIrLF7QnIg=="
      crossorigin="anonymous"
      referrerpolicy="no-referrer"
    ></script>
  </head>

  <body>
    <button id="download-button">Download as PDF</button>
    <div id="invoice">
        {{-- <div id="pspdfkit-header">
            <div class="header-columns">
                <div class="logotype">
                    <img class="logo" src="{{url('')}}/html2pdf/logo.svg" />
                    <p>Company</p>
                </div>
                <p>[Company Info]</p>
            </div>
        </div> --}}
    

    {{-- <div class="page" style="page-break-after: always">
        <div>
          <h2>Invoice #</h2>
        </div>

        <div class="intro-table">
          <div class="intro-form intro-form-item">
            <p class="intro-table-title">Billed To:</p>
            <p>
              Company Ltd.<br />
              Address<br />
              Country<br />
              VAT ID: ATU12345678
            </p>
          </div>

          <div class="intro-form">
            <div class="intro-form-item-border">
              <p class="intro-table-title">Payment Date:</p>
              <p>November 22nd 2021</p>
            </div>

            <div class="intro-form-item-border">
              <p class="intro-table-title">Payment Method:</p>
              <p>Bank Transfer</p>
            </div>
          </div>
        </div>

        <div class="table-box">
          <table cellpadding="0" cellspacing="0">
            <tbody>
              <tr class="heading">
                <td>Description</td>
                <td>QTY</td>
                <td>Unit Price</td>
                <td>Total</td>
              </tr>

              <tr class="item">
                <td></td>
                <td></td>
                <td></td>
                <td></td>
              </tr>

              <tr class="item">
                <td></td>
                <td></td>
                <td></td>
                <td></td>
              </tr>

              <tr class="item">
                <td></td>
                <td></td>
                <td></td>
                <td></td>
              </tr>

              <tr class="item">
                <td></td>
                <td></td>
                <td></td>
                <td></td>
              </tr>

              <tr class="item">
                <td></td>
                <td></td>
                <td></td>
                <td></td>
              </tr>

              <tr class="item">
                <td></td>
                <td></td>
                <td></td>
                <td></td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="summary-box">
          <table cellpadding="0" cellspacing="0">
            <tbody>
              <tr class="item">
                <td></td>
                <td>Subtotal:</td>
                <td></td>
              </tr>

              <tr class="item">
                <td></td>
                <td>Discount:</td>
                <td></td>
              </tr>

              <tr class="item">
                <td></td>
                <td>Subtotal Less Discount:</td>
                <td></td>
              </tr>

              <tr class="item">
                <td></td>
                <td>Tax Rate:</td>
                <td></td>
              </tr>

              <tr class="item">
                <td></td>
                <td>Total Tax:</td>
                <td></td>
              </tr>

              <tr class="item">
                <td></td>
                <td>Shipping/Handling:</td>
                <td></td>
              </tr>

              <tr class="no-border-item">
                <td></td>
                <td>Total Due:</td>
                <td></td>
              </tr>

              <tr class="total">
                <td></td>
                <td>Amount Paid:</td>
                <td></td>
              </tr>
            </tbody>
          </table>
        </div>
    </div> --}}

    {{-- <div class="page" style="page-break-after: always">
        <div>
          <h4>Thank you for your purchase!</h4>
        </div>

        <div class="form">
          <label for="notes" class="label"> Notes: </label>
          <input type="text" id="notes" class="border-bottom" value="" />
        </div>

        <div class="signer">
          <div class="form signer-item">
            <label for="date" class="label">Date:</label>
            <input
              type="text"
              id="date"
              class="border-bottom"
              value="01/01/2021"
            />
          </div>

          <div class="form signer-item">
            <label for="signature" class="label">Issued by:</label>
            <input
              type="text"
              id="signature"
              class="border"
              value="Sign Here"
            />
          </div>
        </div>
    </div> --}}

        {{--  --}}

    @php
        
        // $x_key = 0.3
        // $x_value = 3.3
        // $y_body = 2.3
        // $y_picture = 2.3
        // $x_picture = 5.5
        $line_num = 0;
        $line_fix = 33;
        // $pic_num = 0
        // $pic_fix = 3
        // $new_pageheight = $pageHeight + 1
    @endphp

    {{-- @for ($i = 0; $i < 100; $i++)
        @php
            $line_num = $line_num > $line_fix ? 0 : $line_num;
            $is_page = $line_num >= $line_fix ? 'page' : '';
            $is_style = $line_num >= $line_fix ? 'page-break-after: always' : '';
        @endphp
        @if ($line_num == 0)
            <div id="pspdfkit-header">
                <div class="header-columns">
                    <div class="logotype">
                        <img class="logo" src="{{url('')}}/html2pdf/logo.svg" />
                        <p>Company</p>
                    </div>
                    <p>[Company Info]</p>
                </div>
            </div>
        @endif
        
        @php
            $line_num += 1;
        @endphp
        @if ($line_num == $line_fix+1)
            <p >{{$i}} - {{$line_num}} - {{$is_page}}</p>
            <div class="{{$is_page}}" style="{{$is_style}}">
                <p>footer</p>
            </div>
        @else
        <p class="{{$is_page}}" style="{{$is_style}}">{{$i}} - {{$line_num}} - {{$is_page}}</p>
        @endif
    @endfor --}}

    <div id="sr">
        @foreach ($sr_data as $key=>$data)
            @if ($key == 'Data')
                @foreach ($data as $subkey=>$subdata)
                    <div  class="row">
                        <div class="col p-2 my-2">
                            <b class="h4" style="font-weight: bold;">{{@$subkey}}</b>
                        </div>
                        @php
                                $line_num = $line_num > $line_fix ? 0 : $line_num;
                                $is_page = $line_num >= $line_fix ? 'page' : '';
                                $is_style = $line_num >= $line_fix ? 'page-break-after: always' : '';
                            @endphp
                        <table class="data-list w-left" >
                            <tr><b class="text-blue " >{{@strtoupper($subkey)}} - {{$line_num}}</b> : </tr>
                        </table>
                        @php
                            $line_num += 1;
                        @endphp
                    </div>
        
                    @foreach ($subdata as $head=>$inner)
        
                        @if (is_array($inner))
        
                            @foreach ($inner as $subhead=>$subinner)
        
                                @if ($subhead == 'Fetus ID')
                                    @php
                                        $line_num = $line_num > $line_fix ? 0 : $line_num;
                                        $is_page = $line_num >= $line_fix ? 'page' : '';
                                        $is_style = $line_num >= $line_fix ? 'page-break-after: always' : '';
                                    @endphp
                                    <div class="col-lg-12 my-2 h6" style="font-weight: bold;">{{$subhead.' : '.$subinner}} - {{$line_num}} - {{$is_page}} - {{$is_style}}</div>
                                    @php
                                        $fetal_id = $subinner;
                                        $line_num += 1;
                                        continue;
                                    @endphp
                                @endif
                                @if ($subhead == 'Derivation' || $subhead == 'Equation' || $subhead == 'Selection Status')
                                    @php continue; @endphp
                                @endif
        
                                @if (is_array($subinner))
                                    @foreach ($subinner as $subsubhead=>$subsubinner)
        
                                        @if ($subsubhead == 'Fetus ID')
                                            @php
                                                $line_num = $line_num > $line_fix ? 0 : $line_num;
                                                $is_page = $line_num >= $line_fix ? 'page' : '';
                                                $is_style = $line_num >= $line_fix ? 'page-break-after: always' : '';
                                            @endphp
                                            <div class="col-lg-12 my-2 h6" style="font-weight: bold;">{{$subsubhead.' : '.$subsubinner}} - {{$line_num}} - {{$is_page}} - {{$is_style}}</div>
                                            @php
                                                $fetal_id = $subsubinner;
                                                $line_num += 1;
                                                continue;
                                            @endphp
                                        @endif
                                        @if ($subsubhead == 'Derivation' || $subsubhead == 'Equation' || $subsubhead == 'Selection Status')
                                            @php continue; @endphp
                                        @endif
        
                                        @if (is_array($subsubinner))
        
                                            @foreach ($subsubinner as $subsubsubhead=>$subsubsubinner)
        
                                                @if ($subsubsubhead == 'Fetus ID')
                                                    @php
                                                        $line_num = $line_num > $line_fix ? 0 : $line_num;
                                                        $is_page = $line_num >= $line_fix ? 'page' : '';
                                                        $is_style = $line_num >= $line_fix ? 'page-break-after: always' : '';
                                                    @endphp
                                                    <div class="col-lg-12 my-2 h6" style="font-weight: bold;">{{$subsubsubhead.' : '.$subsubsubinner}} - {{$line_num}} - {{$is_page}} - {{$is_style}}</div>
                                                    @php
                                                        $fetal_id = $subsubsubinner;
                                                        $line_num += 1;
                                                        continue;
                                                    @endphp
                                                @endif
                                                @if ($subsubsubhead == 'Derivation' || $subsubsubhead == 'Equation' || $subsubsubhead == 'Selection Status')
                                                    @php continue; @endphp
                                                @endif

                                                @php
                                                    $line_num = $line_num > $line_fix ? 0 : $line_num;
                                                    $is_page = $line_num >= $line_fix ? 'page' : '';
                                                    $is_style = $line_num >= $line_fix ? 'page-break-after: always' : '';
                                                @endphp

                                                <table class="data-list w-left" style="">
                                                    <tr>
                                                        <td style="width:60%"><b>{{@$subsubsubhead}}: </b></td>
                                                        <td>{{@ltrim($subsubsubinner)}}  - {{$line_num}} - {{$is_page}} - {{$is_style}}</td>
                                                        <td></td>
                                                        <td></td>
                                                        <td></td>
                                                    </tr>
                                                </table>

                                                @php
                                                    $line_num += 1;
                                                @endphp
        
                                            @endforeach
                                        @else

                                            @php
                                                $line_num = $line_num > $line_fix ? 0 : $line_num;
                                                $is_page = $line_num >= $line_fix ? 'page' : '';
                                                $is_style = $line_num >= $line_fix ? 'page-break-after: always' : '';
                                            @endphp
        
                                            <table class="data-list w-left" style="">
                                                <tr>
                                                    <td style="width:40%"><b>{{@$subsubhead}}: </b></td>
                                                    <td>{{@ltrim($subsubinner)}}  - {{$line_num}} - {{$is_page}} - {{$is_style}}</td>
                                                    <td></td>
                                                    <td></td>
                                                    <td></td>
                                                </tr>
                                            </table>
                                            @php
                                                $line_num += 1;
                                            @endphp
                                        @endif
        
                                    @endforeach
        
                                @else

                                    @php
                                        $line_num = $line_num > $line_fix ? 0 : $line_num;
                                        $is_page = $line_num >= $line_fix ? 'page' : '';
                                        $is_style = $line_num >= $line_fix ? 'page-break-after: always' : '';
                                    @endphp
        
                                    <table class="data-list w-left" style="">
                                        <tr>
                                            <td style="width:40%"><b>{{@$subhead}}: </b></td>
                                            <td>{{@ltrim($subinner)}}  - {{$line_num}} - {{$is_page}} - {{$is_style}}</td>
                                            <td></td>
                                            <td></td>
                                            <td></td>
                                        </tr>
                                    </table>
                                    @php
                                        $line_num += 1;
                                    @endphp
                                @endif
                            @endforeach
                        @else

                            @php
                                $line_num = $line_num > $line_fix ? 0 : $line_num;
                                $is_page = $line_num >= $line_fix ? 'page' : '';
                                $is_style = $line_num >= $line_fix ? 'page-break-after: always' : '';
                            @endphp
        
                            <table class="data-list w-left" style="">
                                <tr>
                                    <td style="width:40%"><b>{{@$head}}: </b></td>
                                    <td>{{@ltrim($inner)}}  - {{$line_num}} - {{$is_page}} - {{$is_style}}</td>
                                    <td></td>
                                    <td></td>
                                    <td></td>
                                </tr>
                            </table>
                            @php
                                $line_num += 1;
                            @endphp
                        @endif
                    @endforeach
                @endforeach
            @endif
        @endforeach
    </div> 
        {{--  --}}
    <div id="pspdfkit-footer">
        <div class="footer-columns">
          <span>Invoice</span>
          {{-- <span>Page {{ pageNumber }} of {{ pageCount }}</span> --}}
        </div>
      </div>
    </div>
</div>
    <script>
      const button = document.getElementById("download-button");

      function generatePDF() {
        // Choose the element that your content will be rendered to.
        const element = document.getElementById("sr");
        // Choose the element and save the PDF for your user.
        // html2pdf().set({
        //     pagebreak: { mode: ['avoid-all', 'css', 'legacy'] }
        // });
        // html2pdf().from(element).save();
        html2pdf()
            .from(element)
            .outputPdf('datauristring')
            .then((uristring) => {
                console.log(uristring);
            });

      }

      button.addEventListener("click", generatePDF);
    </script>
  </body>
</html>