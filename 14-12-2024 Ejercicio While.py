#numero=9
#contador=0
#limite=3
#while contador<limite:
#    respuesta = int(input("Digita un número: "))
#    contador += 1
#    if respuesta == numero:
#        print("Felicidades, Ganaste!")
#        break
#else:
#    print("Lo siento, perdiste")


Palabra= ["Trasnocharse","trasnocharse"]
contador=0
limite=3
while contador<limite:
    respuesta = input("¿Qué es lo que se hace de noche, que no se puede hacer de día?, Cúal sería la respuesta: ")
    contador += 1
    if respuesta == Palabra:
        print("La respuesta es correcta.")
        break
else:
    print("Lo siento, Sigue intentando, la respuesta era Trasnocharse.")