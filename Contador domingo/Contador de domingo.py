def es_bisiesto(anio):
    # Divisible por 4, pero no por 100 a menos que sea divisible por 400
    if anio % 400 == 0:
        return True
    if anio % 100 == 0:
        return False
    return anio % 4 == 0

# Días de cada mes (enero a diciembre)
dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 0 = Lunes, 1 = Martes, ..., 6 = Domingo
# El 1 de enero de 1900 fue lunes (0)
dia_semana = 0
domingos = 0

for anio in range(1900, 2001):
    for mes in range(12):
        # Contamos solo desde 1901 hasta 2000
        if anio >= 1901 and dia_semana == 6:
            domingos += 1
        
        # Calculamos los días del mes actual
        dias = dias_mes[mes]
        if mes == 1 and es_bisiesto(anio): # Febrero en año bisiesto
            dias = 29
            
        # Avanzamos al primer día del siguiente mes
        dia_semana = (dia_semana + dias) % 7

print("Total de domingos:", domingos)
