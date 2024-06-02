import Validate as validate
from listas_generales import print_list

def get_int(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int) -> int|None:
    
    number = int(input(f"{mensaje}"))

    for i in range(0, reintentos+1):
        
        if validate.validate_number(number, minimo, maximo):
            return number

        elif i+1 == reintentos:
            return None
        else:
            number = int(input(f"{mensaje_error}"))

def get_float(mensaje:str, mensaje_error:str, minimo:float, maximo:float, reintentos:int) -> float|None:
    
    number = float(input(f"{mensaje}"))

    for i in range(0, reintentos+1):
        
        if validate.validate_number(number, minimo, maximo):
            return number

        elif i+1 == reintentos:
            return None
        else:
            number = float(input(f"{mensaje_error}"))

def get_string(mensaje:str, mensaje_error:str, longitud:int, reintentos:int) -> str|None:

    string = input(f"{mensaje}")

    for i in range(0, reintentos+1):
    
        if validate.validate_length(string, longitud):
            return string
        
        elif i+1 == reintentos:
            return None
        
        else:
            string = input(f"{mensaje_error}")

def get_dimansion(reintentos:int) -> list:
    base = get_float("Ingrese la longitud de la base en cm: ", "Ingrese la longitud de la base en cm (Debe estar entre 0.01 y 1000): ",0.01, 1000, 3)

    altura = get_float("Ingrese la longitud de la altura en cm: ", "Ingrese la longitud de la altura en cm (Debe estar entre 0.01 y 850): ",0.01, 850, 3)

    result = [base, altura]

    return result

def get_dimansion_circle(reintentos:int) -> list:
    radio = get_float("Ingrese la longitud del radio en cm: ", "Ingrese la longitud del radio en cm (Debe estar entre 0.01 y 500): ",0.01, 500, 3)

    result = [radio]
    return result
    
def get_color(colors:dict,reintentos:int) -> tuple|None:
    color_list = list(colors)
    print_list(color_list)

    entry = get_int("Elija un color: ","Elija un color (las únicas opciones son las que figuran en pantalla. Ingrese únicamente el número que correstonda al color): ", 1, len(colors), reintentos)

    if entry == None:
        result = entry
    else:
        result = colors[color_list[entry-1]]

    return result