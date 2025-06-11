import ply.yacc as yacc
from analizador_lexico import analizador, tokens  # Trae el analizador léxico y los tokens

# Aquí guardamos las variables que el usuario crea y sus valores
nombres = {}

# Variable para saber qué regla de la gramática se usó en el parser
produccion_usada = ""

# ------------------ REGLAS DEL PARSER ------------------

# Cuando el usuario escribe una asignación, por ejemplo: x = 5 + 3;
def p_declaracion_asignar(t):
    'declaracion : IDENTIFICADOR ASIGNAR expresion PUNTOCOMA'
    global produccion_usada
    nombres[t[1]] = t[3]  # Guarda el resultado de la expresión en la variable
    produccion_usada = 'declaracion : IDENTIFICADOR ASIGNAR expresion PUNTOCOMA'
    t[0] = f"nombres['{t[1]}'] = {t[3]}"  # Mensaje para mostrar qué se hizo

# Cuando solo escriben una expresión sin asignar, por ejemplo: 2 + 3;
def p_declaracion_expr(t):
    'declaracion : expresion'
    global produccion_usada
    produccion_usada = 'declaracion : expresion'
    t[0] = t[1]  # El resultado es el valor de la expresión

# Suma: una expresión + un término
def p_expresion_suma(t):
    'expresion : expresion SUMA termino'
    t[0] = t[1] + t[3]  # Suma los dos valores

# Resta: una expresión - un término
def p_expresion_resta(t):
    'expresion : expresion RESTA termino'
    t[0] = t[1] - t[3]  # Resta los dos valores

# Cuando solo hay un término, regresa ese término
def p_expresion_termino(t):
    'expresion : termino'
    t[0] = t[1]

# Multiplicación: un término * un factor
def p_termino_mult(t):
    'termino : termino MULT factor'
    t[0] = t[1] * t[3]

# División: un término / un factor
def p_termino_div(t):
    'termino : termino DIV factor'
    if t[3] == 0:
        print("Error: División entre cero.")  # No se puede dividir entre cero
        t[0] = 0
    else:
        t[0] = t[1] // t[3]  # División entera (sin decimales)

# Cuando solo hay un factor, regresa ese factor
def p_termino_factor(t):
    'termino : factor'
    t[0] = t[1]

# Cuando el factor es un número entero
def p_factor_num(t):
    'factor : ENTERO'
    t[0] = t[1]

# Cuando el factor es una variable (identificador)
def p_factor_id(t):
    'factor : IDENTIFICADOR'
    t[0] = nombres.get(t[1], 0)  # Busca el valor en 'nombres', si no existe, da 0

# Para mostrar un error cuando hay un problema en la entrada
def p_error(t):
    if t:
        print(f"\nError de sintaxis en '{t.value}' (línea {t.lineno})\n")
    else:
        print("\nError de sintaxis al final de la entrada\n")

# ------------------ CONSTRUIR EL PARSER ------------------

parser = yacc.yacc()  # Crea el parser con las reglas anteriores

# ------------------ INTERPRETE EN LA CONSOLA ------------------

if __name__ == '__main__':
    while True:
        try:
            entrada = input("ingresa dato >>> ")  # Pide al usuario una expresión o asignación
            if entrada.strip() == "":
                break  # Si el usuario solo da Enter, termina el programa

            print(f"\nUsuario escribe:      {entrada}")

            # PASO 1: El analizador léxico separa la entrada en tokens
            analizador.input(entrada)
            tokens_generados = []
            while True:
                tok = analizador.token()
                if not tok:
                    break
                tokens_generados.append(tok.type)

            print("↓\nLexer (analizador):   ", ' '.join(tokens_generados))

            # PASO 2: El parser analiza si la secuencia de tokens sigue las reglas
            resultado = parser.parse(entrada)
            if resultado is not None:
                print(f"↓\nParser (sintáctico):  \"{produccion_usada}\"")
                print(f"↓\nResultado:            {resultado}")
                if nombres:
                    print("\n", nombres)  # Muestra las variables y sus valores guardados
            else:
                print("No se pudo procesar la entrada.\n")

        except EOFError:
            break
