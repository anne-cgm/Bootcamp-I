#Código que tem problema
print('Digite [0] para sair')
menor=999999999
maior=-999999999
altura=0
f=0
m=0
while True:
    genero=str(input('Digite seu gênero (feminino ou masculino):'))
    altura=float(input('Digite sua altura:'))
    if altura == 0:
        break
    if altura < menor:
        menor=altura
    if altura > maior:
        maior=altura
    if genero == 'feminino':
        f=f+1
    if genero == 'masculino':
        m=m+1
print('Maior altura do grupo:',maior)
print('Menor altura do grupo:', menor)
print('Quantidade de mulheres do grupo:', f)
print('Quantidade de homens do grupo:', m)

