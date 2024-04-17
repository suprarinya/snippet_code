<?php

use App\Http\Controllers\Test2Controller;
// use App\Http\Controllers\Test3Controller;
use App\Http\Controllers\TestController;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

// Route::get('/', function () {
//     return view('welcome');
// });

// $resources['test']            = TestController::class;

// Route::resources($resources);
Route::get('/', function () {
    return view('welcome');
});

$resources['test']            = TestController::class;
$resources['test2']           = Test2Controller::class;
// $resources['test3']           = Test3Controller::class;


Route::resources($resources);


