<?php
# Ejercicico N.5 para hacer una consulta en Php por Michael Pachón

#conexion con la base de datos
include("conexion.php");

$con=conectar();

#Se selecciona la tabla la cual se quiere realizar la consulta
$sql = "SELECT Nombre FROM Estudiantes WHERE Edad > 18";

#Se ejecuta
$result = $con->query($sql);

#Verifica los resultados 
if ($result->num_rows > 0) {
    #Imprimir los resultados
    while ($row = $result->fetch_assoc()) {
        echo $row["Nombre"] . "<br>";
    }
} else {
    echo "No se encontraron estudiantes mayores de 18 años.";
}

?>
