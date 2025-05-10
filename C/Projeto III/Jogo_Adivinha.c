// feito por Anna Nicolly da Silva e Anne Caroline Gonçalves de Mesquita

#include <stdio.h> // para printf() e scanf()
#include <locale.h> // para aceitar acentos
#include <stdlib.h> // para rand() e srand()
#include <time.h> //para time
int main() {
    setlocale(LC_ALL, "pt_BR.UTF-8"); //para selecionar e aplicar a língua portuguesa
    system("chcp 65001"); // Ativa UTF-8 no terminal (acentos)

    int tentativa = 0; // define uma variável, nomeia ela e atribui valor
    int ct = 1; // começa do 1, porque já começa com 1 tentativa
    srand(time(NULL)); //Garante que gere números aleatórios diferentes. Nesse caso baseado no horário atual
    int numero = rand() % 100 + 1; //rand() vai gerar um número aleatório. Nesse caso um número de 1 a 100
    printf("Jogo da Adivinhação\n"); // imprimir na tela 
    printf("Digite a sua tentativa de 1 a 100:"); 
    scanf("%d", &tentativa); // lê dados digitados pelo usuário e armazena na variável

    while (tentativa != numero){ //estrutura de repetição
        if (tentativa > numero){ // condição
            printf("Muito Alto!\n");
        }
        else{ // caso if seja falso
            printf("Muito Baixo!\n");
        }
        printf("Você errou, digite novamente:");
        scanf("%d", &tentativa);
        ct++; //adiciona 1 à variável ct
    }
    printf("Você acertou! Número de tentativas: %d\n", ct);
    return 0; // returna 0, se o programa funcionar sem erros
}
