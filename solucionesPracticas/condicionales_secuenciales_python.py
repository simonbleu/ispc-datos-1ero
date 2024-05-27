
"""
Ejemplos simples de estructuras condicionales para los ejercicios de la presentacion. En el primer ejemplo se
pregunta la edad y solo se responde en caso de que la edad sea igual o menor a cero. En el segundo se vuelve a
preguntar la edad, como en el resto de los ejemplos, pero en particular en este caso response si el numero es par
(utilizando el operador de modulo) o impar (else). En el tercero indica si la edad ingresada corresponde a una 
persona en edad laboral (mayor o igual a 18, y menor a 60). En el ultimo ejemplo detalla si la edad corresponde
a una persona menor a 18 años, o si su edad es igual o mayor a 70 años,lo cual en cualquiera de los casos implica
que el individuo no esta obligado a votar en las elecciones.

"""

#1 condicional parcial (if) simple
num = int(input("Ingrese su edad"))
if num <=0:
    print("la edad ingresada no es mayor a cero, intente nuevamente")
    
#2 condicional completo (if-else) simple
num = int(input("Ingrese su edad"))
if (num % 2) == 0:
    print("su edad es un numero par")
else:
    print("su numero es un numero impar")  
    
#3 condicional parcial (if) compuesto (and)
num = int(input("Ingrese su edad"))
if num >= 18 and num < 60:
    print("Ustead es mayor de edad, pero aun es muy joven para jubilarse")
    
#4 condicional completo (if-else) compuesto (or)
num = int(input("Ingrese su edad nuevamente"))
if num < 18  or num >= 70:
    print("Debido a su edad, usted no esta obligado de participar en las elecciones")
else:
    print("Debido a su edad, usted esta obligado de participar en las elecciones")
    
    