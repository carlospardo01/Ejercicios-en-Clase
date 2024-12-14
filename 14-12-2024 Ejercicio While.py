#Lista con las respuestas correctas
Palabra = ["Trasnocharse", "trasnocharse"]
#Contador y límite de intentos
contador = 0
limite = 3
#se usa la función While para contar la cantidad de intentos y ver si es correcto lo que responde
while contador < limite:
    # Se hace la pregunta de la adivinanza, se captrua el dato y se eliminan los espacios en blanco
    respuesta = input("Adivinanza:\n¿Qué es lo que se hace de noche, que no se puede hacer de día?\n").strip()
    #Cuenta la cantidad de respuestas
    contador += 1
    #compara si la respuesta es correcta y si es correcta, imprime un mensaje en pantalla y rompe el bucle, de lo contrario vuelve a intentarlo hasta que acaba el bucle
    if respuesta in Palabra:
        print("La respuesta es correcta.")
        break
#Imprime mensje si no logro contestar en los intentos permitidos
else:
    print("Lo siento, sigue intentando, la respuesta es: Trasnocharse")