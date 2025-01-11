#Función sin parámetro
a=10
b=5
def multplicar():
    resultado=a*b
    print(resultado)
multplicar()

#Función con parámetro
altura=8
base=10
def triangulo(a,b):
    c=(altura*base)/2
    print("El área de un tríangulo es: ")
    print(c)
triangulo(8,10)

#funcion para la operacion de suma
a=1
b=2
def suma():
    resultado=a+b
    print(resultado)
suma() 

#funcion para imprimir Hola mundo
def frase():
    print("Hola Mundo")
frase()

#Función que calcule el cuadrado de un número
def cuadrado():
    numero=int(input("ingrese un número: "))
    resultado=numero**2
    print(f"El cuadrado de {numero} es {resultado}")
cuadrado()

#Función que salude a una persona por su nombre capturando el dato
def saludo():
    nombre=input("Ingrese su nombre: ").strip().capitalize()
    print(f"Hola {nombre}, un gusto conocerte")
saludo()

#Función que salude a una persona por su nombre con parámetro
def saludo2(nombre):
    print(f"Hola {nombre}, un gusto conocerte")
saludo2("carlos")