# Función para calcular el área de un rectángulo
def calcular_ARectangulo(altura, base):
    return altura * base

# Función para calcular el área de un triángulo
def calcular_ATriangulo(base, altura):
    return 0.5 * base * altura

# Función principal
def main():
    base = 4
    altura = 6
    rectangulo_area = calcular_ARectangulo(base, altura)
    print("Área del rectángulo:", rectangulo_area)

    base = 5
    altura = 8
    triangulo_area = calcular_ATriangulo(base, altura)
    print("Área del triángulo:", triangulo_area)

main()
