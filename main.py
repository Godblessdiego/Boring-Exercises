class Numero:
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return str(self.valor)

    def calcular_decimal_binario(self):
        restos = []
        numero_actualizado = self.valor
        while numero_actualizado > 0:
            resto = numero_actualizado % 2
            restos.append(resto)
            numero_actualizado //= 2
        numero_bytes = ''.join(str(resto) for resto in restos[::-1])
        return numero_bytes

numero1 = Numero(10)

print(numero1.calcular_decimal_binario())
