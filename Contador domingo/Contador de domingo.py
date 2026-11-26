def es_bisiesto(anio):
    if anio % 400 == 0:
        return True
    if anio % 100 == 0:
        return False
    return anio % 4 == 0

dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dia_semana = 0
domingos = 0

for anio in range(1900, 2001):
    for mes in range(12):
        if anio >= 1901 and dia_semana == 6:
            domingos += 1
        
        dias = dias_mes[mes]
        if mes == 1 and es_bisiesto(anio): # Febrero en año bisiesto
            dias = 29
            
        dia_semana = (dia_semana + dias) % 7

print("Total de domingos:", domingos)
