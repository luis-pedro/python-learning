#Gere código Python que crie uma lista com os números entre 1 e 100 e então imprima os números pares, mas somente se o número for divisível por 4.

numeros01 = list(range(1, 101))

for n in numeros01:
    if n % 2 == 0 and n % 4 == 0:
        print(n)

#Gere código Python que crie uma lista com os números entre 1 e 100 e então imprima os números pares, mas somente se o número for divisível por 4, usando list comprehension.

numeros02 = list(range(1, 101))
pares_divisiveis_por_4 = [n for n in numeros02 if n % 2 == 0 and n % 4 == 0]
print(pares_divisiveis_por_4)