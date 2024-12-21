### Ejemplo 1 - Listas ###
numero = [1,3,5,7,9,11]
fruta = ['manzana', 'pera', 'mandarina','melon','fresa']
dato = [1, 'carlos', 7.35, 'otro',True, False]

#Imprimir 4to dato de la lista
print(dato[3])
#Imprimir último dato de las listas
print(numero[-1])
print(fruta[-1])
print(dato[-1])
#Añadir número al final de al lista 
numero.append(13)
print(numero[-1])
#Eliminar un número de la fila
numero.remove(13)
print(numero[-1])

#forma de poder ver todos los datos de una lista
for i in numero:
    print(i)

for i in dato:
    print(i)

#Elevar un número al cuadrado en un rango específico
elevacion = [x**2 for x in range(1,6)]
print(elevacion)

#### Ejemplo 2 - Tupla ####
Color = ('Azul','Rojo','verde','amarillo','rosado')
numeros = (1,5,9,12,20,1)

#Cantidad de elementos en la tupla
print(len(Color))
print(len(numeros))

#Contar elementos repetidos en una tupla o lista
print(numeros.count(1))

### Ejercicio 3 - Diccionario ###
#Diccionadio normal
diccionario = {'Aldair':'Tepic','Carlos':'Bogorá','Sergio':'Guanajuato','Josué':'Guadalajara','Elker':'Monterrey','José':'Estado de México'}
print(diccionario)
#Diccionadio como lista anidada
d1 = dict([
    ('Aldair','Tepic'),
    ('Carlos','Bogorá'),
    ('Sergio','Guanajuato'),
    ('Josué','Guadalajara'),
    ('Elker','Monterrey'),
    ('José','Estado de México')
])
print(d1)