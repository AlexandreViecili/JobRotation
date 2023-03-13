frase = str(input('Digite uma frase: ')).strip()
letras = len(frase) - 1
while letras >= 0:
    print(frase[letras], end='')
    letras -= 1
