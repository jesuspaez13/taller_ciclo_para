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

# Ejercicio 2
def animales(elefantes, jirafas, chimpances):
    Raza_animal = str(input('Digite el animal que se va a estudiar: '))
    rango_edad_uno = 0
    rango_edad_dos = 0
    rango_edad_tres = 0
    if(Raza_animal == 'elefante'):
        for x in range(elefantes):
            edad = int(input(f'Digite la edad {x+1}: '))
            if(edad >= 0 and edad <= 1):
                rango_edad_uno = rango_edad_uno + 1
                porcentaje1 = (rango_edad_uno * 100) / 20
            elif(edad > 1 and edad < 3):
                rango_edad_dos = rango_edad_dos + 1
                porcentaje2 = (rango_edad_dos * 100) / 20
            elif(edad >= 3):
                rango_edad_tres = rango_edad_tres + 1
                porcentaje3 = (rango_edad_tres * 100) / 20
            else:
                print('La edad ingresada es equivocada')
        print(f'El porcentaje de elefantes entre 0 y 1 años es: {porcentaje1}')
        print(f'El porcentaje de elefantes entre 1 y 3 años es: {porcentaje2}')
        print(f'El porcentaje de elefantes de 3 ó más años es: {porcentaje3}')
    if(Raza_animal == 'jirafa'):
        for x in range(jirafas):
            edad = int(input(f'Digite la edad {x+1}: '))
            if(edad >= 0 and edad <= 1):
                rango_edad_uno = rango_edad_uno + 1
                porcentaje1 = (rango_edad_uno * 100) / 15
            elif(edad > 1 and edad < 3):
                rango_edad_dos = rango_edad_dos + 1
                porcentaje2 = (rango_edad_dos * 100) / 15
            elif(edad >= 3):
                rango_edad_tres = rango_edad_tres + 1
                porcentaje3 = (rango_edad_tres * 100) / 15
            else:
                print('La edad ingresada es equivocada')
        print(f'El porcentaje de jirafas entre 0 y 1 años es: {porcentaje1}')
        print(f'El porcentaje de jirafas entre 1 y 3 años es: {porcentaje2}')
        print(f'El porcentaje de jirafas de 3 ó más años es: {porcentaje3}')
    if(Raza_animal == 'chimpance'):
        for x in range(chimpances):
            edad = int(input(f'Digite la edad {x+1}: '))
            if(edad >= 0 and edad <= 1):
                rango_edad_uno = rango_edad_uno + 1
                porcentaje1 = (rango_edad_uno * 100) / 40
            elif(edad > 1 and edad < 3):
                rango_edad_dos = rango_edad_dos + 1
                porcentaje2 = (rango_edad_dos * 100) / 40
            elif(edad >= 3):
                rango_edad_tres = rango_edad_tres + 1
                porcentaje3 = (rango_edad_tres * 100) / 40
            else:
                print('La edad ingresada es equivocada')
        print(f'El porcentaje de chimpancés entre 0 y 1 años es: {porcentaje1}')
        print(f'El porcentaje de chimpancés entre 1 y 3 años es: {porcentaje2}')
        print(f'El porcentaje de chimpancés de 3 ó más años es: {porcentaje3}')
animales(20, 15, 40)

# Ejercicio 3
def numero_obreros(obreros):
    if(obreros > 0):
        for x in range(obreros):
            horas = int(input(f'Digite las horas trabajadas del obrero {x + 1}: '))
            if(horas <= 40):
                salario = horas * 20
                print(f'El salario del obrero es: {salario}')
            elif(horas > 40):
                sub_salario = horas - 40
                salario = (sub_salario * 25) + 800
                print(f'El salario del obrero es: {salario}')
    else:
        print('El número de obreros es equivocado')
numero_obreros(3)

# Ejercicio 4
def total_grupo(todo_el_grupo, hombres, mujeres):
    promedio_grupo = 0
    promedio_hombres = 0
    promedio_mujeres = 0
    for x in range(todo_el_grupo):
        edad = int(input(f'Digite la edad del alumno {x+1}: '))
        sexo = str(input(f'Digite si es hombre o mujer el alumno {x+1}: '))
        if(sexo == 'hombre' or sexo == 'mujer'):
            promedio_grupo = promedio_grupo + edad
            promedio_grupo = round(promedio_grupo, 2)
            total_grupos = promedio_grupo / todo_el_grupo
            #print(f'El promedio de edad de todo el grupo es: {total_grupos}')
            if(sexo == 'hombre'):
                promedio_hombres = promedio_hombres + edad
                promedio_hombres = round(promedio_hombres, 2)
                total_hombres = promedio_hombres / hombres
                #print(f'El promedio de edad de los hombres es: {total_hombres}')
            elif(sexo == 'mujer'):
                promedio_mujeres = promedio_mujeres + edad
                promedio_mujeres = round(promedio_mujeres, 2)
                total_mujeres = promedio_mujeres / mujeres
                #print(f'El promedio de edad de las mujeres es: {total_mujeres}')
        else:
            print('El sexo ingresado es equivocado')
    print(f'El promedio de edad de todo el grupo es: {total_grupos}')
    print(f'El promedio de edad de los hombres es: {total_hombres}')
    print(f'El promedio de edad de las mujeres es: {total_mujeres}')
total_grupo(4, 2, 2)

# Ejercicio 5
def total_numeros(conjunto_numeros):
    import math
    menor = math.inf
    for x in range(conjunto_numeros):
        numero = float(input(f'Digite el número {x+1}: '))
        if(numero < menor):
            menor = numero
    print(f'El número menor es: {menor}')
total_numeros(3)

# Ejercicio 6
def total_mienbros(mienbros):
    peso = 0
    for x in range(mienbros):
        peso_antiguo = int(input(f'Digite el peso antiguo de la persona {x+1}: ')) 
    for p in range(10):
        peso = int(input(f'Digite el peso de la báscula {p+1}: '))   
    if(peso_antiguo - peso < 0):
        print("El miembro bajó: ", peso_antiguo - (peso / 10), "kilos")
    if(peso_antiguo - peso > 0):
        print("El miembro subió: ", peso_antiguo - (peso / 10), "kilos")
total_mienbros(5) 

# Ejercicio 7
def supermercado(numero_de_productos):
    total = 0
    for x in range(numero_de_productos):
        precio = int(input(f'Digite el precio del producto {x+1}: '))
        if(precio > 1):
            cantidad = int(input('Digite que cantidad va llevar: '))
            sub_total = precio * cantidad
            total = total + sub_total
        else:
            precio = 0
    print(f'El total de la compra es: {total}')
supermercado(2)

# Ejercicio 8
def personas(numero_de_personas):
    precio_boleta = int(input("Digite el precio de la boleta "))
    num_personas = int(input("digite el número de personas "))
    rango_edad_1 = 0
    rango_edad_2 = 0
    rango_edad_3 = 0
    rango_edad_4 = 0
    rango_edad_5 = 0
    for x in range(numero_de_personas):
        edad = int(input(f'Digite la edad de la persona {x+1}: '))
        if edad < 5:
            print("Los niños menores de 5 años no pueden entrar")
        if edad > 5 and edad <= 14:
            rango_edad_1 += 1
        if edad > 15 and edad <= 19:
            rango_edad_2 += 1
        if edad > 20 and edad <= 45:
            rango_edad_3 += 1
        if edad > 46 and edad <= 65:
            rango_edad_4 += 1
        if edad > 66:
            rango_edad_5 += 1
    print('El dinero no percibido por el descuento en la categoría 5-14 es: ',
          rango_edad_1*precio_boleta*0.35)
    print('El dinero no percibido por el descuento en la categoría 15-20 es: ',
          rango_edad_2*precio_boleta*0.25)
    print('El dinero no percibido por el descuento en la categoría 20-45 es: ',
          rango_edad_3*precio_boleta*0.10)
    print('El dinero no percibido por el descuento en la categoría 46-65 es: ',
          rango_edad_4*precio_boleta*0.25)
    print('El dinero no percibido por el descuento en la categoría 66-adelante es: ',
          rango_edad_5*precio_boleta*0.35)
personas(2)

# Ejercicio 9
def empleados(numero_de_empleados):
    for x in range(numero_de_empleados):
        venta = int(input(f'Digite cuanto vendío el empleado {x+1}: '))
        if(venta < 20):
            print("La comisión del empleado es de ", venta*0.1)
        if(venta < 40 and venta > 20):
            print("La comisión del empleado es de ", venta*0.15)
        if(venta < 80 and venta >= 40):
            print("La comisión del empleado es de ", venta*0.20)
        if(venta < 160 and venta >= 80):
            print("La comisión del empleado es de ", venta*0.25)
        if(venta > 160):
            print("La comisión del empleado es de ", venta*0.30)
empleados(100)
