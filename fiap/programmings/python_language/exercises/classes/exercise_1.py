# ==========================================
# EXERCÍCIOS 1 DE PYTHON - FIAP - ENGENHARIA DA COMPUTAÇÃO
# ==========================================

# 1. Faça um programa que exiba seu nome na tela.
# R: Definindo o nome em uma variável e exibindo-o
nome = "Seu Nome Aqui"
print(nome)


# 2. Escreva um programa que exiba o resultado de 2a x 3b, em que a vale 3 e b vale 5.
# R:
a = 3
b = 5

# Calculando a expressão (2 * a) * (3 * b)
resultado = (2 * a) * (3 * b)

# Exibindo o resultado na tela
print("O resultado de 2a x 3b é:", resultado)
# Explicação: 2a vira 2 * 3 = 6 | 3b vira 3 * 5 = 15 | O produto final é 6 * 15 = 90.


# 3. Escreva um programa que calcule a soma de três variáveis e imprima o resultado na tela.
# R:
num1 = 10
num2 = 25
num3 = 15

# Calculando a soma
soma = num1 + num2 + num3

# Exibindo o resultado na tela
print("A soma das três variáveis é:", soma)
# Como funciona: Criamos três variáveis, somamos com '+' e usamos print().


# 4. Faça um programa que peça dois números inteiros. Imprima a soma desses dois números na tela.
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
soma = num1 + num2
print("A soma é:", soma)


# 5. Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.
metros = float(input("Digite o valor em metros: "))
milimetros = metros * 1000
print(f"{metros} metros equivalem a {milimetros} milímetros.")


# 6. Escreva um programa que leia a quantidade de dias, horas, minutos e segundos. Calcule o total em segundos.
dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))
total_segundos = (dias * 24 * 3600) + (horas * 3600) + (minutos * 60) + segundos
print("O total em segundos é:", total_segundos)


# 7. Faça um programa que calcule o aumento de um salário. Solicite salário e porcentagem de aumento.
salario = float(input("Digite o valor do salário: "))
porcentagem = float(input("Digite a porcentagem do aumento: "))
aumento = salario * (porcentagem / 100)
novo_salario = salario + aumento
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")


# 8. Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
preco = float(input("Digite o preço da mercadoria: "))
desconto_perc = float(input("Digite o percentual de desconto: "))
valor_desconto = preco * (desconto_perc / 100)
preco_pagar = preco - valor_desconto
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço a pagar: R$ {preco_pagar:.2f}")


# 9. Escreva um programa que calcule o tempo de uma viagem de carro (distância e velocidade média).
distancia = float(input("Digite a distância a percorrer (km): "))
velocidade = float(input("Digite a velocidade média esperada (km/h): "))
tempo = distancia / velocidade
print(f"O tempo estimado da viagem é de {tempo:.2f} horas.")


# 10. Escreva um programa que converta temperatura em °C em °F. Fórmula: F = ((9 x C) / 5) + 32
celsius = float(input("Digite a temperatura em °C: "))
fahrenheit = ((9 * celsius) / 5) + 32
print(f"A temperatura em Fahrenheit é: {fahrenheit:.1f}°F")


# 11. Preço a pagar por carro alugado (R$60 por dia e R$0,15 por km rodado).
dias_alugado = int(input("Quantidade de dias que o carro foi alugado: "))
km_percorridos = float(input("Quantidade de km percorridos: "))
preco_total = (dias_alugado * 60) + (km_percorridos * 0.15)
print(f"O preço total a pagar é: R$ {preco_total:.2f}")


# 12. Escreva um programa que receba 2 valores inteiros x e y, e calcule z = (x^2 + y^2) / (x - y)^2
x = int(input("Digite o valor inteiro de x: "))
y = int(input("Digite o valor inteiro de y: "))
z = (x**2 + y**2) / (x - y)**2
print("O valor de z é:", z)


# 13. Escreva um programa que receba o salário de um funcionário (float) e retorne o novo salário com reajuste de 35%.
salario_atual = float(input("Digite o salário do funcionário: "))
novo_salario_35 = salario_atual * 1.35
print(f"O novo salário com 35% de reajuste é: R$ {novo_salario_35:.2f}")
