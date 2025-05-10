inicial=int(input('Digite o valor inicial:'))
final=int(input('Digite o valor final:'))
print('Fahrenheit|Celsius')
if inicial<=final:
    for f in range(inicial,final+1,1):
        c = 5 * (f - 32) / 9
        print (f'{f:.1f}', end='°F    |',)
        print (f'{c:.3f}°C')
else:
    for f in range(inicial,final-1,-1):
        c = 5 * (f - 32) / 9
        print(f'{f:.1f}', end='°F    |', ) 
        print(f'{c:.3f}°C')