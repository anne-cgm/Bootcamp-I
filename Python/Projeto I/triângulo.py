a=float(input('Digite o comprimento da reta a:'))
b=float(input('Digite o comprimento da reta b:'))
c=float(input('Digite o comprimento da reta c:'))
triangulo=a+b>c and a+c>b and b+c>a
if triangulo and a==b==c:
    print('É um triângulo equilátero')
elif triangulo and (a==b or a==c or b==c):
    print('É um triângulo isóceles')
elif triangulo:
    print('É um triângulo escaleno')
else:
    print('Não é um triângulo')