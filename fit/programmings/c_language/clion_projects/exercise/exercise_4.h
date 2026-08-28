//
  Exercício 4 
    Enunciado: Ler uma quantidade de chuva em polegadas 
      e imprimir a equivalente em milímetros (polegada = $25,4$ milímetros).
//

#include <stdio.h>

int main() {
    float polegadas, milimetros;

    printf("Digite a quantidade de chuva em polegadas: ");
    scanf("%f", &polegadas);

    // Converte polegadas para milímetros (1 polegada = 25.4 mm)
    milimetros = polegadas * 25.4;

    printf("A quantidade de chuva em milimetros e: %.2f mm\n", milimetros);

    return 0;
}
