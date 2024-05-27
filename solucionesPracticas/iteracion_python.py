"""
El ejercicio uno pide que el usuario ingrese un numero mayor a cero. Si lo hace correctamente, comienza a contar desde 1 
hasta el numero tipeado, caso contrario informa al usuario que el numero es menor o igual a cero. En el Ejercicio 2 el
algoritmo tambien pide un numero, en este caso mayor a 1, y cuenta solamente los pares. Y en el tercer ejercicio se pide
al usuario ingresar nombres, imprimiendolo en pantalla, hasta que presione fin, que da fin al bucle.
    
    """
    
# Ejercicio 1
num = int(input('Ingrese un numero mayor a 0 para comenzar a contar: '))
if num <= 0:
    print("El numero debe ser mayor a cero.")
else:
    for i in range(1,num+1):
        print(i)

# Ejercicio 2
num = int(input('Ingrese un numero mayor a 1 para comenzar a contar los pares: '))
if num <= 1:
    print("El numero debe ser mayor a uno.")
else:
    for i in range(1,num+1):
        if i % 2 == 0:
            print(i)


# Ejercicio 3

nombre = str(input("Escriba un nombre, o escriba 'fin' para salir: "))

while nombre != "fin":
    print(nombre)
    nombre = str(input("Escriba otro nombre, o escriba 'fin' para salir: "))
    
