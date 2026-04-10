
def ingresar_entero():
    while True:
        try:
            num = int(input("\nIngrese un número entero: "))
            print(f"\nEl número ingresado es correcto.\n")
            break
        except ValueError:
            print("Número o dato incorrecto. Ingrese nuevamente.\n")
    return num
    
def cantidad_digitos(num):
    num = abs(num)
    cont = 0
    if num == 0:
        cont += 1
    else:
        while num != 0:
            cont += 1
            num = num//10
    return cont

def mostrar_cant_digitos(cant):
    print(f"La cantidad de dígitos que tiene el número ingresado es: {cant}. \n")