<?php

function conectar(){
    $server = 'localhost';
    $bd = 'ejercicio5';
    $user = 'root';
    $pass = '';
    $con=mysqli_connect($server,$user,$pass,$bd) or die ("Error al conectar a la base de datos".mysql_error());
    
    return $con;
}   

?>