from Grafico import *
from os import *
from Input import *

choise_message = "Elija una opción: "

first_menu_message_1 = "1. Seleccionar figura y cargar valores"
first_menu_message_2 = "2. Visualizar resultados"
first_menu_message_3 = "3. Salir"
first_menu_choise_error_message = "Elija una opción (Ingrese únicamente el número de la opción que desea elegir): "

first_menu_message_final = f"{first_menu_message_1}\n{first_menu_message_2}\n{first_menu_message_3}\n{choise_message}"

second_menu_message_a = "a. Círculo"
second_menu_message_b = "b. Rectángulo"
second_menu_message_c = "c. Triángulo"
second_menu_message_d = "d. Volver al menu anterior"
second_menu_choise_error_message = "Elija una opción (Ingrese únicamente la letra en minúscula de la opción que desea elegir): "

second_menu_message_final = f"{second_menu_message_a}\n{second_menu_message_b}\n{second_menu_message_c}\n{second_menu_message_d}\n{choise_message}"


def inicio_programa():
    system("cls")

    while True:
        opcion = get_int(first_menu_message_final, first_menu_choise_error_message, 1, 3, 3)

        if opcion == None:
            print("Agotó el número de reintentos. Vuelva a iniciar")
            break
        else:

            match opcion:
                case 1:
                    system("cls")
                    print("¿Qué tipo de figura desea representar?")
                    que_figura = get_string(second_menu_message_final, second_menu_choise_error_message, 1, 3)

                    while 97 >  ord(que_figura) or ord(que_figura) > 100 or que_figura == None: 
                        que_figura = get_string(second_menu_message_final, second_menu_choise_error_message, 1, 3)

                    if que_figura == None:
                        print("Agotó el número de reintentos. Vuelva a iniciar")
                     
                    match que_figura:
                        case "a":
                            system("cls")
                            entrada_dimensiones = get_dimansion_circle(3)
                            entrada_color = get_color(colores, 3)
                            
                            try:
                                figura = {
                                    "tipo" : "Circulo",
                                    "color" : entrada_color,
                                    "posicion"  :  (500, 425),
                                    "dimensiones" : [entrada_dimensiones[0]]}
                            except:
                                print("Agotó el número de reintentos. Vuelva a iniciar")
                                
                        case "b":
                            system("cls")
                            entrada_dimensiones = get_dimansion(3)
                            entrada_color = get_color(colores, 3)
                            
                            figura = {
                                "tipo" : "Rectangulo",
                                "color" : entrada_color,
                                "posicion"  :  (0, 0),
                                "dimensiones" : [entrada_dimensiones[0], entrada_dimensiones[1]]}
                            
                        case "c":
                            system("cls")
                            entrada_dimensiones = get_dimansion(3)
                            entrada_color = get_color(colores, 3)
                            
                            figura = {
                                "tipo" : "Triangulo",
                                "color" : entrada_color,
                                "posicion"  :  (0, 0),
                                "dimensiones" : [entrada_dimensiones[0], entrada_dimensiones[1]]}
                        
                        case _:
                            pass

                case 2:
                    graficar(figura)
                case 3:
                    print("Gracias por usar nuestro programa")
                    break 
            
            system("cls")   

inicio_programa()