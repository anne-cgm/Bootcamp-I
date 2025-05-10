# Conversor de Temperatura: Fahrenheit para Celsius

Este script em Python converte um intervalo de temperaturas em Fahrenheit para Celsius e exibe os resultados em forma de tabela.

## 🧠 Lógica do Funcionamento

1. O programa solicita ao usuário dois valores inteiros:
   - Valor **inicial** (em Fahrenheit).
   - Valor **final** (em Fahrenheit).
2. Se o valor inicial for menor ou igual ao final, o intervalo é percorrido em ordem crescente.
   Caso contrário, é percorrido em ordem decrescente.
3. Para cada valor de Fahrenheit no intervalo, o programa converte para Celsius utilizando a fórmula:

\
°C = 5 * (f - 32) / 9


4. Os resultados são exibidos com formatação em colunas.

## 📄 Exemplo de Uso

```bash
Digite o valor inicial: 32
Digite o valor final: 36
Fahrenheit|Celsius
32.0°F    |0.000°C
33.0°F    |0.556°C
34.0°F    |1.111°C
35.0°F    |1.667°C
36.0°F    |2.222°C


