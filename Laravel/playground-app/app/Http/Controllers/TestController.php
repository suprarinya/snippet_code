<?php

namespace App\Http\Controllers;

use App\Models\Car;
use App\Models\Color;
use App\Models\Mongo;
use Exception;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Hash;
use Carbon\Carbon;

class TestController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {

        // Path ของ dicom SR file
        $dicom_file_path = 'D:\laragon\htdocs\playground\laravel\playground-app\asset\sr_dicom\sr_temp';
        // สำคัญ: ตั้งค่า environment variable ของ Path ในเครื่องที่รันโค้ด ไปยังโฟลเดอร์ bin ของ dcmtk ที่โหลดมา!!!
        $dcmtk_path = 'C:\Users\bright\Downloads\dcmtk-3.6.7-win64-dynamic\bin';
        // Path ของ text file
        $text_file_path = 'D:\laragon\htdocs\playground\laravel\playground-app\asset\sr_text';

        // get files in folder
        $files = file_exists($dicom_file_path) ? scandir($dicom_file_path) : 0;
        for($i=0;$i<count($files);$i++){
            if(file_exists($dicom_file_path."\\$files[$i]") && is_file($dicom_file_path."\\$files[$i]")){
                $command = "dsrdump +f +U8 +Ps $dicom_file_path\\$files[2]";
                $output = shell_exec($command);
                $explode = explode("\n", $output);
                // dd($command, $explode);
                $dict = $this->change_to_array(array_values(array_filter($explode)));
                dd($dict);

                $json_unit_dict = $this->array_to_json($dict['unit']);
                $json_unitless_dict = $this->array_to_json($dict['unitless']);

                // save to database
                $this->save_to_database($json_unitless_dict);
                
                // create text file
                // file_put_contents("$text_file_path\data$i.txt", $json_unitless_dict);
            }
        }
        echo 'success';
    }

    function save_to_database($json){
        $i['sr_json'] = $json;
        $add = DB::table('pg_srdicom')->insert($i);
        return $add;
    }

    // function change_to_array($explode){
    //     $this_dict = [];
    //     $this_unitless_dict = [];
    //     foreach ($explode as $line) {
    //         dd($explode);
    //         if(str_contains('has properties', $line) == false){
    //             $text_str = '';
    //             if(str_contains($line, 'SR Document')){
    //                 $this_dict['type'] = $line;
    //             }
    
    //             if(str_contains($line, ' :')){
    //                 $text_arr = explode(':', $line);
    //                 $this_dict[rtrim($text_arr[0])] = $this->remove_special_char(ltrim($text_arr[1]));
    //                 $this_unitless_dict[rtrim($text_arr[0])] = $this->remove_special_char(ltrim($text_arr[1]));
    //             }
    
    //             if(str_contains($line, '"')){
    //                 $text_arr = explode('"', $line);
    //                 $number = count($text_arr);
    //                 if(str_contains($line, 'SEPERATE')){
    //                     $this_dict[$text_arr[1]] = '';
    //                     $this_unitless_dict[$text_arr[1]] = '';
    //                 } else {
    //                     if($number > 3){
    //                         $z = range(3, $number-1);
    //                         $last_number = $z[array_key_last($z)];
    //                         foreach ($z as $n) {
    //                             $new_line = ltrim(str_replace('\n', '', $text_arr[$n]));
    //                             $text_str = $text_str.$new_line;
    //                             if(str_contains($text_arr[$n-1], '(') && $n == $last_number){
    //                                 $text_str = $text_str.')';
    //                             }
    //                         }
    //                         $this_dict[rtrim($text_arr[1])] = $this->remove_special_char($text_str);
    //                         $this_unitless_dict[rtrim($text_arr[1])] = $this->remove_special_char(explode('(', $text_str)[0]);
    //                     }   
    //                 }
    //             }
    //         }
    //     }
    //     $dict['unit'] = $this_dict;
    //     $dict['unitless'] = $this_unitless_dict;
    //     return $dict;
    // }

    function is_match_head($word){
        $head = [
            "Patient Characteristics", "Summary", "Fetal Biometry", "Biophysical Profile", "Fetal Cranium",
            "Early Gestation", "Fetal Long Bones", "Fetal Heart", "Pelvis and Uterus", "Fetal Biometry Ratios",
            "Findings", "User-defined concepts"
        ];

        if(in_array($word, $head)){
            return true;
        } else {
            return false;
        }

    }

    function change_to_array($explode){
        // dd($explode);
        $this_dict = [];
        $this_unitless_dict = [];
        // dd($explode);
        $main = [];
        $sub = [];
        for ($i=0; $i < count($explode) ; $i++) {
            $line = $explode[$i];
            $text_arr = explode('"', $line);
            $text_str = '';

            if(str_contains($explode[$i], ': ')){
                $text_arr = explode(':', $line);
                $this_unitless_dict[rtrim($text_arr[0])] = $this->remove_special_char(ltrim($text_arr[1]));
                continue;
            } else if(str_contains($explode[$i], '<CONTAINER:' )){
                $this_unitless_dict['report type'] = $text_arr[1];
                continue;
            } else if(str_contains($explode[$i], 'contains') || str_contains($explode[$i], 'has') || str_contains($explode[$i], 'inferred')){
                array_push($sub, $explode[$i]);
                if(isset($explode[$i+1])){
                    $text_arr2 = explode('"', $explode[$i+1]);
                    if($this->is_match_head($text_arr2[1])){
                        array_push($main, $sub);
                        $sub = [];
                    }
                }
            }
        }

        $this_unitless_dict['Data'] = $this->change_to_associatice_array($main);
        dd($this_unitless_dict);

        // dd('main: ', $main);

        $dict['unit'] = $this_dict;
        $dict['unitless'] = $this_unitless_dict;
        return $dict;
    }

    function change_to_associatice_array($array){
        $ass_arr = [];
        $fetal_biometry         = [];
        $biophysical_profile    = [];
        $fetal_cranium          = [];
        $early_gestation        = [];
        $fetal_long_bones       = [];
        $fetal_heart            = [];
        $pelvis                 = [];
        $fetal_biometry_ratios  = [];
        $finding                = [];

        foreach ($array as $index => $arr) {
            $exp = explode('"', $arr[0]);
            $head = $exp[1];

            // create head ass array
            foreach($arr as $in=>$line){
                if($in == 0){
                    $ass_arr[$head] = [];
                } else {
                    if($head == 'Patient Characteristics'){
                        $exp = explode('"', $line);
                        $ass_arr[$head][$exp[1]] = $exp[3];
                    } 
                }              
            }

            if($head == 'Summary'){
                $sub = [];
                $sub['Fetus Summary'] = [];
                // $main['Fetus Summary'] = [[fetus id],[fetus id],[fetus id]]
                $summary_arr = $this->get_only_id_data($head, $arr);
                for($i=0; $i<count($summary_arr); $i++){
                    if(str_contains($summary_arr[$i][0], 'Fetus Summary')){
                        $subset = [];
                        for($j=1; $j<count($summary_arr[$i]); $j++){
                            $line = explode('"', $summary_arr[$i][$j]);
                            $subset[$line[1]] = ($line[1]=='Equation'||$line[1]=='Selection Status') ? $this->remove_special_char($line[2]).$line[3] : $line[3];
                        }
                        if(isset($subset) && $subset != null){
                            array_push($sub['Fetus Summary'], $subset);
                        }                
                    } else {
                        for($k=1; $k<count($summary_arr[$i]); $k++){
                            $line = explode('"', $summary_arr[$i][$k]);
                            $sub[$line[1]] = $line[3];
                        }
                    }
                }
                $ass_arr[$head] = $sub;
            }


            if($head == 'Fetal Biometry'){
                $sub = $this->get_array($head, $arr);
                array_push($fetal_biometry, $sub);
            }

            if($head == 'Biophysical Profile'){
                $bio_arr = $this->get_only_id_data($head, $arr);
                // dd($bio_arr, 'ff');
                $sub = [];
                $sub['Data'] = [];
                $subset = [];
                for ($i=0; $i < count($bio_arr); $i++) { 
                    if($i == 0){    
                        $line = explode('"', $bio_arr[$i][0]);
                        $sub[$line[1]] = $line[3];
                    } else {
                        $subset = [];
                        for($j=0; $j<count($bio_arr[$i]); $j++){
                            $line = explode('"', $bio_arr[$i][$j]);
                            $subset[$line[1]] = ($line[1]=='Equation'||$line[1]=='Selection Status') ? $this->remove_special_char($line[2]).$line[3] : $line[3];
                        }
                        array_push($sub['Data'], $subset);
                    }
                }
                array_push($biophysical_profile, $sub);
            }

            if($head == 'Fetal Cranium'){
                $sub = $this->get_array($head, $arr);
                array_push($fetal_cranium, $sub);
            }

            if($head == 'Early Gestation'){
                $sub = $this->get_array($head, $arr);
                array_push($early_gestation, $sub);
            }

            if($head == 'Fetal Long Bones'){
                $sub = $this->get_array($head, $arr);
                array_push($fetal_long_bones, $sub);
            }

            if($head == 'Fetal Heart'){
                $sub = $this->get_array($head, $arr);
                array_push($fetal_heart, $sub);
            }

            if($head == 'Pelvis and Uterus'){
                $pelvis_arr = $this->get_only_id_data($head, $arr);
                $sub = [];
                $subset = [];
                for($i=0; $i<count($pelvis_arr);$i++){

                    if(is_array($pelvis_arr[$i])){
                        for ($j=0; $j < count($pelvis_arr[$i]) ; $j++) { 
                            $line = explode('"', $pelvis_arr[$i][$j]);
                            array_push($subset, $line[3]);
                        }
                        $sub['Cervix Length'] = $subset;
                    } else {
                        $line = explode('"', $pelvis_arr[$i]);
                        $sub[$line[1]] = $line[3];
                    }
                }
                array_push($pelvis, $sub);
            }

            if($head == 'Fetal Biometry Ratios'){
                $sub = [];
                for($i=1; $i<count($arr);$i++){
                    $line = explode('"', $arr[$i]);
                    $sub[$line[1]] = $line[3];
                }
                array_push($fetal_biometry_ratios, $sub);
            }

            if($head == 'Findings'){
                $finding_arr = $this->get_only_id_data($head, $arr);
                $sub = [];
                // dd($finding_arr[0], str_contains($finding_arr[0], 'Amniotic Sac'));
                if(isset($finding_arr)){
                    if(!is_array($finding_arr[0])&&str_contains($finding_arr[0], 'Amniotic Sac')){
                        for($i=0; $i<count($finding_arr);$i++){
                            $line = explode('"', $finding_arr[$i]);
                            $sub[$line[1]] = $line[3];
                        }
                        array_push($finding, $sub);
                    } 
                    else if(is_array($finding_arr[0])&&str_contains($finding_arr[0][0], 'Embryonic Vascular Structure')) {
                        // dd($finding_arr);
                        for ($i=0; $i < count($finding_arr) ; $i++) { 
                            $head = explode('"', $finding_arr[$i][0]);
                            $subset = [];
                            for ($j=0; $j < count($finding_arr[$i]); $j++) { 
                                $line = explode('"', $finding_arr[$i][$j]);
                                if($i == 0){
                                    $sub[$line[1]] = $line[3];
                                } else {
                                    if(!str_contains($finding_arr[$i][$j], 'SEPARATE')){
                                        if(str_contains($finding_arr[$i][$j], 'Selection Status')){
                                            continue;
                                        }
                                        $subset[$line[1]] = $line[3];
                                    }
                                }
                            }

                            if($i!=0){
                                $sub[$head[1]] = $subset;
                            }
                        }
                        array_push($finding, $sub);
                    } else if(is_array($finding_arr[0])&&str_contains($finding_arr[0][0], 'Ovary')){
                        // dd($finding_arr);
                        $k =1;
                        for ($i=0; $i < count($finding_arr) ; $i++) { 
                            $head = explode('"', $finding_arr[$i][0]);
                            $subset = [];
                            for ($j=0; $j < count($finding_arr[$i]); $j++) { 
                                $line = explode('"', $finding_arr[$i][$j]);
                                if($i == 0){
                                    $sub[$line[1]] = $line[3];
                                } else {
                                    if(!str_contains($finding_arr[$i][$j], 'SEPARATE')){
                                        if(str_contains($finding_arr[$i][$j], 'Selection Status') || str_contains($finding_arr[$i][$j], 'Derivation')){
                                            continue;
                                        }
                                        $subset[$line[1]] = $line[3];
                                    }
                                }
                            }

                            if($i!=0){
                                $sub[$head[1].$k] = $subset;
                                $k++;
                            }
                        }
                        array_push($finding, $sub);
                    }
                }
            }


        }

        $ass_arr['Fetal Biometry'] = $fetal_biometry;
        $ass_arr['Biophysical Profile'] = $biophysical_profile;
        $ass_arr['Fetal Cranium'] = $fetal_cranium;
        $ass_arr['Early Gestation'] = $early_gestation;
        $ass_arr['Fetal Long Bones'] = $fetal_long_bones;
        $ass_arr['Fetal Heart'] = $fetal_heart;
        $ass_arr['Pelvis and Uterus'] = $pelvis;
        $ass_arr['Fetal Biometry Ratios'] = $fetal_biometry_ratios;
        $ass_arr['Findings'] = $finding;

        return $ass_arr;
    }

    function get_only_id_data($head, $array){
        $main = [];
        $sub = [];
        if($head == 'Summary'){ 
            for ($i=0; $i < count($array) ; $i++) { 
                array_push($sub, $array[$i]);
                if(isset($array[$i+1])){
                    if(str_contains($array[$i+1], 'Fetus Summary')){
                        array_push($main, $sub);
                        $sub = [];
                    }
                }
            }
            array_push($main, $sub);
            return $main;
        } else if ($head == 'Fetal Biometry' || $head == 'Fetal Cranium' || $head == 'Early Gestation'
                   || $head == 'Fetal Long Bones' || $head == 'Fetal Heart') {
            for($i=1; $i<count($array); $i++){
                array_push($sub, $array[$i]);
                if(isset($array[$i+1])){
                    if($i == 1){
                        if(str_contains($array[$i+1], 'Biometry Group')){
                            array_push($main, $sub);
                            $sub = [];
                        }
                    } else {
                        if(str_contains($array[$i+1], 'Biometry Group')){
                            array_push($main, $sub);
                            $sub = [];
                        }
                    }
                }
            }
            return $main;
        } else if ($head == 'Biophysical Profile'){
            for($i=1; $i<count($array); $i++){
                array_push($sub, $array[$i]);
                if(isset($array[$i+1])){
                    if($i == 1){
                        if(str_contains($array[$i+1], 'contains NUM:')){
                            array_push($main, $sub);
                            $sub = [];
                        }
                    } else {
                        if(str_contains($array[$i+1], 'contains NUM:')){
                            array_push($main, $sub);
                            $sub = [];
                        }
                    }
                }
            }
            return $main;
            // dd($main);
        } else if ($head == 'Pelvis and Uterus'){
            for($i=1; $i<count($array); $i++){
                if(str_contains($array[$i], 'Cervix Length')){
                    array_push($sub, $array[$i]);
                } else {
                    array_push($main, $array[$i]);
                }
            }
            array_push($main, $sub);
            return $main;
        } else if ($head == 'Findings'){
            if(str_contains($array[1], 'Amniotic Sac')){
                for ($i=1; $i < count($array); $i++) { 
                    if(str_contains($array[$i], 'Selection Status')){
                        continue;
                    }
                    array_push($sub, $array[$i]);
                }
                return $sub;
            } else if(str_contains($array[1], 'Embryonic Vascular Structure') || str_contains($array[1], 'Ovary')) {
                for($i=1; $i<count($array); $i++){
                    array_push($sub, $array[$i]);
                    if(isset($array[$i+1])){
                        if(str_contains($array[$i+1], 'SEPARATE')){
                            array_push($main, $sub);
                            $sub = [];
                        }
                    }
                }
                array_push($main, $sub);
                return $main;
            } 

        }
    }

    function get_array($head, $arr){
        $array = $this->get_only_id_data($head, $arr);
        $sub = [];
        $sub['Biometry Group'] = [];
        $subset = [];
        for ($i=0; $i < count($array); $i++) { 
            if($i == 0){    
                $line = explode('"', $array[$i][0]);
                $sub[$line[1]] = $line[3];
            } else {
                $subset = [];
                for($j=1; $j<count($array[$i]); $j++){
                    $line = explode('"', $array[$i][$j]);
                    $subset[$line[1]] = $line[3];
                }
                array_push($sub['Biometry Group'], $subset);
            }
        }
        return $sub;
    }


    function remove_special_char($string){
        if(str_contains($string, '>')){
            $string = str_replace('>', '', $string);
        }
        if(str_contains($string, ')=(')){
            $string = str_replace(')=(', '', $string);
        }
        return $string;
    }

    function array_to_json($array){
        $json = json_encode($array, JSON_UNESCAPED_UNICODE);
        return $json;
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $r)
    {

        
        if(isset($r->event)){
            if($r->event=='get_file_content')                {return $this->get_file_content($r);}
            if($r->event=='add_new_account')                 {return $this->add_new_account($r);}
            if($r->event=='change_bitrate')                  {return $this->change_bitrate($r);}
            if($r->event=='get_progress')                    {return $this->get_progress($r);}
            if($r->event=='get_form')                        {return $this->get_form($r);}
            if($r->event=='get_form_html')                   {return $this->get_form_html($r);}





        }
        // dd($r->all());

        if ($r->hasFile('files')) {
            $images = $r->file('files');
            foreach($images as $img){
                $ran    = rand(100,999);
                $millisec = gettimeofday()['usec'];
                $sec = date("s");
                $name   = $r->case_id."_1_".date("Y_m_d_h_i")."_".$sec."_".$millisec.".".$img->getClientOriginalExtension();
                // $destinationPath    = htdocs('ScreenRecord');
                $destinationPath = 'D:/laragon/htdocs/test';
                // dd($name, $destinationPath, $img);
                $img->move($destinationPath, $name);
            }
            // return redirect()->back();
            echo json_encode('done');
        }
    }

    function get_file_content($r){
        $name = $r->file;
        $data['data'] = view("$name")->render();
        $json_encode = json_encode($data);
        echo $json_encode;
    }

    function add_new_account($r){
        // dd($r->all());
        $data['us_check']     = $r->us_check; // 0 - in, 1 - out
        $data['us_status']    = 0;
        $data['us_prefix']    = $r->us_prefix;
        $data['us_firstname'] = $r->us_firstname;
        $data['us_lastname']  = $r->us_lastname;

        $data['us_affiliation'] = 9; // 9- อื่นๆ
        $data['us_work_year']   = 1;

        $data['us_id_number']    = $r->us_id_number;
        $data['us_email']        = $r->us_email; 
        $data['us_phone_number'] = $r->us_phone_number;


        $data['name']     = $r->email;
        $data['email']    = $r->email;
        $data['password'] = Hash::make($r->password);
        // dd($data);

        DB::table('users')->insert($data);
        return redirect()->back();
    }

    public function update_json($id, $data_to_update){
        
        $w[0] = array('sr_id', $id);
        $pg_srdicom = DB::table('pg_srdicom')->where($w)->first();
        $ori = isset($pg_srdicom->sr_json) ? json_decode($pg_srdicom->sr_json, true) : []; 
        $add = [];
        $update = [];
        if(count($ori) > 0){
            foreach($data_to_update as $key=>$val){
                // key found in ori or not found
                if(isset($ori[$key])){
                    $update[$key] = $val;
                } else {
                    $add[$key] = $val;
                }

                foreach($ori as $ori_key=>$ori_val){
                    if($ori_key){

                    }
                }
                $ori[$key] = $val;
            }
        }

        $diff = array_diff($ori, $data_to_update);
        // show updated data, added key - value, updated key - value
        dd('data ที่อัพเดทแล้ว: ', $ori, 'key ที่อัพเดท: ',$update, 'key ที่เพิ่มใหม่',$add, 'key ที่มีอยู่แล้ว (ไม่มีการอัพเดท)', $diff);
    }

    function change_bitrate($r){
        $input_path = $r->vdo_input;
        $output_path = $r->vdo_output;
        $text_path = $r->text;

        // empty text file
        file_put_contents($text_path, "");

        try{
            // set system environment variable ชี้มายังโฟล์เดอร์ที่มี ffmpeg
            // ปรับขนาดของ video ( ในที่นี้คือ 1280x720 แต่ยังไม่สามารถกำหนดขนาด bitrate ที่เจาะจงได้)
            $output = exec("ffmpeg -y -i $input_path -vf scale=1280:720 -b:v 120k $output_path -progress $text_path");
        } catch (Exception $e) {
            echo 0;
        }
    }

    function get_progress($r){
        $input_path = $r->vdo_input;
        $text_path = $r->text;

        try {
            // หา frame ทั้งหมดใน video
            $all_frame = exec("ffprobe -v error -select_streams v:0 -count_packets -show_entries stream=nb_read_packets -of csv=p=0 $input_path");
            $array = explode("\n", file_get_contents($text_path));
            $frame = '0';

            foreach ( $array as $line){
                if(str_contains($line, 'frame=')){
                    $frame = str_replace('frame=', '', $line); 
                }
            }

            $frame = intval($frame);
            $percent = ($frame / (intval($all_frame))) * 100;

            echo $percent;
        } catch(Exception $e) {
            echo 0;
        }
    }

    public function get_form(Request $r){
        // $w[0] = array('sr_id', 12); 
        // $get = DB::table('pg_srdicom')->where($w)->first();
        // $case_json = json_decode($get->sr_json, true);
        // $data['sr_data'] = $case_json['sr_data'];

        $render['header'] = view('pdf.header')->render();
        $render['footer'] = view('pdf.footer')->render();
        // $render['body']   = view('pdf.body', $data)->render();

        $json = json_encode($render, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);

        echo $json;

        // dd($json);

    }

    public function get_form_html(Request $r){
        $w[0] = array('sr_id', 12); 
        $get = DB::table('pg_srdicom')->where($w)->first();
        $case_json = json_decode($get->sr_json, true);
        $data['sr_data'] = $case_json['sr_data'];
        // dd($data);

        $render['body'] = view('pdf.body2', $data)->render();
        $json = json_encode($render, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
        echo $json;
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {  

        if($id == 'dup'){
            $test = DB::table('exam_playlist')->get();
            
            return view('test');
        } 
        else if($id == 'acc'){
            return view('account');
        } 
        else if($id == 'drawing') {
            return view('drawing1');
        } 
        else if($id == 'upload'){
            return view('upload2');
        } 
        else if ($id == 'update'){
            $w[0] = array('sr_id', 3); 
            $get = DB::table('pg_srdicom')->where($w)->first();
            $toarray = json_decode($get->sr_json, true);
            $this->update_json(2, $toarray);
        } 
        else if ($id == 'pdf'){
            // dd(phpinfo());
            $w[0] = array('sr_id', 12); 
            $get = DB::table('pg_srdicom')->where($w)->first();
            $case_json = json_decode($get->sr_json, true);
            $data['sr_data'] = $case_json['sr_data'];
            // $data = [];
            // dd($data);
            // return view('pdf.footer');
            return view('pdf2', $data);
        } 
        else if ($id == 'html2pdf'){
            return view('pdf.test');
        } 
        else if ($id == 'ffmpeg'){
            return view('ffmpeg');
        } 
        else if ($id == 'camera'){
            return view('camera');
        } 
        else if ($id == 'is_sr') {
            $sr_fpath = "D:\laragon\htdocs\\terra\\patient\\29111820220517\\1.2.840.113663.1500.1.489863433.1.1.20220517.181129.902.dcm";
            $command = "dsrdump +f +U8 +Ps $sr_fpath";
            $output = shell_exec($command);
            if($output == null){
                dd('is not sr file');
            } else {
                dd('is sr file');
            }
            // dd($output);
        }

        else if($id == 'mongo'){

            // // get / first
            // $w[] = array('car_id', '1');
            // $get = Mongo::table('cars')->where($w)->get();

            // // insert
            // $last_rec = Mongo::table('cars')->raw()->findOne([],['sort' => ['_id' => -1],'projection' => ['_id' => 1]]);
            // $last_rec  = Mongo::table('cars')->where('_id', '=' , $last_rec->_id)->first();
            // $last_id   = intval($last_rec['car_id']);

            // $i['car_id'] = strval($last_id+1);
            // $i['color']  = '1';
            // $insert = Mongo::table('cars')->insert($i);

            // // update
            // $u['color'] = '2';
            // $update = Mongo::table('cars')->where($w)->update($u);

            // dd($get, $last_id, $insert, $update);



            // $val = DB::table('tb_case')
            // ->leftjoin('patient','patient.hn','tb_case.case_hn')
            // ->leftjoin('users', 'tb_case.case_physicians01', 'users.id')
            // ->leftjoin('tb_procedure', 'tb_case.case_procedurecode','tb_procedure.procedure_code')
            // ->leftjoin('dd_gender', 'dd_gender.gender_id', 'patient.gender')
            // ->select('tb_case.*', 'users.*', 'tb_procedure.*','patient.*','dd_gender.gender_name')
            // ->where('tb_case.case_id',$id)
            // ->first();
            $id = 1;
            $tb_case = Mongo::table('tb_case')->where('case_id', strval($id))->first(); // return array
            $main = [];

            if(isset($tb_case)){
                $case_hn = isset($tb_case['case_hn']) ? $tb_case['case_hn'] : '1';
                $case_physicians01 = isset($tb_case['case_physicians01']) ? $tb_case['case_physicians01'] : '1';
                $case_procedurecode = isset($tb_case['case_procedurecode']) ? $tb_case['case_procedurecode'] : '1';

                $w[] = array('hn', strval($case_hn));
                $patient = Mongo::table('patient')->where($w)->first();
                $gender_id = isset($patient) ? $patient['gender'] : '1'; 

                $w = [];
                $w[] = array('id', strval($case_physicians01));
                $users = Mongo::table('users')->where($w)->first();

                $w = [];
                $w[] = array('gender_id', strval($gender_id));
                $dd_gender = Mongo::table('dd_gender')->where($w)->first();

                $w = [];
                $w[] = array('procedure_code', $case_procedurecode);
                $tb_procedure = Mongo::table('tb_procedure')->where($w)->first();

                $main = $this->get_data_in_array($main, $tb_case);
                $main = $this->get_data_in_array($main, $users);
                $main = $this->get_data_in_array($main, $dd_gender);
                $main = $this->get_data_in_array($main, $tb_procedure);
                $main = $this->get_data_in_array($main, $patient);
                $main = $this->change_null_string($main);

                $object = (object) $main;

                dd($object->case_id);
            }

            

            
            dd($tb_case);

            // $colors = Car::where('car_id', '1')->get();
            // dd($colors);

            // $cars = DB::connection('mongodb')->collection('cars')
            //     ->raw(function($collection) {
            //         return $collection->aggregate([
            //             [
            //                 '$lookup' => [
            //                     'from' => 'colors',
            //                     'localField' => 'car_id',
            //                     'foreignField' => '',
            //                     'as' => 'author',
            //                 ],
            //             ],
            //         ]);
            //     })
            //     ->get();
        }



        else if ($id == 'body'){
            $id = 1;

            $view['cid'] = $id;
            $view['case'] = DB::table('tb_case')
            ->leftjoin('patient','patient.hn','tb_case.case_hn')
            ->leftjoin('users', 'tb_case.case_physicians01', 'users.id')
            ->leftjoin('tb_procedure', 'tb_case.case_procedurecode','tb_procedure.procedure_code')
            ->leftjoin('dd_gender', 'dd_gender.gender_id', 'patient.gender')
            ->select('tb_case.*', 'users.*', 'tb_procedure.*','patient.*','dd_gender.gender_name')
            ->where('tb_case.case_id',$id)
            ->first();
            $view['json'] = jsonDecode($view['case']->case_json);
            $view['hospital'] = setting_type('hospital', $is_array=false);
            $view['text01'] = '';
            $view['text02'] = '';
            $view['text03'] = '';
            $view['text04'] = '';
            $view['i']      = 0;
            $view['date'] = date("dM,Y");
            $view['charts'] = array();
            if(isset($view['case']->studydate) && @$view['case']->studydate!=''){
                $carbon = new Carbon($view['case']->studydate);
                $view['date'] = $carbon->format('dM,Y');
            }

            if(isset($view['json']->charts)){
                $view['charts'] = jsonDecode($view['json']->charts);
            };


            if(isset($view['json']->photo)){
                $view['photo'] = jsonDecode($view['json']->photo);
            };

            $case_json = isset($view['case']->case_json) ? json_decode($view['case']->case_json, true) : [];
            $view['sr_data']   = $case_json['sr_data'];
            $chart_names = $view['charts'];
            $ploty       = [35, 150, 35];
            $img_arr     = [];

            // $python_path = get_python_path();
            // $python_script_path = 'D:\laragon\htdocs\endocapture5.0\public\python\graph.py';
            // for($i=0;$i<count($chart_names); $i++){
            //     // $y = $ploty[$i];
            //     $name = $chart_names[$i];
            //     $output = shell_exec("$python_path $python_script_path 17 35 $name");
            //     array_push($img_arr, $output);
            // }

            $view['charts_img'] = $img_arr;

            // $python_script_path = 'D:\laragon\htdocs\endocapture5.0\public\python\read.py';
            // $case_hn = $view['case']->case_hn;
            // $studydate = $view['case']->studydate;
            // $modality = $view['case']->modality;
            // $output = shell_exec("$python_path $python_script_path $case_hn/$studydate/$modality"); // 1/20220608/US
            // $decode = $output!=null ? json_decode($output, true) : [];
            // $view['dic'] = $decode;

            // check file exists
            $base_path = str_replace('terralink','', base_path());
            for($i=0;$i<count($view['photo']);$i++){
                $path = "$base_path/store/".$view['photo'][$i];
                if(file_exists($path) == false){
                    $view['photo'][$i] = "public/images/no_image.jpg";
                }
            }

            // ////////////////////////////////////////////////////////////////////////////////////////////
            $view['case_json'] = (isset($view['case']->case_json)) ? $view['case']->case_json : [];
            $view['doctor01']            = DB::table('tb_case as tc')->join('users as u', 'tc.case_physicians01', 'u.id')->where('tc.case_id', '=', $id)->first();
            $view['casedata']            = DB::table('tb_case')
            ->join('patient', 'tb_case.case_hn','patient.hn')
            ->join('dd_gender', 'patient.gender','dd_gender.gender_id')
            ->join('tb_procedure', 'tb_case.case_procedurecode', 'tb_procedure.procedure_code')
            ->where('case_id', $id)
            ->first();

            $view['pdfshow']             = jsonDecode($view['casedata']->procedure_pdfshow);
            $view['pdfshownew']          = jsonDecode($view['casedata']->procedure_pdfshownew);
            $view['json']                = jsonDecode($view['casedata']->case_json);
            $view['between_line']        = '8px';

            $view    = $this->staffname($view);
            $view    = $this->totaltime($view);
            $view    = $this->scopeall($view);

            $apppoint                   = explode(" ",$view['case']->case_dateappointment);
            $view['folderdate']          = $apppoint[0];

            // render view header, body, footer as of right now then store in php variable pass to javascript



            return view('pdf.body3', $view);
            }

            $w[0] = array('sr_id', $id);
            $get = DB::table('pg_srdicom')->where($w)->first();
            $toarray = json_decode($get->sr_json, true);

            $get = DB::table('pg_srdicom')->where('sr_id', 1)->first();
            $toarray2 = json_decode($get->sr_json, true);
            dd('data เดิม: ', $toarray,'data ใหม่: ', $toarray2);

    }

    public function get_data_in_array($first_array, $second_array){
        if(isset($second_array)){
            foreach ($second_array as $key => $val) {
                $first_array[$key] = $val;
            }
        }
        return $first_array;
    }

    public function change_null_string($array){
        if(isset($array)){
            foreach($array as $key => $val){
                if($val == 'NULL'){
                    $array[$key] = null;
                }
            }
        }
        return $array;
    }

    

    public function totaltime($val){
        $val['totaltime'] = ' - ';
        if(isset($val['json']->time_start) && isset($val['json']->time_finish)){
            $val['totaltime'] = $val['json']->time_start." - ".$val['json']->time_finish;
            $start      = new Carbon($val['json']->time_start);
            $end        = new Carbon($val['json']->time_finish);
            $toltal     = Carbon::parse($start)->diffInMinutes($end);
            $val['totaltime'] .= " [".$toltal."] นาที";
        }
        return $val;
    }

    public function checkUSERNULL($uid){
        $user   = DB::table('users')->where('id',$uid)->first();
        $str    = "";
        if($user!=null){
            $str.= $user->user_prefix;
            $str.= $user->user_firstname." ";
            $str.= $user->user_lastname;
        }
        return $str;
    }

    public function scopeall($val){
        $val['scopeall'] = array();
        if(isset($val['json']->endoscope)){
            foreach($val['json']->endoscope as $endoscope){
                $tb_scope = DB::table('tb_scope')->where('scope_id',$endoscope)->first();
                if(isset($tb_scope->scope_name)){
                    $val['scopeall'][]=$tb_scope->scope_name;
                }
            }
        }
        return $val;
    }

    public function staffname($val){
        $pati = $val['casedata']->firstname.$val['casedata']->lastname;
        if (!preg_match('/[^A-Za-z0-9]/', $pati)){
            if(@$val['doctor01']->name!=""){
                $val['doctor'][1]   = @$val['json']->doctorname."";
            }else{
                $val['doctor'][1]   = @$val['json']->doctorname."";
            }
        }else{
            $val['doctor'][1]   = @$val['json']->doctorname."";
        }
        $val['doctor'][2]       = $this->checkUSERNULL(@$val['json']->physicians02);
        $val['doctor'][3]       = $this->checkUSERNULL(@$val['json']->physicians03);
        $val['doctor'][4]       = $this->checkUSERNULL(@$val['json']->physicians04);
        $val['nurse'][1]        = $this->checkUSERNULL(@$val['json']->nurse01);
        $val['nurse'][2]        = $this->checkUSERNULL(@$val['json']->nurse02);
        $val['nurse'][3]        = $this->checkUSERNULL(@$val['json']->nurse03);
        $val['nurse'][4]        = $this->checkUSERNULL(@$val['json']->nurse04);
        $val['nurse_anes'][1]   = $this->checkUSERNULL(@$val['json']->nurse_anes01);
        $val['nurse_anes'][2]   = $this->checkUSERNULL(@$val['json']->nurse_anes02);
        return $val;
    }

    

    /**
     * Show the form for editing the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function edit($id)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, $id)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        //
    }
}
