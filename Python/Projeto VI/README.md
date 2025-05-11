# 📏 Análise de Altura e Gênero

Este programa em Python coleta informações sobre a **altura** e o **gênero** de diferentes pessoas, determinando estatísticas simples como a maior e menor altura, além do total de homens e mulheres registrados.

## 🧠 Como Funciona

1. O programa solicita repetidamente que o usuário digite:
   - Seu gênero (`feminino` ou `masculino`);
   - Sua altura (em metros).
2. O loop continua até que o usuário digite `0` como altura.
3. Durante a coleta:
   - Armazena a maior e a menor altura inseridas;
   - Conta quantas pessoas do gênero feminino e masculino foram registradas.
4. Ao final, exibe:
   - A maior altura;
   - A menor altura;
   - A quantidade de mulheres;
   - A quantidade de homens.

## 🧪 Exemplo de Execução

```
Digite [0] para sair  
Digite seu gênero (feminino ou masculino): feminino  
Digite sua altura: 1.65  
Digite seu gênero (feminino ou masculino): masculino  
Digite sua altura: 1.80  
Digite seu gênero (feminino ou masculino): feminino  
Digite sua altura: 1.55  
Digite seu gênero (feminino ou masculino): masculino  
Digite sua altura: 0  

Maior altura do grupo: 1.8  
Menor altura do grupo: 1.55  
Quantidade de mulheres do grupo: 2  
Quantidade de homens do grupo: 1
```

## ⚠️ Observações

- O código inicia com valores extremos para garantir que qualquer altura digitada seja válida para comparação.
- A condição de parada é a entrada da altura `0`.


## ✨ Melhorias Aplicadas

Uma versão aprimorada do código foi implementada com os seguintes ajustes:

- **Padronização de entrada de gênero** com .lower(), permitindo digitação flexível como FEMININO, feminino, Feminino, etc.
- **Validação de dados:** O programa agora verifica se o gênero informado é válido antes de continuar.
- **Contador de registros válidos (ct)** adicionado para garantir que os resultados só sejam exibidos se houver entrada válida. 
- **Organização e clareza** no código, utilizando boas práticas de indentação, nomes de variáveis mais claros e estrutura mais robusta. 

Essas mudanças tornam o programa mais confiável, fácil de usar e pronto para ser utilizando em testes com múltiplos usuários.






