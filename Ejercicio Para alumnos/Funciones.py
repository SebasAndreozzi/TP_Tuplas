from math import *

#region Calculos

def calcular_area_rectangulo(base:float, altura:float) -> float:
    result = base * altura
    result = round(result, 2)

    return result

def calcular_perimetro_rectangulo(base:float, altura:float) -> float:
    result = 2*base + 2*altura
    result = round(result, 2)
    
    return result

def calcular_area_circulo(radio:float) -> float:
    result = pi * (radio ** 2)
    result = round(result, 2)
    return result

def calcular_perimetro_circulo(radio:float) -> float:
    result = pi * (radio * 2)
    result = round(result, 2)

    return result

def calcular_area_triangulo_rectangulo(base:float, altura:float) -> float:
    result = (base * altura)/2
    result = round(result, 2)

    return result

def calcular_perimetro_triangulo_rectangulo(base:float, altura:float) -> float:
    hipotenusa = sqrt(base ** 2 + altura ** 2)

    result = base + altura + hipotenusa
    result = round(result, 2)

    return result
#endregion

print(calcular_area_circulo(3))
    
