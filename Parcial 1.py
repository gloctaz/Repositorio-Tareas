numero = int(input("Ingresa un número entero de 4 dígitos: "))

if 1000 <= numero <= 9999:

    d1 = numero // 1000
    d2 = (numero % 1000) // 100
    d3 = (numero % 100) // 10
    d4 = numero % 10

    if d1 > d2:
        extra = d1
        d1 = d2
        d2 = extra

    if d1 > d3:
        extra = d1
        d1 = d3
        d3 = extra

    if d1 > d4:
        extra = d1
        d1 = d4
        d4 = extra

    if d2 > d3:
        extra = d2
        d2 = d3
        d3 = extra

    if d2 > d4:
        extra = d2
        d2 = d4
        d4 = extra

    if d3 > d4:
        extra = d3
        d3 = d4
        d4 = extra

    print("Forma ascendente:", d1, d2, d3, d4)
    print("Forma descendente:", d4, d3, d2, d1)

else:
    print("Número no válido")