"""
Jennifer Marlene Gutiérrez Beteta
10 de Abril de 2025.

Descripción del programa:
Debe crear una calculadora simple que devuelva el resultado de la suma, resta, multiplicación o división de dos números.

La función aceptará tres argumentos:
El primer y el segundo argumento deben ser números.
El tercer argumento debe representar un signo que indique la operación a realizar sobre estos dos números.

Si las variables no son números o el signo no pertenece a la lista anterior, se debe devolver el mensaje "Valor desconocido".
"""

def calculator(x, y, opc):
    if opc == "+":
        return  x + y
    elif opc == "-":
        return  x - y
    elif opc == "*":
        return  x * y
    elif opc == "/":
        return  x / y
    else:
        return "unknown value"



if __name__ == '__main__':
    x = int(input("Ingresa el primer número:"))
    y = int(input("Ingresa el segundo número:"))
    opc = str(input("Ingresa el opción:"))