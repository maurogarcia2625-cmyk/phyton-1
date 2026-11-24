# Contador de Domingos (SigloXX)

Un contador que cuenta los dias que cumplan los siguientes requisitos;

Dias que sean Domingo y que sean el primero de cada mes.
Durante los años del siglo XX.
Cuida los años bisiestos para que el calculo coencida.
Resultado que debe de dar 171.

Caracteristicas:

Usa la funcion "es_bisiesto()" para saber si febrero tiene 28 o 29 dias.
Empieza desde el 1ro de Enero de 1900 que fue Lunes como punto de partida.
Recorre cada mes hasta el año 2000 usando el operador módulo (`% 7`) para calcular los días de la semana y suma `1` cada vez que el primer día del mes es domingo.