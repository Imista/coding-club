# Escribe un programa que dado un numero, compruebe y muestre si es primo, fibonacci y par.

num = int(input("Ingresa un numero:\t"))

# Comprobar si es par
esPar = num % 2 == 0


# Comprobar si es primo
primos = []
esPrimo = True
for i in range(2, num):
    if (num % i == 0):
        esPrimo = False
        break

# Comprobar si es fibonacci
fibonaccis = [1, 1]
while (True):
    if (fibonaccis[-1] >= num):
        break
    fibonaccis.append(fibonaccis[-2] + fibonaccis[-1])
esFibonacci = (num in fibonaccis)

print("{} {}, {}, {}".format(num, ("es par" if esPar else "es impar"),
      ("es primo" if esPrimo else "no es primo"), ("es fibonacci" if esFibonacci else "no es fibonacci")))

print("Fibonaccis:\t", fibonaccis)
