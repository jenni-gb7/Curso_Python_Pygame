"""
El tablero de conexiones conectaba las 26 letras del alfabeto latino entre sí, de modo que una entrada en una letra podía generar una salida como otra letra. Si no había un cable, entonces la letra de entrada no se modificó. Cada placa de conexión venía con un máximo de 10 cables, por lo que al menos seis letras no estaban conectadas entre sí.

Por ejemplo:

Si un cable se conecta a , entonces una entrada generará una salida y una entrada generará una salida.ABABBA

Si no se conecta ningún cable a , entonces solo una entrada generará una salida.CCC
"""

class Plugboard:
    def __init__(self, wires: str = ""):
        """
        wires: This is the mapping of pairs of characters
        """

        if len(wires) > 20:
            raise ValueError("Too many wires")

        if len(wires) % 2:
            raise ValueError("Partial wire definition")

        if len(wires) != len(set(wires)):
            raise ValueError("A wire is mapped twice")

        self.plugs = dict(zip(wires[::2] + wires[1::2], wires[1::2] + wires[::2]))

    def process(self, c: str) -> str:
        """
        c: The single character to process
        """
        return self.plugs.get(c, c)
