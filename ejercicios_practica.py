#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"


def ej1():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
    '''
    numero_1 = {}
    numero_2 = {}

 if (numero_1 > 0) and (numero_2 > 0):
        resta = (numero_1 - numero_2) > 0:
        print('La resta entre {} y {} es {}'.format(numero_1, numero_2, positivo)
  elif (numero_1 > 0) and (numero_2 > 0):
        resta = (numero_1 - numero_2) < 0:
        print('La resta entre {} y {} es {}'.format(numero_1, numero_2, negativa)
  elif (numero_1 > 0) and (numero_2 > 0):
        resta = (numero_1 - numero_2) == 0:
        print('La resta entre {} y {} es {}'.format(numero_1, numero_2, cero)

def ej2():
    print('Ejercicios de práctica con números')

  '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
  '''
    numero_1 = {}
    numero_2 = {}
    numero_3 = {}

    if (numero_1 % 2) == 0:
        print('"numero_1" es par')
    elif (numero_1 % 2) != 0:
        print('"numero_1" es impar')

    if (numero_2 % 2) == 0:
        print('"numero_2" es par')
    elif (numero_2 % 2) != 0:
        print('"numero_2" es impar')
      
    if (numero_3 % 2) == 0:
        print('"numero_3" es par')
    elif (numero_3 % 2) != 0:
        print('"numero_3" es impar')

def ej3():
    print('Ejercicios de práctica con números')

    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    '''
numero_1 = {} , numero_2 = {}
Suma(numero_1 + numero_2), Resta(numero_1 - numero_2), Multiplicación(numero_1 * numero_2), 
División(numero_1 / numero_2), Potencia(numero_1 ** numero_2)

if(numero_1 + numero_2) == 0
    print(Suma)

elif(numero_1 - numero_2) == 0
    print(Resta)

elif(numero_1 * numero_2) == 0
    print(Multiplicación)

elif(numero_1 / numero_2) == 0
    print(División)

elif(numero_1 ** numero_2) == 0
    print(Potencia)


def ej4():
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor
  '''

  texto_1 = str(input(''))
  texto_2 = str(input(''))
  texto_3 = str(input(''))

opcion_1 = (texto_1 > texto_2 > texto_3) or 
opcion_2 = (len(texto_1 > texto_2 > texto_3) < 50)):

if (opcion_1):
    print('{} {} y {} estan en orden alfabetico'.format(texto_1, texto_2, texto_3))

elif (opcion_2):
    print('{} {} y {} estan en orden alfanumerico'.format(texto_1, texto_2, texto_3))


def ej5():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado
    '''

    temperatura_1 = {}
    temperatura_2 = {}
    temperatura_3 = {}
    listado = (temperatura_1 + temperatura_2 + temperatura_3)

    max([temperatura_1], [temperatura_2], [temperatura_3])
    min([temperatura_1], [temperatura_2], [temperatura_3])
    avg = (sum(listado)/len(listado)

    if(max):
      print("'la temperatura maxima es' {}".format(max))

    if(min):
      print("'la temperatura minima es' {}".format(min))

    if(avg):
      print("'la temperatura promedio es' {}".formata(avg)

if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
