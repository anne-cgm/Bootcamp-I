#include <stdio.h>
#include <locale.h>

int main (){
    setlocale(LC_ALL, "Portuguese" );
    int valor[3];
    printf("Digite o primeiro valor:");
    scanf("%d", &valor[0]);
    printf("Digite o segundo valor:");
    scanf("%d", &valor[1]);
    printf("Digite o valor terceiro valor:");
    scanf("%d", &valor[2]);
printf("Os valores digitados foram:%d,%d,%d", valor[0], valor[1], valor[2]);
return 0;
}
