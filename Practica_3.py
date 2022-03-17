from os import system


def es_primo(numero):
    contador = 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False


def numerosFibonacci():
    system("clear")
    numero = int(
        input("Introduce la cantidad de números que deseas de esta sucesión: "))
    a, b = 0, 1
    for _ in range(0, numero):
        print(a, end=' ')
        a, b = b, a+b

    input()


def numeroRomano():
    system("clear")
    numero = int(input("Ingrese un numero entero: "))
    n = numero
    decimales = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanos = ['M', 'CM', 'D', 'CD', 'C', 'XC',
               'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    num = ''
    i = 0
    while numero > 0:
        for _ in range(numero//decimales[i]):
            num += romanos[i]
            numero -= decimales[i]
        i += 1
    print("El número " + str(n) + " es igual a: " + str(num))
    input()


def run():
    menu = """
        Python Práctica #3 
        
    [1]_____Imprimir números primos
    [2]_____Imprimir números de la serie Fibonacci
    [3]_____Convertir un número decimal a romano
    [4]_____Salir """

    op_salir = False

    while op_salir != True:
        system("clear")
        print(menu)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            system("clear")
            numero = int(input('Escribe un número: '))
            contador = 0
            num = 2
            while contador < numero:
                if es_primo(num):
                    print(num, end=' ')
                    contador += 1
                num += 1
            input()
        elif opcion == "2":
            system("clear")
            numerosFibonacci()
        elif opcion == "3":
            numeroRomano()
        elif opcion == "4":
            op_salir = True
        else:
            system("clear")
            print("Opción no valida.")


if __name__ == "__main__":
    run()
