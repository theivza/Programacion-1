import random
#Programa que genera un número al azar entre 1 y 100 que se tiene que adivinar
nmagico=random.randint(1, 100)
intervalo1=1
intervalo2=100
n=int(input("Ingresa el número magico [1-100]:\n"))
while n < 1 | n > 100:
    n=int(input("Ingresa el número amgico en el intervalo [1 al 100]:\n"))
while n != nmagico:
    if nmagico > n:
        print("Pista el número magico es mayor")
        intervalo1=n+1
        print("nuevo intervalo [", intervalo1, "-", intervalo2, "]")
    else:
        print("Pista el número magico es menor")
        intervalo2=n-1
        print("nuevo intervalo [", intervalo1, "-", intervalo2, "]")
    
    n=int(input("Ingresa el número magico, [{}-{}]:\n".format(intervalo1, intervalo2)))
    
    while n < intervalo1 or n > intervalo2:
        print("Ingresa el número magico")
        n=int(input("intervalo [", intervalo1, "-", intervalo2, "]"))
if n == nmagico:
    print("Fin")
