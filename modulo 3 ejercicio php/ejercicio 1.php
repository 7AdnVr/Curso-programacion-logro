<?php

$pares = 0;
$impares = 0;

for ($numero = 1; $numero <= 50; $numero++) {
    if ($numero % 2 == 0) {
        $pares++;
    } else {
        $impares++;
    }
}

echo "Cantidad de números pares -> " . $pares ;
echo "\nCantidad de números impares -> " . $impares;
echo "\nEn el rango del 1 al 50"
?>
