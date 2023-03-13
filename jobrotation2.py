numero = int(input('Digite um número: '))
n1 = 0
n2 = 1
print(f'{n1} -> {n2}', end='')
c = 3
while c <= numero:
    n3 = n1 + n2
    print(f' -> {n3}', end='')
    n1 = n2
    n2 = n3
    c += 1
    if n3 >= numero:
        break
if n3 == numero:
    print('\nO número pertence a sequência de Fibonacci.')
else:
    print('\nO número NÃO pertence a sequência de Fibonacci.')
