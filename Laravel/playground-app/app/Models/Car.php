<?php

namespace App\Models;

// use Illuminate\Database\Eloquent\Model;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Jenssegers\Mongodb\Eloquent\Model;

class Car extends Model
{
    use HasFactory;
    protected $connection = 'mongodb';
    protected $collection = 'cars';
    
    protected $fillable = [
        'car_id', 'color'
    ];

    // public function color() {
    //     return $this->hasOne(Color::class);
    // }
}