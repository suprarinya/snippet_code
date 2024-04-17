<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class Test3Controller extends Controller
{
    public function index(){
        return json_encode('index');
        // echo 'index'; 
        // $request = $r;
        // if ($request->hasFile('image')) {
        //     $image = $request->file('image');
        
        //     $fileName = $image->getClientOriginalName();
        //     $destinationPath = base_path() . '/public/posttest/' . $fileName;
        //     $image->move($destinationPath, $fileName);
        
        //     $attributes['image'] = $fileName;
        // }
    }

    public function store(Request $r){
        $this->store_file($r);
        // return json_encode('store');
    }

    public function show(Request $r, $id){
        // if($id == 'store'){
        //     $this->store_file($r);
        // }
    }

    public function store_file($r){
        // dd($r->all());
        // return json_encode('in store');
        $request = $r;
        if ($request->hasFile('file')) {
            $file = $request->file('file');
            $fileName = $file->getClientOriginalName();
            // dd($file, $fileName);

            $destinationPath = base_path() . '/public/posttest/';
            $file->move($destinationPath, $fileName);
        
            $attributes['file'] = $fileName;
            return json_encode('success');


        } else {
            return json_encode('fail');
            

        }
    }
}
