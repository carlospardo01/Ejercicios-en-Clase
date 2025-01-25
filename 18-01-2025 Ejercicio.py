#si todos estan dormidos la profesora pone una actividad

Estudiante = input("Cómo está el estudiante? \nA) dormido \nB) despierto\n")
Actividad = 1

while Estudiante == "A":
    profesor = print("Toca hacer una actividad")
    if Actividad == 1:
        print("Todos deben hacer un ejercicio que complemente al de sus compañeros")
        break
else:
    print("Toca ayudar a tus compañeros")