numero = int(input('Ingresa el numero de interacciones a comprobar impares: '))

def fizzbuzz(numero):
    for i in range(1, numero +1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


fizzbuzz(numero)