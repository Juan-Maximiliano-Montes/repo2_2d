
def ingresar_decimal():
    while True:
        try:
            dec = float(input("\nIngrese número decimal: "))
            break
        except ValueError:
            print("\nEl número ingresado es incorrecto.\n")
    return dec

def contar_parte_entera(num):
    num = abs(num)
    cont = 0
    if num == 0:
        cont += 1
    else:
        parte_entera = num - (num % 1)
        while parte_entera != 0:
            cont += 1
            parte_entera = parte_entera // 10
    return cont

def contar_parte_decimal(num):
    cont = 0
    band = 0
    parte_decimal = str(num)
    for decimal in parte_decimal:
        if decimal == ".":
            band = 1
        else:
            if band == 1:
                cont +=1
    return cont

def mostrar_cantidades(cant1, cant2):
    print(f"\nLa cantidad de dígitos de la parte entera es: {cant1}")
    print(f"\nLa cantidad de dígitos de la parte decimal es: {cant2}\n")
    
    