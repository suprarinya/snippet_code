<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Jenssegers\Mongodb\Eloquent\Model as Eloquent;

class Users extends Eloquent
{
    use HasFactory;
    protected $connection = 'mongodb';
    protected $collection = 'users'; 
    
    // Define your fields in the collection
    protected $fillable = [
        'user_id', 
        'email', 
        'password', 
        'role' , 
        'name' , 
        'contact_number' , 
        'created_at', 
        'updated_at'
    ];

    public static function addUser($arr){
        $user = new static();
        $user->fill($arr);
        $user->save();
        return $user;
    }

    public static function findUser($email) {
        return static::where('email', $email)->first();
    }


}
