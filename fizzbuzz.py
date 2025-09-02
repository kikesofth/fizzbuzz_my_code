numero = int(input('Ingresa el numero de interacciones a comprobar impares: '))

def fizzbuzz(numero):
    # Haciendo un recorrido qie se dio en el anterior paso
    for i in range(1, numero +1):
        #Comparando si al dividir el numero dado por 5 o 0 da 0
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

# Se llama a la funcion para que imprima
fizzbuzz(numero)