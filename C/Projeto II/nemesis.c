#include <stdio.h>
#include <string.h>
#include <locale.h>
int main (){
    setlocale(LC_ALL, "Portuguese" );
    char nome[20] = "augusto\0";
    printf("%s\n", nome);
    nome[0] = 'A';
    printf("%s", nome);
return 0;
}
