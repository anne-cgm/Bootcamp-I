def idade(ano):
    calculo=2025-ano
    return calculo
if __name__=='__main__':
    nascimento=int(input('Digite seu ano de nascimento:'))
    resultado=idade(nascimento)
    print(resultado,'anos')