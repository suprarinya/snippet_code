<div id="sr">
    @foreach ($sr_data as $key=>$data)
    @if ($key == 'Data')
        @foreach ($data as $subkey=>$subdata)
            <div class="row">
                {{-- <div class="col p-2 my-2">
                    <b class="h4" style="font-weight: bold;">{{@$subkey}}</b>
                </div> --}}
                <table class="data-list w-left">
                    <tr><b class="text-blue">{{@strtoupper($subkey)}}</b> : </tr>
                </table>
            </div>

            @foreach ($subdata as $head=>$inner)

                @if (is_array($inner))

                    @foreach ($inner as $subhead=>$subinner)

                        @if ($subhead == 'Fetus ID')
                            <div class="col-lg-12 my-2 h6" style="font-weight: bold;">{{$subhead.' : '.$subinner}}</div>
                            @php
                                $fetal_id = $subinner;
                                continue;
                            @endphp
                        @endif
                        @if ($subhead == 'Derivation' || $subhead == 'Equation' || $subhead == 'Selection Status')
                            @php continue; @endphp
                        @endif

                        @if (is_array($subinner))
                            @foreach ($subinner as $subsubhead=>$subsubinner)

                                @if ($subsubhead == 'Fetus ID')
                                    <div class="col-lg-12 my-2 h6" style="font-weight: bold;">{{$subsubhead.' : '.$subsubinner}}</div>
                                    @php
                                        $fetal_id = $subsubinner;
                                        continue;
                                    @endphp
                                @endif
                                @if ($subsubhead == 'Derivation' || $subsubhead == 'Equation' || $subsubhead == 'Selection Status')
                                    @php continue; @endphp
                                @endif

                                @if (is_array($subsubinner))

                                    @foreach ($subsubinner as $subsubsubhead=>$subsubsubinner)

                                        @if ($subsubsubhead == 'Fetus ID')
                                            <div class="col-lg-12 my-2 h6" style="font-weight: bold;">{{$subsubsubhead.' : '.$subsubsubinner}}</div>
                                            @php
                                                $fetal_id = $subsubsubinner;
                                                continue;
                                            @endphp
                                        @endif
                                        @if ($subsubsubhead == 'Derivation' || $subsubsubhead == 'Equation' || $subsubsubhead == 'Selection Status')
                                            @php continue; @endphp
                                        @endif

                                        <table class="data-list w-left">
                                            <tr>
                                                <td style="width:60%"><b>{{@$subsubsubhead}}: </b></td>
                                                <td>{{@ltrim($subsubsubinner)}}</td>
                                                <td></td>
                                                <td></td>
                                                <td></td>
                                            </tr>
                                        </table>

                                    @endforeach
                                @else

                                    <table class="data-list w-left">
                                        <tr>
                                            <td style="width:40%"><b>{{@$subsubhead}}: </b></td>
                                            <td>{{@ltrim($subsubinner)}}</td>
                                            <td></td>
                                            <td></td>
                                            <td></td>
                                        </tr>
                                    </table>
                                @endif

                            @endforeach

                        @else

                            <table class="data-list w-left">
                                <tr>
                                    <td style="width:40%"><b>{{@$subhead}}: </b></td>
                                    <td>{{@ltrim($subinner)}}</td>
                                    <td></td>
                                    <td></td>
                                    <td></td>
                                </tr>
                            </table>
                        @endif
                    @endforeach
                @else

                    <table class="data-list w-left">
                        <tr>
                            <td style="width:40%"><b>{{@$head}}: </b></td>
                            <td>{{@ltrim($inner)}}</td>
                            <td></td>
                            <td></td>
                            <td></td>
                        </tr>
                    </table>
                @endif
            @endforeach
        @endforeach
    @endif
@endforeach
</div>