#Functions

import os 

#Shows menu
def menu():
    print("SISTEMA DE ANALISIS DE INGRESOS" + str("\n"))
    print("Ingrese 1 para cargar un nuevo dia de ingresos")
    print("Ingrese 2 para analizar un dia")
    print("Ingrese 3 para borrar un dia")
    x = int(input())
    if (x == 1):
        cargar()
    elif (x == 2):
        analizar()
    elif (x == 3):
        borrar()
    else:
        print("Error, operacion no valida")
    menu()

#Loads information
def cargar():
    try:
        y = []
        dia = str("Dia_" + input("Ingrese el numero de dia: "))

        #Llena la lista
        print('Ingrese un monto de dinero: ')
        x = int(input())
        while x != -1:
            y.extend([x])
            print('Ingrese un monto de dinero: ')
            x = int(input())
        print(y)
        y.sort()
        print(y)

        # Rellena la base de datos
        handle = open(dia , "a")
        for index in range(len(y)):
            handle.write(str(y[index]) + str("\n"))
        handle.close()
    except:
        print("Ha ocurrido un error, volviendo al menu" + str("\n"))
        menu()

#Analyzes selected day
def analizar():
    try:
        acu = int()
        day = input("Ingrese el dia que desea analizar: ") 
        file = str("Dia_" + day)
        f = open(file, "r")
        while True:
            line = f.readline()
            if not line:
                break
            print(line)
            acu = acu + int(line)
        print(str("\n") + "Las ganancias totales del dia: " + str(day) + " fueron de: $" + str(acu) + str("\n") )
    except:
        print(str("\n") + "Ha ocurrido un error, volviendo al menu" + str("\n"))

#Deletes a day
def borrar():
    try:
        day = input("Ingrese el dia que quiere borrar: ")
        os.remove(str("Dia_" + str(day)))
        print(str("\n") + "Se removio el dia")
    except:
        print(str("\n") + "Ha ocurrido un error, volviendo al menu" + str("\n"))

#Main program
menu()