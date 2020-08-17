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
    print('ingrese dos numeros')
    numero_1 = str(input())
    numero_2 = str(input())
    resta = (numero_1 - numero_2)

    if (resta > 0):
        print('La resta entre {} y {} es {}'.format(numero_1, numero_2, positivo)
    elif (resta < 0):
        print('La resta entre {} y {} es {}'.format(numero_1, numero_2, negativa)

    else:
        print('La resta entre {} y {} es {}'.format(numero_1, numero_2, cero)

def ej2():
    print('Ejercicios de práctica con números')

  '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
  '''
    print('ingrese tres numeros enteros')
    numero_1 = str(input())
    numero_2 = str(input())
    numero_3 = str(input())

    if (numero_1 % 2) == 0:
        print(numero_1, 'es par')
    else: 
        print(numero_1, 'es impar')

    if (numero_2 % 2) == 0:
        print(numero_2, 'es par')
    else:
        print(numero_2, 'es impar')
      
    if (numero_3 % 2) == 0:
        print(numero_3, 'es par')
    elif:
        print(numero_3, 'es impar')

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
print('ingrese dos numeros')
numero_1 = str(input())
numero_2 = str(input())

print('que operacion desea realizar?')
print('ingrese: (+), (-), (*), (/), (**)')
operacion = str(input())

if operacion = (+): suma = numero_1 + numero_2:
    print('la suma entre', numero_1, 'y', numero_2, 'es:', suma)
elif operacion = (-): resta = numero_1 - numero_2:
    print('la resta entre', numero_1, 'y', numero_2, 'es:', resta)
elif operacion = (*): multiplicacion = numero_1 * numero_2:
    print('la multiplicacion entre', numero_1, 'y', numero_2, 'es:', multiplicacion)
elif operacion = (/): division = numero_1 / numero_2:
    print('la division entre', numero_1, 'y', numero_2, 'es:', division)
elif potencia = (**): potencia = numero_1 ** numero_2:
    print('la potencia entre', numero_1, 'y', numero_2, 'es:', potencia)


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
print('ingrese tres palabras cualesquiera')

palabra_1 = str(input())
palabra_2 = str(input())
palabra_3 = str(input())
lista_palabras = (palabra_1, palabra_2, palabra_3)
lista_caracteres = (len(palabra_1), len(palabra_2, len(palabra_3)))

print('como quisiera ordenarlas?')
print('ingrese el numero: 1, para orden alfabetico')
print('ingrese el numero: 2, para cantidad de letras')
ingrese_opcion = str(input())
orden_alfabetico == 1
cantidad_letras == 2

if orden_alfabetico == 1: lista_palabras.sort(reverse = True):
    print('{} {} y {} estan en orden alfabetico decreciente'.format.lista_palabras.sort)
elif cantidad_letras == 2: lista_caracteres.sort(reverse = True):
    print('{} {} y {} estan por cantidad de letras'.format.lista_caracteres.sort)


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

    print('ingrese tres valores de temperatura')
    temperatura_1 = str(input())
    temperatura_2 = str(input())
    temperatura_3 = str(input())
    listado = (temperatura_1, temperatura_2, temperatura_3)
    suma = (temperatura_1 + temperatura_2 + temperatura_3)
    listado_len = len(listado)

    maxima = max(listado)
    minima = min(listado)
    promedio = avg(suma / listado_len)

    if maxima:
      print("la temperatura maxima es: {}".format(maxima))

    if minima:
      print("la temperatura minima es {}".format(minima))

    if promedio:
      print("la temperatura promedio es {}".formata(promedio)

if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
