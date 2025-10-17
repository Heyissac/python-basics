'''
 Escribe un programa que muestre por consola (con un print) los
 números de 1 a 100 (ambos incluidos y con un salto de línea entre
 cada impresión), sustituyendo los siguientes:
    - Múltiplos de 3 por la palabra "fizz".
    - Múltiplos de 5 por la palabra "buzz".
    - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''

for i in range(1, 101):
    divByThree = i % 3 == 0
    divByFive = i % 5 == 0
    match (i % 3 == 0, i % 5 == 0):
        case (True, True):
            i = "fizzbuzz"
            print(i)
        case (True, False):
            i = "fizz"
            print(i)
        case (False, True):
            i = "buzz"
            print(i)
        case _:
            print(i)
        







