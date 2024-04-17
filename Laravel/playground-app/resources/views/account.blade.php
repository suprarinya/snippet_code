<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>Document</title>
</head>
<body>
    <h4 class="m-3">สร้างบัญชีผู้ใช้งาน</h4>
    <div class="col-lg-12 m-0 mt-4">
        <div class="col-lg">
            <form action="{{url('test')}}" method="post">
                @csrf
                <input type="text" name="event" value="add_new_account" hidden>
                <input type="text" name="us_type" value="5" hidden>
                <div class="row m-0 mt-4">
                    <div class="col-lg">
                        <label for="us_firstname" class="me-5 h4">สังกัดของผู้ใช้งาน &emsp;</label>
                        {{-- <div class="form-check form-check-inline">
                            <input class="form-check-input" type="radio" id="us_check_in" name="us_check" value="0" checked onchange="change_aff(this.value)">
                            <label class="form-check-label h4" for="us_check_in">ภายในสถาบัน</label>
                        </div> --}}
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="radio" id="us_check_out" name="us_check" value="1" onchange="" checked>
                            <label class="form-check-label h4" for="us_check_out">ผู้ใช้งานภายนอก</label>
                        </div>
                    </div>
                </div>
                <div class="col-12">&nbsp;</div>
                    <div class="row m-0 border-bottom mb-5">
                        <div class="col-2 text-right h4">คำนำหน้า<b class="text-danger">*</b> :</div>
                        <div class="col-10 text-right h4">
                            <select id="us_prefix" name="us_prefix" class="form-control form-control-sm" required>
                                    <option value="">เลือก</option>
                                    <option value="นาง">นาง</option>
                                    <option value="นาย">นาย</option>
                                    <option value="นางสาว">นางสาว</option>
                            </select>
                        </div>
                        <div class="col-2 text-right h4">ชื่อ<b class="text-danger">*</b> :</div>
                        <div class="col-10 h4"><input type="text" id="us_firstname" name="us_firstname" class="form-control form-control-sm" required></div>
                        <div class="col-2 text-right h4">ชื่อสกุล :</div>
                        <div class="col-10 h4"><input type="text" id="us_lastname" name="us_lastname" class="form-control form-control-sm" ></div>
                        {{-- <div class="col-2 text-right h4">เลขที่พนักงาน :</div>
                        <div class="col-10 h4"><input type="text" id="us_position_number" name="us_position_number" class="form-control form-control-sm" ></div>
                        <div class="col-2 text-right h4">ตำแหน่ง :</div>
                        <div class="col-10 h4"><input type="text" id="us_position" name="us_position" class="form-control form-control-sm" ></div>
                        <div class="col-2 text-right h4">ระดับ :</div>
                        <div class="col-10 h4"><input type="text" id="us_degree" name="us_degree" class="form-control form-control-sm"  ></div>
                        <div class="col-2 text-right h4">สังกัดฝ่าย :</div>
                        <div class="col-10 h4">
                            <input type="text" id="us_affiliation_inp" name="us_affiliation_inp" class="form-control form-control-sm" style="display: none">
                            <select name="us_affiliation" id="us_affiliation" class="form-control form-control-sm" onchange="get_sector()">
                                <option value="">โปรดเลือกสังกัดฝ่าย</option>
                                @isset($affiliation)
                                    @foreach ($affiliation as $aff)
                                        <option value="{{@$aff->ua_id}}" {{@$user->us_affiliation == @$aff->ua_id ? 'selected' : ''}}>{{@$aff->ua_name}}</option>
                                    @endforeach
                                @endisset
                            </select>
                        </div>
                        <div class="col-2 text-right h4">หน่วยงาน :</div>
                        <div class="col-10 h4">
                            <input type="text" id="us_sector_inp" name="us_sector_inp" class="form-control form-control-sm" style="display: none" >
                            <select name="us_sector" id="us_sector" class="form-control form-control-sm" onchange="get_sub_sector()">
                                <option value="">โปรดเลือกหน่วยงาน/สาขา</option>
                                @isset($sector)
                                    @foreach ($sector as $sec)
                                        @if (isset($user->us_sector) && ($user->us_affiliation == $sec->sec_aff))
                                            <option value="{{@$sec->ua_id}}" {{$user->us_sector == $sec->sec_id ? 'selected' : ''}}>{{@$sec->sec_name}}</option>
                                        @endif
                                    @endforeach
                                @endisset
                            </select>
                        </div>
                        <div class="col-2 text-right h4">หน่วยงานย่อย :</div>
                        <div class="col-10 h4">
                            <input type="text" id="us_sub_sector_inp" name="us_sub_sector_inp" class="form-control form-control-sm" style="display: none">
                            <select name="us_sub_sector" id="us_sub_sector" class="form-control form-control-sm">
                                <option value="">โปรดเลือกหน่วยงานย่อย</option>
                                @isset($sub_sector)
                                    @foreach ($sub_sector as $sub)
                                        @if (isset($user->us_sub_sector) && ($user->us_sector == $sub->uss_sector))
                                            <option value="{{@$sub->uss_id}}" {{ $user->us_sub_sector == $sub->uss_id ? 'selected' : ''}}>{{@$sub->uss_name}}</option>
                                        @endif
                                    @endforeach
                                @endisset
                            </select>
                        </div>
                        <div class="col-2 text-right h4">วันบรรจุ :</div>
                        <div class="col-10 h4"><input type="date" id="us_employ_date" name="us_employ_date" class="form-control form-control-sm" onchange="change_date(this.value)"></div>
                        <div class="col-2 text-right h4">อายุงาน :</div>
                        <div class="col-10 h4"><input type="text" id="us_work_year" name="us_work_year" class="form-control form-control-sm"  ></div> --}}
                        <div class="col-2 text-right h4">เลขประจำตัวประชาชน :</div>
                        <div class="col-10 h4"><input type="text" id="us_id_number" name="us_id_number" class="form-control form-control-sm"  ></div>
                        <div class="col-2 text-right h4">อีเมล์<b class="text-danger">*</b> :</div>
                        <div class="col-10 h4"><input type="email" id="us_email" name="us_email" class="form-control form-control-sm" required ></div>
                        <div class="col-2 text-right h4">เบอร์โทรศัพท์ :</div>
                        <div class="col-10 h4"><input type="text" id="us_phone_number" name="us_phone_number" class="form-control form-control-sm"  ></div>
                    </div>

                    <div class="row m-0 mb-3">
                        <div class="col-2 text-right h4">ระดับการใช้งาน</div>
                        <div class="col-10">
                            <select name="us_type" class="form-control form-control-sm" required id="select_type"  disabled>
                                <option value="">เลือกระดับการใช้งาน</option>
                                <option value="1" selected>Learner</option>
                                {{-- <option value="4" disabled>Teacher</option>
                                <option value="6" disabled>Moderator</option>
                                <option value="0" disabled>Admin</option> --}}
                            </select>
                        </div>
                    </div>
                    {{-- <div class="row m-0 mb-3">
                        <div class="col-2 text-right h4">รายละเอียดผู้ใช้งาน</div>
                        <div class="col-10">
                            <textarea name="us_detail" id="" rows="4" class="form-control form-control-sm"></textarea>
                        </div>
                    </div> --}}
                    <div class="row m-0">
                        <div class="col-2 text-right h4">Username<b class="text-danger">*</b> :</div>
                        <div class="col-8 h4">
                            <input type="text" id="email" name="email" class="form-control form-control-sm" required>
                            <small id="emailHelp" class="form-text text-danger"></small>
                        </div>
                        {{-- <div class="col-2"><button type="button" class="btn btn-primary btn-sm btn-block generate-name">Auto</button></div> --}}
                    </div>
                    <div class="row m-0">
                        <div class="col-2 text-right h4">Password<b class="text-danger">*</b> :</div>
                        <div class="col-8 h4"><input type="text" id="password" name="password" class="form-control form-control-sm" required></div>
                        <!-- <div class="col-1"><button type="button" class="btn btn-primary btn-sm generate-default-pw w-100">Default</button></div> -->
                        <div class="col-2"><button type="button" class="btn btn-primary btn-sm btn-block generate-random-pw w-100">Random</button></div>
                        <div class="col-6">&nbsp;</div>
                    </div>

                <div class="row m-0 mt-5 pt-5 mb-5 pb-5">
                    <div class="col-lg-6 m-auto">
                        <button type="submit" class="btn btn-success w-100" id="submit_btn">สร้างบัญชี</button>
                    </div>
                </div>
            </form>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://code.jquery.com/jquery-3.6.0.js"></script>
    <script>
        $('.generate-random-pw').on('click', function() {
            const random    = (min, max) => Math.floor(Math.random() * (max - min)) + min
            $('#password').val(random(100000, 999999))
        })
    </script>
</body>
</html>