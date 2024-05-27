"""
Estas es una version de python del ejercicio de cambio de divisas.
El programa empeiza pidiendote el valor de venta, o cambio, de la moneda hacia el dolar estadounidense y entra en 
bucle volviendote a pedir el dato si el numero ingresado es igual o menor a cero. Luego se inicializa la variable
"interesado" que representa al menu, en 1, lo que lleva a pedirte que ingreses el monto a convertir y lo divide en
el cambio para imprimir la conversion. Luego te pregunta si desea hacer otra conversion, en cuyo caso la operacion
se repite, si desea salir, en cuyo caso se agradece y termina, o si desea cambiar el valor de la variable de cambio.
De elegir esta ultima las opciones son las mismas que las iniciales; En caso de elegir un numero mayor o menor a los 
establecidos para el menu, se informara del error y se continuara pidiendo un numero valido (0, 1 o 2)
"""
    
cambio = float(input("Ingrese el valor de venta del dólar estadounidense (USD): "))
while cambio <= 0:
    cambio = int(input("El valor de venta debe ser mayor a cero. Ingrese un nuevo valor: "))

interesado = 1

while True:  # Bucle infinito controlado por las condiciones internas
    if interesado == 1:
        monto = int(input("Ingrese el monto a convertir a USD: "))
        print("$", monto, " equivalen a ", monto / cambio, " dólares.")
        interesado = int(input("Desea realizar otra conversión? 2 = cambiar valor de conversión / 1 = Si / 0 = No: "))
    elif interesado == 2:
        cambio = float(input("Ingrese el valor de venta del dólar estadounidense (USD): "))
        while cambio <= 0:
            cambio = float(input("El valor de venta debe ser mayor a cero. Ingrese un nuevo valor: "))
        interesado = 1
    elif interesado == 0:
        print("Muchas gracias por utilizar nuestro servicio!")
        break  # Salir del bucle
    else:
        print("La opción seleccionada no es correcta.")
        interesado = int(input("Desea realizar otra conversión? 2 = cambiar valor de conversión / 1 = Si / 0 = No: "))
    
    
    
    
    
    
    
    
    
    
    

