print('Digite [0] para sair')
ct=0
menor = 3
maior = 0
f = 0
m = 0

while True:
    genero = input('Digite seu gênero (feminino ou masculino): ').lower() # utilizado para transformar todas as letras de uma string em minúsculas
    if genero == '0':
        break
    if genero not in ['feminino', 'masculino']:
        print("Gênero inválido! Digite 'feminino' ou 'masculino'.")
        continue

    altura = float(input('Digite sua altura: '))
    if altura == 0:
        break

    if altura < menor:
        menor = altura
    if altura > maior:
        maior = altura

    if genero == 'feminino':
        f += 1
    elif genero == 'masculino':
        m += 1
    ct = ct + 1

if ct>0:
    print('Maior altura do grupo:', maior)
    print('Menor altura do grupo:', menor)
    print('Quantidade de mulheres do grupo:', f)
    print('Quantidade de homens do grupo:', m)

