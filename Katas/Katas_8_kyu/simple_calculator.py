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
        res1 = x + y
        print(res1)
    elif opc == "-":
        res2 = x - y
        print(res2)
    elif opc == "*":
        res3 = x * y
        print(res3)
    elif opc == "/":
        res4 = x / y
        print(res4)
    elif opc == "&":
        res5 = x & y
        print(res5)
    else:
        print("unknown value")


if __name__ == '__main__':
    x = int(input("Ingresa el primer número:"))
    y = int(input("Ingresa el segundo número:"))
    opc = str(input("Ingresa el opción:"))
    calculator(x,y,opc)