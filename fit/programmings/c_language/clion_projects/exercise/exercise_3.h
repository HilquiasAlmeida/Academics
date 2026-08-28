//
  Exercício 3 
          Enunciado: Ler a temperatura na escala Celsius e imprimir a equivalente em Fahrenheit 
          (fórmula: $F = 9/5 * C + 32$).
//

#include <stdio.h>
int main() {
    float celsius, fahrenheit;

    printf("Digite a temperatura em graus Celsius: ");
    scanf("%f", &celsius);

    // Converte para Fahrenheit (utiliza 9.0 / 5.0 para evitar divisão inteira)
    fahrenheit = (9.0 / 5.0) * celsius + 32;

    printf("A temperatura equivalente em Fahrenheit e: %.2f °F\n", fahrenheit);

    return 0;
}
