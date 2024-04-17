<?php

function jsonDecode($value)
    {
        $value = json_decode($value);
        if ($value == null) {
            $value = array("");
        }
        return $value;
    }

function setting_type($type, $is_array=false){
    $root_path = $_SERVER['DOCUMENT_ROOT'];
    $str    = ($type!='hospital') ? file_get_contents($root_path."/config/project/$type.txt") : file_get_contents($root_path."/setting/$type.txt");
    $json   = jsonDecode($str, $is_array);
    return $json;
    
}

function age_form_bd($birthdate)
{
    $age = "";
    if(isset($birthdate)){
        if($birthdate!="")
        {
            $date   = new DateTime($birthdate);
            $now    = new DateTime();
            $interval = $now->diff($date);
            $age    = $interval->y;
        }
    }
    return $age;
}

?>