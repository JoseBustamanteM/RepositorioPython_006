#Crear menu con 3 opciones
import os

def Numeros():
    #Ingresar n numeros donde n es un numero ingresado por teclado.
    #Mostrar cantidad de nuemeros positivos, cantidad de numeros negativos y cantidad de numeros igual a 0
    mayor=0
    menor=0
    igual=0

    cantidad=int(input("ingrese cantidad de números a ingresar: "))

    for i in range(cantidad):
        n=int(input(str(i)+".- Ingresa un número "))

        if (n>0):
            mayor+=1
        elif (n<0):
            menor+=1
        else:
            igual+=1
    print("cantidad de números positivos: "+str(mayor))
    print("cantidad de números negativos: "+str(menor))
    print("cantidad de 0: "+str(igual))


def Personas():
    #Ingresar para n personas: nombre y edad. Mostrar promedio de todas la edades ingresadas

     
    edad = 0
    promedio = 0

    personas = int(input("Cantidad de personas a ingresar"))
    for i in range(personas)
        a = int(input(str(i)+"  Ingresa la edad"))

        edad = edad + a
    
    promedio = edad / personas

    print("promedio de edades es: " promedio)




seguir=True
while (seguir):
    os.system('cls')
    print("1. Numeros")
    print("2. Datos personales")
    print("3. Finalizar")
    op=int(input("Digite opcion 1, 2, 3: "))
    if (op==1):
        Numeros()
    if (op==2):
        Personas()
    if (op==3):
        print("Programa finalizado")
        break