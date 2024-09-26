# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 23:51:56 2023

@author: Admin

"""

# Juego de bolas verdes y azules. El jugador debe tomar una bola al insertar un numero. Si el número corresponde
# a una bola azul acierta. El jugador debe intentarlo hasta encontrar las 5 bolas

from random import randint
import sys


# creación de lista con las bolas. V = verde, A = azul
contador_de_intentos = 0


# funcion para crear la lista con las bolas aleatoriamente
def bolsa_de_bolas():
    Lista_bolas = []
    bolas_azules = 0
    bolas_verdes = 0
    for bola in range(20):
        color = randint(0, 1)
        if color == 0 and bolas_azules < 5 and bolas_verdes <= 15:
            Lista_bolas.append("A")
            bolas_azules += 1
        else:
            Lista_bolas.append("V")
            bolas_verdes += 1
    return Lista_bolas


# Función para verificar que valores se enceuntren en rango de lista
def corrector(valor, Bolas_iniciales):
    while True:
        try:
            bandera = True
            while bandera == True:
                if valor >= Bolas_iniciales or valor <= -1:
                    print("Ese numero/valor no es valido")
                    valor = int(
                        int(
                            input(
                                "Favor ingresar un número del 1 al  "
                                + str(Bolas_iniciales)
                                + " : "
                            )
                        )
                        - 1
                    )
                else:
                    bandera = False
            break
        except ValueError:
            print("Ese no es un número")
    return valor


# Decide si la bola selecionada es azul o no
def identificar_bola(valor, lista):
    if lista[valor] == "A":
        print("bien! encontraste la bola azul")
        return True
    else:
        print("lastima!,No es una bola azul")
        return False


# Se usa para decidir si la bola elecionada es azul o no
def buscar_elemento(elemento, lista):
    for item in lista:
        if lista[item] == elemento:
            return True
        else:
            return False


# devuelve el número de intentos qe le tomó al jugador encontrar la bola azul
def numero_intentos(lista, Bolas_iniciales):
    contador_de_intentos = 0
    detener = False

    while (
        detener == False or contador_de_intentos < 0
    ):  # la primera condición es la bandera y la otra condición es para evitar el error de local variable assignada pero no usada
        while True:  # función para verificar que el jugador inserte un número
            try:
                entrada = (
                    int(
                        input(
                            "Favor ingresar un número del 1 al  "
                            + str(Bolas_iniciales)
                            + " : "
                        )
                    )
                    - 1
                )
                break
            except ValueError:
                print("Ese no es un número")
        intento = corrector(entrada, Bolas_iniciales)
        if identificar_bola(intento, lista) == True:
            print("felicdades!,encontraste la bola azul ")
            detener = True
            lista.pop(intento)
            contador_de_intentos += 1
        else:
            print("Lastima, no es la bola azul,. Intentalo de nuevo")
            contador_de_intentos += 1

    return contador_de_intentos


# función principal, invoca al juego y se detiene cuando el jugador logra encontrar las 5 bolas azules
def Juego_bolas():
    print("Bienvenido al Juego // Tratar de tomar la bola azul")
    bolas = bolsa_de_bolas()
    contador_bolas_azules = 0
    intentos_totales = 0
    detener = False
    bolas_iniciales = 20
    while detener == False:
        intentos_totales = intentos_totales + numero_intentos(bolas, bolas_iniciales)
        bolas_iniciales -= 1
        contador_bolas_azules += 1

        print(intentos_totales)
        # print(bolas)
        print("contador de bolas " + str(contador_bolas_azules))
        if contador_bolas_azules == 5:
            detener = True
        else:
            pass

    print("felicidades! Has ganado el juego")
    print("te tomo " + str(intentos_totales) + " intentos ganar")
    sys.exit("Adios ")


Juego_bolas()
