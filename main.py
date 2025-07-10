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

class Binario(Numero):
    def __init__(self, valor):
        super().__init__(valor)

    def __str__(self):
        return self.valor

    def numero_es_binario(self):
        cadena = str(self.valor)
        if all(digito in '01' for digito in cadena):
            return  True
        else:
            raise ValueError("El valor no es un número binario válido")

    def calcular_binario_decimal(self):
        self.numero_es_binario()
        cadena = str(self.valor)
        resultado = 0
        lista = [int(digito) for digito in cadena]
        for i, digito in enumerate(reversed(lista)):
            resultado += int(digito) * (2 ** i)
        return resultado

numero2 = Binario(10)

print(numero2.calcular_binario_decimal())
