#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"


def ej1():
    # Ejercicios de práctica numérica

    # Comparadores
    # Ingrese dos números cualesquiera y realice las siguientes
    # comparaciones entre ellos

    numero_1 = 10
    numero_2 = 5

    # Compare cual de los dos números es mayor
    # Imprima en pantalla según corresponda

    if numero_1 > numero_2:
        print('"numero_1 =', numero_1, '" es mayor a "numero_2 =', numero_2, '"')

    # Verifique si el numero_1 positivo, negativo o cero
    # Imprima el resultado en cada caso

    if numero_1 > 0:
        print(numero_1, 'es positivo')
    elif numero_1 < 0:
        print(numero_1, 'es negativo')
    elif numero_1 == 0:
        print(numero_1, 'es igual a cero')

    # Verifique si el numero_1 es mayor a 0 y menor a 100
    # Imprima en pantalla si se cumple o no la condición

    if (numero_1 > 0 and numero_1 < 100):
        print('El numero {} es positivo'.format(numero_1))
    else:
        print('El numero {} es negativo o cero'.format(numero_1))

    # Verifique si el numero_1 es menor a 10 o el numero_2
    # es mayor a -2
    # Imprima en pantalla si se cumple o no la condición

    if (numero_1 < 10 or numero_2 > -2):
        print('Se cumple con la condicion') 
    else:
        print('No se cumple la condicion')

    print('grande bocaaaaa agarrate')
                                                                     

def ej2():
    # Ejemplos variables de texto

    # Comparadores
    # Ingrese dos palabras cualesquiera y realice las sigueintes
    # comparaciones entre ellas
    texto_1 = 'ovni'
    texto_2 = 'antena'

    # Compare cual de las dos palabras es mayor (alfabéticamente)
    # Imprima en pantalla según corresponda

    if texto_1 > texto_2:
        print('{} es mayor que {}'.format(texto_1, texto_2))
    elif texto_1 < texto_2:
        print('{} es mayor que {}'.format(texto_2, texto_1))
    else:
        print('{} es igual que {}'.format(texto_1, texto_2))
    
    # Compare cual de las dos palabras tiene mayor
    # cantidad de letras
    # Imprima en pantalla según corresponda

    if (len(texto_1) > len(texto_2)):
        print('{} es mayor que {}'.format(texto_1, texto_2))
    elif (len(texto_2) > len(texto_1)):
        print('{} es mayor que {}'.format(texto_2, texto_1))

    else:
        print('{} es igual a {}'.format(texto_1, texto_2))

    # Verifique si la primera letra de la primera palabra
    # es mayor a la primera letra de la segunda palabra
    # Imprima en pantalla según corresponda 
    caracter_ini_1 = texto_1[0]
    caracter_ini_2 = texto_2[0]

    if (caracter_ini_1 > caracter_ini_2):
        print('{} es mayor que {}'.format(caracter_ini_1, caracter_ini_2)
    elif (caracter_ini_2 > caracter_ini_1):
        print('{} es mayor que {}'.format(caracter_ini_2, caracter_ini_1)

    else:
        print('{} es igual que {}'.format(caracter_ini_1, caracter_ini_2)

    # Copia de la variable texto_1
    copia_texto_1 = texto_1  

    # Verifique que copia_texto_1 es igual a texto_1
    # Imprima en pantalla según corresponda
    if copia_texto_1 == texto_1:
        print(copia_texto_1, 'es igual a', texto_1)

    # Verifique que copia_texto_1 es distinta a texto_2
    # Imprima en pantalla según corresponda
    if copia_texto_1 != texto_2:
        print(copia_texto_1,'es distinto a', texto_2)

def ej3():
    # Ejercicios de práctica numérica
    # Condicionales anidados
    numero_1 = 7
    numero_2 = -2

    # Verifique si el numero_1 es mayor a 5
    #   --> En caso afirmativo, verifique si el numero_2
    #       es positivo
    #       --> En caso afirmativo imprima en pantalla "Resp=1"
    #       --> En caso negativo imprima en pantalla   "Resp=2"
    
    if (numero_1 > 5 and numero_2 > 0):
        print("Resp=1")
    else:
        print("Resp=2")

    #  --> En caso negativo (numero_1 no es mayor a 5)
    #      verifique si el numero_2 es mayor a 5
    #       --> En caso afirmativo imprima en pantalla "Resp=3"
    #       --> En caso negativo imprima en pantalla "Resp=4"

    if not (numero_1 > 5):
    elif (numero_2 > 5):
        print("Resp=3")
    else:
        print("Resp=4")

    # Verifique la calificación de un estudiante según su
    # puntaje en un examen
    puntaje = 70

    # Si el puntaje es mayor igual a 90 --> imprimir A
    # Si el puntaje es mayor igual a 80 --> imprimir B
    # Si el puntaje es mayor igual a 70 --> imprimir C
    # Si el puntaje es mayor igual a 60 --> imprimir D
    # Si el puntaje es manor a  60      --> imprimir F

    # Debe imprimir en pantalla la calificacion
    # Utilizar "if" anidados

    if puntaje >= 90:
        print('A')
    elif puntaje >= 80:
        print('B')
    elif puntaje >= 70:
        print('C')
    elif puntaje >= 60:
        print('D')
    elif puntaje < 60:
        print('F')

def ej4():
    # Ejemplos variables de texto
    texto_1 = 'Boca'
    texto_2 = 'Juniors'

    # Verifique cual cual de los dos textos es mayor alfabéticamente
    # Imprima en pantalla según corresponda

    if texto_1 > texto_2:
        print('{} es mayor que {}'.format(texto_1, texto_2))
    else:
        print('{} es mayor que {}'.format(texto_2, texto_1))

    # Transforma esas variables tipo texto y almacénalas
    # en nuevas variables númericas (int)
    # Repita el proceso, ¿Cuál de las nuevas variables es mayor?
    # Imprima en pantalla según corresponda
    texto_1_len = len(texto_1)
    texto_2_len = len(texto_2)

    if texto_1_len > texto_2_len:
        print('{} es mayor que {}'.format(texto_1_len, texto_2_len))
    else:
        print('{} es mayor que {}'.format(texto_2_len, texto_1_len))


    # Para pensar!
    # ¿Por qué cree que texto_2 es mayor a texto_1?
    # En mi caso creo que se da por las palabras que elegí. 
    # Siendo números tiene sentido, pero son caracteres, texto,
    # aún así el operador arroja el mismo resultado que con las
    # variables numéricas, cierto? ¿Por qué creen que es así?
    # En mi caso da la casualidad que la segunda es mayor porque 
    # tiene mas letras y al trasformarse en numero sigue siendo
    # mayor tanto por el valor numerico como por el orden en el 
    # abecedario.
    # Esta pregunta estará repetida en el Campus para que puedan
    # responder.
    # NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
