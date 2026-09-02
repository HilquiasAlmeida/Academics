# ==========================================
# EXERCÍCIOS DE PYTHON - FIAP - ENGENHARIA DA COMPUTAÇÃO (1 a 9)
# Condicionais (if / elif / else)
# ==========================================

# 1. Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por km acima de 80km/h.
velocidade = float(input("Digite a velocidade do carro (km/h): "))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print("Você foi multado!")
    print(f"O valor da multa é: R$ {multa:.2f}")
else:
    print("Velocidade dentro do limite permitido. Boa viagem!")


# 2. Escreva um programa que leia três números e que imprima o maior e o menor.
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

maior = max(n1, n2, n3)
menor = min(n1, n2, n3)
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")


# 3. Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para inferiores ou iguais, de 15%.
salario = float(input("Digite o salário do funcionário: "))
if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
novo_salario = salario + aumento
print(f"O valor do aumento é: R$ {aumento:.2f}")
print(f"O novo salário é: R$ {novo_salario:.2f}")


# 4. Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.
distancia = float(input("Digite a distância da viagem em km: "))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f"O preço da passagem é: R$ {preco:.2f}")


# 5. Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular soma, subtração, multiplicação e divisão. Exiba o resultado da operação solicitada.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Escolha a operação (+, -, *, /): ")

if operacao == '+':
    resultado = num1 + num2
    print(f"Resultado: {resultado}")
elif operacao == '-':
    resultado = num1 - num2
    print(f"Resultado: {resultado}")
elif operacao == '*':
    resultado = num1 * num2
    print(f"Resultado: {resultado}")
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {resultado}")
    else:
        print("Erro: Não é possível dividir por zero.")
else:
    print("Operação inválida!")


# 6. Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário.
valor_casa = float(input("Digite o valor da casa a comprar: "))
salario_comprador = float(input("Digite o seu salário: "))
anos_pagar = int(input("Digite a quantidade de anos a pagar: "))

meses = anos_pagar * 12
prestacao = valor_casa / meses
limite_prestacao = salario_comprador * 0.30

print(f"Valor da prestação mensal: R$ {prestacao:.2f}")
if prestacao <= limite_prestacao:
    print("Empréstimo APROVADO!")
else:
    print("Empréstimo NEGADO! A prestação ultrapassa 30% do salário.")


# 7. Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios.
kwh = float(input("Digite a quantidade de kWh consumida: "))
tipo_instalacao = input("Digite o tipo de instalação (R - Residencial, C - Comercial, I - Industrial): ").upper()

preco_energia = 0
if tipo_instalacao == 'R':
    if kwh <= 500:
        preco_energia = kwh * 0.40
    else:
        preco_energia = kwh * 0.65
elif tipo_instalacao == 'C':
    if kwh <= 1000:
        preco_energia = kwh * 0.55
    else:
        preco_energia = kwh * 0.60
elif tipo_instalacao == 'I':
    if kwh <= 5000:
        preco_energia = kwh * 0.55
    else:
        preco_energia = kwh * 0.60
else:
    print("Tipo de instalação inválido!")
    preco_energia = None

if preco_energia is not None:
    print(f"O valor a pagar pelo fornecimento de energia é: R$ {preco_energia:.2f}")


# 8. Faça um programa que leia 2 notas de um aluno, calcule a média e imprima aprovado ou reprovado (para ser aprovado a média deve ser no mínimo 6).
n_nota1 = float(input("Digite a primeira nota: "))
n_nota2 = float(input("Digite a segunda nota: "))
media = (n_nota1 + n_nota2) / 2

print(f"Média: {media:.1f}")
if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")


# 9. Refaça o exercício 8, identificando o conceito aprovado (média superior ou igual a 6), exame (média maior ou igual a 4 e menor que 6) ou reprovado (média inferior a 4).
n_nota1 = float(input("Digite a primeira nota: "))
n_nota2 = float(input("Digite a segunda nota: "))
media = (n_nota1 + n_nota2) / 2

print(f"Média: {media:.1f}")
if media >= 6:
    print("Aprovado")
elif media >= 4:
    print("Exame")
else:
    print("Reprovado")
