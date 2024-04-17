<?php

namespace App\Models;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Support\Facades\DB;

class Mongo extends Model
{
    use HasFactory;
    public static function table($name){
        return DB::connection("mongodb")->collection($name);
    }

}
