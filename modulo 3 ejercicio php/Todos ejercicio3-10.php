<?php
# Ejercicio 3
$numero5 = 7;
$intento = 0;
$contador = 0;

while ($intento != $numero5) {
    $intento++;
    $contador++;
    echo "Intento $contador -> $intento\n";
}

echo "Adivinaste el numero $numero5 en $contador intentos\n";


# Ejercicio 4
$suma = 0;

for ($p = 1; $p <= 100; $p++) {
    if ($p % 2 != 0) {
        $suma += $;
    }
}

echo "La suma de los impares es $suma\n";


#  Ejercicio 5
$edad = 20;

if ($edad >= 18 && $edad <= 65) {
    echo "Puede obtener licencia\n";
} else {
    echo "No puede obtener licencia\n";
}


#  Ejercicio 6
for ($f = 0; $f < 5; $f++) {
    for ($j = 0; $j < 5; $j++) {
        echo "#";
    }
    echo "\n";
}


#  Ejercicio 7
$numero = -3;

if ($numero > 0) {
    echo "Positivo\n";
} else if ($numero < 0) {
    echo "Negativo\n";
} else {
    echo "Cero\n";
}


# Ejercicio 8
for ($a = 1; $a <= 30; $a++) {
    if ($a % 3 == 0 && $a % 5 == 0) {
        echo "MarTierra\n";
    } else if ($a % 3 == 0) {
        echo "Mar\n";
    } else if ($a % 5 == 0) {
        echo "Tiierra\n";
    } else {
        echo "$a\n";
    }
}


# Ejercicio 9
$temperatura = 22;

if ($temperatura < 10) {
    echo "Fraa\n";
} else if ($temperatura >= 10 && $temperatura <= 25) {
    echo "Templada\n";
} else {
    echo "Calurosaa\n";
}


# Ejercicio 10
for ($t = 10; $t >= 1; $t--) {
    echo "$t\n";
}

echo "¡Feliz Año Nuevo! 🎉\n";

?>