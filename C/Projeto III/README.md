# 🎯 Jogo da Adivinhação em C

Este é um simples jogo de adivinhação implementado em linguagem C, onde o jogador deve tentar descobrir um número aleatório entre 1 e 100.

## 🧠 Descrição do Funcionamento

O programa realiza os seguintes passos:

1. Define o uso de caracteres UTF-8 e a localidade para o português do Brasil.
2. Gera um número aleatório entre 1 e 100.
3. Solicita ao jogador que tente adivinhar o número.
4. A cada tentativa:
   - Informa se o número digitado é **muito alto** ou **muito baixo**.
   - Conta a quantidade de tentativas realizadas.
5. Finaliza o jogo quando o jogador acerta o número, mostrando o total de tentativas.

## 🧪 Exemplo de Execução

```
Jogo da Adivinhação  
Digite a sua tentativa de 1 a 100: 50  
Muito Alto!  
Você errou, digite novamente: 25  
Muito Baixo!  
Você errou, digite novamente: 38  
Você acertou! Número de tentativas: 3
```

## 📌 Recursos Utilizados

- `rand()` e `srand()` para geração de números aleatórios.
- `setlocale()` e `system("chcp 65001")` para suporte a acentuação.
- Estrutura de repetição `while` para controlar as tentativas.

## 👩‍💻 Autoria

Feito por **Anne Caroline Gonçalves de Mesquita** e **[Anna Nicolly da Silva](https://github.com/Annans95)**.
