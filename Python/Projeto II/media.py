print('Digite 0 para sair')
par=0
somap=0
impar=0
somai=0
while True:
    valor=int(input('Digite um valor:'))
    if valor==0:
        break
    if valor % 2==0:
        par=par+1
        somap=somap+valor
    else:
        impar=impar+1
        somai=somai+valor
mediap=somap/par
mediai=somai/impar
print('Média dos valores pares:', mediap)
print('Média dos valores ímpares:',mediai)