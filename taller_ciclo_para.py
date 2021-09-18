# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 21:41:02 2021

@author: USER
"""
# Ejercicio 1
def variable(cantidad_autos):
    amarillo = 0
    rosa = 0
    rojo = 0
    verde = 0
    azul = 0
    for x in range(cantidad_autos):
        placa = int(input(f'Digite el ultimo digito de la placa {x+1}: '))
        if(placa == 1 or placa == 2):
            amarillo = amarillo + 1
        elif(placa == 3 or placa == 4):
            rosa = rosa + 1
        elif(placa == 5 or placa == 6):
            rojo = rojo + 1
        elif(placa == 7 or placa == 8):
            verde = verde + 1
        elif(placa == 9 or placa == 0):
            azul = azul + 1
        else:
            print('El numero ingresado en equivocado')
    print(f'Total de carros con calcomanía amarilla: {amarillo}')
    print(f'Total de carros con calcomanía rosa: {rosa}')
    print(f'Total de carros con calcomanía roja: {rojo}')
    print(f'Total de carros con calcomanía verde: {verde}')
    print(f'Total de carros con calcomanía azul: {azul}')
variable(3)
