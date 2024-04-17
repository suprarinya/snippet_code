<?php

namespace App\Http\Controllers;

use Exception;
use Illuminate\Http\Request;
use mysqli;
use Illuminate\Support\Facades\DB;
use Maatwebsite\Excel\Facades\Excel;
use Illuminate\Support\Facades\Input;

class Test2Controller extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {

        $view['tb_case'] = DB::table('tb_case')->get();
        $view['head'] = $this->get_head($view['tb_case']);
        return view('test2.table', $view);
    }

    public function get_head($tb_case=[]){
        $head = [];
        foreach ($tb_case as $case) {
            foreach (json_decode($case->case_json) as $key => $data) {
                if(!in_array($key, $head)){
                    $head[] = $key; 
                }
            }
        }
        return $head;
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
            if($r->event=='dump_mongo')                {return $this->dump_mongo($r);}
            if($r->event=='upload_file')                {return $this->upload_file($r);}

            if($r->event=='test')                {return $this->test($r);}

        }
    }

    public function test(Request $r){
        dd('a');
    }

    public function dump_mongo($r){
        // dd($r->all());
        $python_path = $r->python_path;
        $python_script_path = $r->script_path;

        $db_host = $r->db_host;
        $db_name = $r->db_name;
        $mongodb_host = $r->mongodb_host;
        $mongodb_name = $r->mongodb_name;

        try {
            $output = shell_exec("$python_path $python_script_path $db_host $db_name $mongodb_host $mongodb_name");
        } catch(Exception $e) {
            $output = 0;
        }
        return redirect()->back()->with('status', $output);
    }

    public function upload_file($r){
        return 'success';
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        if($id == 'mongo'){
            return view('test2.mongo');
        } else if ($id == 'rstp') {
            return view('test2.webrtc');
        } else if ($id == 'pdf') {
            return view('test2.pdf');
        } else if ($id == 'sort' ){
            return view('test2.sort');
        } else if ($id == 'ocr'){
            return view('test2.ocr');
        } else if ($id == 'canva'){
            return view('test2.dragacanvas');
        } else if($id == 'excel'){
            return view('test2.excel');
        } else if($id == 'upload'){
            return view('test2.upload');
        } else if($id == 'photoviewer'){
            return view('test2.photoviewer');
        } else if($id == 'endosmart'){
            $this->endosmart();
        }
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

    public function endosmart(){
        // if($id=='endosmart'){
        $key_order = ['date_operation', 'procedure', 'hn', 'unknown'];
        $mainarr = [];
        $init_path = htdocs('endosmart_data');
        $folder = $this->get_data_inside_path($init_path);
        $data   = $this->create_data_array();
        foreach ($folder as $f) {
            $path        = $init_path."/$f";
            $is_folder   = $this->check_folder($path);
            $folder      = $this->get_data_inside_path($path);
            if($is_folder){
                foreach ($folder as $f) {
                    $index     = 0;
                    $path      = $path."/$f";
                    $is_folder = $this->check_folder($path);
                    $folder    = $this->get_data_inside_path($path);
                    if($is_folder){
                        $data[$key_order[$index]] = $f;
                        foreach ($folder as $f) {
                            $index     = 1;
                            $path      = $path."/$f";
                            $is_folder = $this->check_folder($path);
                            $folder    = $this->get_data_inside_path($path);
                            if($is_folder){
                                $data[$key_order[$index]] = $f;
                                foreach ($folder as $f) {
                                    $index     = 2;
                                    $path      = $path."/$f";
                                    $is_folder = $this->check_folder($path);
                                    $folder    = $this->get_data_inside_path($path);
                                    if($is_folder){
                                    $data[$key_order[$index]] = $f;
                                        foreach($folder as $f){
                                            $index     = 3;
                                            $path      = $path."/$f";
                                            $is_folder = $this->check_folder($path);
                                            $folder    = $this->get_data_inside_path($path);
                                            if($is_folder){
                                                $data[$key_order[$index]] = $f;
                                                foreach ($folder as $f) {
                                                    $path      = $path."/$f";
                                                    $is_folder = $this->check_folder($path);
                                                    $folder    = $this->get_data_inside_path($path);
                                                    if($is_folder){
                                                        // dd($path);
                                                    } else {
                                                        $is_file = $this->check_file($path);
                                                        if($is_file){
                                                            // in here so if found file -> save to array
                                                            $data = $this->check_image($f, $data);
                                                        } 
                                                    }
                                                    $path      = $this->remove_last_slash($path);
                                                }
                                                // save to database
                                                $data          = $this->get_path_string($data, $init_path);
                                                unset($data['unknown']);
                                                $mainarr[]     = $data;
                                                $checkdb       = $this->check_have_in_db($data['url']);
                                                if($checkdb){
                                                    Mongo::table('endosmart_data')->insert($data);
                                                }
                                                $data['image'] = [];
                                                $data['pdf']   = [];
                                            } else {}
                                            $path      = $this->remove_last_slash($path);
                                        }
                                    } else {}
                                    $path      = $this->remove_last_slash($path);
                                }
                            } else {}
                            $path      = $this->remove_last_slash($path);
                        }
                    }
                    $path      = $this->remove_last_slash($path);
                }
            }
        }
        dd($init_path, $mainarr);
        // }
    }

    //
    function check_have_in_db($path){
        $status = true;
        $endosmart_data = Mongo::table('endosmart_data')->get();
        foreach ($endosmart_data as $data) {
            $data =  (object) $data;
            $url  = isset($data->url) ? $data->url : '';
            if($path == $url){
                $status = false;
            }
        }
        return $status;
    }

    function create_data_array(){
        $data['date_operation'] = '';
        $data['procedure']      = '';
        $data['hn']             = '';
        $data['pdf']            = [];
        $data['image']          = [];
        $data['patientname']    = '';
        $data['pathfolder']     = '';
        $data['url']            = '';
        return $data;
    }

    function get_data_inside_path($path){
        $in_path = [];
        try {
            $in_path = scandir($path);
            $in_path = array_values(array_diff($in_path, array('.', '..')));
        } catch (Exception $e) {}
        return $in_path;
    }

    function remove_last_slash($str){
        $str_arr = explode("/", $str);
        array_pop($str_arr);
        $str = join("/", $str_arr);
        return $str;
    }

    function check_folder($path){
        $status = false;
        try{
            if(is_dir($path)){
                $status = true;
            }
        } catch (Exception $e) {}
        return $status;
    }

    function check_file($path){
        $status = false;
        try{
            if(is_file($path)){
                $ext = pathinfo($path)['extension'];
                if($ext == 'jpg' || $ext == 'png' || $ext == 'jpeg'){
                    $status = true;
                }
            }
        } catch(Exception $e){}
        return $status;
    }

    function check_image($filename, $data){
        if(str_contains($filename, '-') && strlen($filename) > 30){
            $data['pdf'][] = $filename;
        } else {
            $data['image'][] = $filename;
        }
        return $data;
    }

    function get_path_string($data, $init_path, $main_folder="endosmart_data"){
        $month_year = '';

        if(isset($data['date_operation'])){
            $exp = explode('-', $data['date_operation']);
            $month = isset($exp[1]) ? $exp[1] : '';
            $year = isset($exp[2]) ? $exp[2] : '';
            $month_year = "$month-$year";
        }

        $data['patientname'] = '';
        $data['pathfolder']  = $init_path."/$month_year"."/".$data['date_operation']."/".$data['procedure']."/".$data['hn']."/".$data['unknown'];
        $data['url']  = $main_folder."/$month_year//".$data['date_operation']."/".$data['procedure']."/".$data['hn']."/".$data['unknown'];

        return $data;
    }
}
