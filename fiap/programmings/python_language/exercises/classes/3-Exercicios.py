# 1. Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por km acima de 80km/h.

# Solicita a velocidade do carro
velocidade = float(input("Qual a velocidade atual do carro em km/h? "))

# Define o limite de velocidade
limite = 80

# Verifica se a velocidade ultrapassou o limite
if velocidade > limite:
    print("Você foi MULTADO! Ultrapassou o limite de 80km/h.")
    
    # Calcula o valor da multa (R$5 por cada km acima do limite)
    excesso = velocidade - limite
    multa = excesso * 5
    
    print(f"O valor da sua multa é de: R${multa:.2f}")
else:
    print("Velocidade dentro do limite. Boa viagem!")

# OU

# Entrada de dados
velocidade = float(input("Qual a velocidade atual do carro (km/h)? "))
distancia = float(input("Qual a distância do destino (km)? "))

limite = 80

# 1. Verificação da Multa
if velocidade > limite:
    excesso = velocidade - limite
    multa = excesso * 5
    print(f"\nALERTA: Você foi multado em R${multa:.2f} por excesso de velocidade!")
else:
    print("\nVelocidade dentro do limite permitido.")

# 2. Cálculo do Tempo de Viagem
if velocidade > 0:
    tempo_horas = distancia / velocidade
    
    # Convertendo para horas e minutos para ficar mais amigável
    horas = int(tempo_horas)
    minutos = int((tempo_horas - horas) * 60)
    
    print(f"Estimativa de viagem: {horas}h e {minutos}min para percorrer {distancia}km.")
else:
    print("Com o carro parado, você não chegará ao destino!")









# 2. Escreva um programa que leia três números e que imprima o maior e o menor.

# Lendo os três números
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

# Colocando os números em uma lista
numeros = [n1, n2, n3]

# Identificando o maior e o menor com funções prontas
maior = max(numeros)
minor = min(numeros)

print("-" * 30)
print(f"O maior número digitado foi: {maior}")
print(f"O menor número digitado foi: {minor}")

#ou

a = float(input("Primeiro valor: "))
b = float(input("Segundo valor: "))
c = float(input("Terceiro valor: "))

# Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f"O menor valor digitado foi {menor}")
print(f"O maior valor digitado foi {maior}")

# OU

numeros = []

print("--- ANALISADOR DE NÚMEROS INFINITO ---")
print("Digite os números que desejar. Para parar e ver o resultado, digite 'S'.")

while True:
    entrada = input("Digite um número (ou 'S' para sair): ").strip().upper()
    
    if entrada == 'S':
        break
    
    try:
        # Tenta converter a entrada para número e adiciona na lista
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida! Digite um número ou 'S'.")

# Verifica se a lista não está vazia antes de calcular
if numeros:
    maior = max(numeros)
    menor = min(numeros)
    quantidade = len(numeros)
    media = sum(numeros) / quantidade

    print("-" * 40)
    print(f"Você digitou {quantidade} números.")
    print(f"O maior valor foi: {maior}")
    print(f"O menor valor foi: {menor}")
    print(f"A média dos valores foi: {media:.2f}")
    print("-" * 40)
else:
    print("Nenhum número foi processado.")


# 3. Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para inferiores ou iguais, de 15%.

# Entrada de dados
salario = float(input("Digite o salário do funcionário: R$ "))

# Lógica do aumento
if salario > 1250:
    # Aumento de 10% (Multiplicar por 0.10)
    porcentagem = 10
    aumento = salario * 0.10
else:
    # Aumento de 15% (Multiplicar por 0.15)
    porcentagem = 15
    aumento = salario * 0.15




# 3. Cálculo do novo salário
novo_salario = salario + aumento

# 4. Exibição dos resultados
print("-" * 30)
print(f"Salário antigo: R${salario:.2f}")
print(f"Percentual aplicado: {porcentagem}%")
print(f"Valor do aumento: R${aumento:.2f}")
print(f"Novo salário: R${novo_salario:.2f}")
print("-" * 30)





# 4. Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.

# 1. Entrada de dados
distancia = float(input("Qual a distância da viagem em km? "))

# 2. Lógica de cálculo do preço
if distancia <= 200:
    preco_por_km = 0.50
else:
    preco_por_km = 0.45

# 3. Cálculo do valor total
preco_final = distancia * preco_por_km

# 4. Exibição do resultado
print("-" * 40)
print(f"Distância informada: {distancia} km")
print(f"Tarifa aplicada: R$ {preco_por_km:.2f} por km")
print(f"O preço total da passagem é: R$ {preco_final:.2f}")
print("-" * 40)


# 5. Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular soma, subtração, multiplicação e divisão. Exiba o resultado da operação solicitada.

# 1. Entrada de dados
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\nEscolha a operação:")
print("[+] Soma")
print("[-] Subtração")
print("[*] Multiplicação")
print("[/] Divisão")

operacao = input("\nQual operação deseja realizar? ")

# 2. Lógica de decisão
if operacao == '+':
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")

elif operacao == '-':
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")

elif operacao == '*':
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado}")

elif operacao == '/':
    # Verificação de segurança: não existe divisão por zero!
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")
    else:
        print("Erro: Não é possível dividir por zero!")

else:
    print("Operação inválida! Por favor, escolha +, -, * ou /.")





# 6. Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

# 1. Entrada de dados
valor_casa = float(input("Qual o valor da casa a comprar? R$ "))
salario = float(input("Qual o seu salário mensal? R$ "))
anos_pagar = int(input("Em quantos anos pretende pagar? "))

# 2. Cálculos iniciais
# Transformamos anos em meses para achar a prestação
meses = anos_pagar * 12
prestacao = valor_casa / meses

# Calculamos o limite de 30% do salário
limite_salario = salario * 0.30

# 3. Verificação do empréstimo
print("\n" + "="*30)
print(f"Valor da prestação: R$ {prestacao:.2f}")
print(f"Limite de 30% do salário: R$ {limite_salario:.2f}")
print("="*30)

if prestacao <= limite_salario:
    print("✅ EMPRÉSTIMO APROVADO!")
    print(f"Você pagará a casa em {meses} meses.")
else:
    print("❌ EMPRÉSTIMO NEGADO!")
    print("O valor da prestação excede 30% do seu salário mensal.")

# ou

# 1. Entrada de dados
valor_casa = float(input("Qual o valor da casa a comprar? R$ "))
salario = float(input("Qual o seu salário mensal? R$ "))
anos_pagar = int(input("Em quantos anos pretende pagar? "))
taxa_anual = float(input("Qual a taxa de juros anual (em %)? ")) / 100

# 2. Cálculos Financeiros
meses = anos_pagar * 12
taxa_mensal = (1 + taxa_anual)**(1/12) - 1 # Ajuste de taxa anual para mensal
montante_total = valor_casa * (1 + taxa_mensal)**meses
prestacao = montante_total / meses
limite_salario = salario * 0.30

# 3. Verificação do empréstimo
print("\n" + "="*40)
print(f"Total a pagar com juros: R$ {montante_total:.2f}")
print(f"Prestação mensal calculada: R$ {prestacao:.2f}")
print(f"Limite de 30% do seu salário: R$ {limite_salario:.2f}")
print("="*40)

if prestacao <= limite_salario:
    print("✅ EMPRÉSTIMO APROVADO!")
else:
    print("❌ EMPRÉSTIMO NEGADO!")
    print("A prestação mensal excede 30% do seu salário.")

# ou
# (Mantemos as variáveis anteriores de valor_casa, salario, taxa_anual, meses)
# ... [código anterior para entrada e cálculo da prestação]

print(f"\n{'Mês':<6} | {'Prestação':<12} | {'Juros':<10} | {'Amortização':<12} | {'Saldo Devedor':<15}")
print("-" * 65)

saldo_devedor = montante_total # (ou valor original, dependendo do sistema)
# Nota: Para o sistema Price, a prestação é constante
for mes in range(1, meses + 1):
    juros_mes = saldo_devedor * taxa_mensal
    amortizacao_mes = prestacao - juros_mes
    saldo_devedor -= amortizacao_mes
    
    # Exibe apenas os primeiros 12 meses para não encher a tela
    if mes <= 12:
        print(f"{mes:<6} | R$ {prestacao:>8.2f} | R$ {juros_mes:>6.2f} | R$ {amortizacao_mes:>8.2f} | R$ {max(0, saldo_devedor):>12.2f}")

print("-" * 65)
print("... (Tabela truncada nos primeiros 12 meses)")

# ou 

# Supondo as variáveis: valor_casa, meses, taxa_mensal, prestacao
# Calculamos o total pago no cenário comum
total_pago_comum = prestacao * meses
total_juros_comum = total_pago_comum - valor_casa

# Cenário com extra de R$ 500
extra = 500.00
saldo_devedor_extra = valor_casa
total_pago_extra = 0
meses_extra = 0

while saldo_devedor_extra > 0:
    juros = saldo_devedor_extra * taxa_mensal
    pagamento_total = prestacao + extra
    
    # Se o saldo for menor que o pagamento, ajusta o último pagamento
    if saldo_devedor_extra + juros < pagamento_total:
        pagamento_total = saldo_devedor_extra + juros
        
    amortizacao = pagamento_total - juros
    saldo_devedor_extra -= amortizacao
    total_pago_extra += pagamento_total
    meses_extra += 1

print("-" * 40)
print(f"CENÁRIO SEM EXTRA:")
print(f"Total pago: R$ {total_pago_comum:.2f}")
print(f"Meses totais: {meses}")
print("-" * 40)
print(f"CENÁRIO COM R$ 500 EXTRA/MÊS:")
print(f"Total pago: R$ {total_pago_extra:.2f}")
print(f"Meses totais: {meses_extra}")
print(f"Economia total: R$ {total_pago_comum - total_pago_extra:.2f}")
print("-" * 40)


# 7. Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.

# 1. Entrada de dados
consumo = float(input("Quantidade de kWh consumida: "))
tipo = input("Tipo de instalação (R para Residencial, C para Comercial, I para Industrial): ").upper()

preco = 0

# 2. Lógica de cálculo conforme tipo e consumo
if tipo == 'R':
    if consumo <= 500:
        preco = 0.40
    else:
        preco = 0.65
        
elif tipo == 'C':
    if consumo <= 1000:
        preco = 0.55
    else:
        preco = 0.60
        
elif tipo == 'I':
    if consumo <= 5000:
        preco = 0.55
    else:
        preco = 0.60
else:
    print("Erro: Tipo de instalação inválido.")
    preco = 0

# 3. Exibição do resultado
if preco > 0:
    valor_a_pagar = consumo * preco
    print(f"\nTipo de instalação: {tipo}")
    print(f"Consumo: {consumo} kWh")
    print(f"Preço por kWh: R$ {preco:.2f}")
    print(f"Total a pagar: R$ {valor_a_pagar:.2f}")

# ou

# 1. Entrada de dados
consumo = float(input("Quantidade de kWh consumida: "))
tipo = input("Tipo de instalação (R, C ou I): ").upper()

# 2. Definição do preço por kWh
preco = 0
if tipo == 'R':
    preco = 0.40 if consumo <= 500 else 0.65
elif tipo == 'C':
    preco = 0.55 if consumo <= 1000 else 0.60
elif tipo == 'I':
    preco = 0.55 if consumo <= 5000 else 0.60
else:
    print("Tipo inválido.")
    preco = 0

# 3. Cálculo com ICMS
if preco > 0:
    subtotal = consumo * preco
    aliquota_icms = 0.18
    valor_icms = subtotal * aliquota_icms
    total_a_pagar = subtotal + valor_icms
    
    print(f"\n--- Detalhamento da Conta ---")
    print(f"Consumo: {consumo} kWh")
    print(f"Preço Base: R$ {subtotal:.2f}")
    print(f"ICMS (18%): R$ {valor_icms:.2f}")
    print(f"TOTAL A PAGAR: R$ {total_a_pagar:.2f}")

# ou

# (Mantendo a lógica de cálculo anterior)
# ... [Após calcular o total_a_pagar]

# 3. Cálculo de Desconto por Pontualidade
# Se pagar antes do vencimento, ganha 5% de desconto
desconto = total_a_pagar * 0.05
total_com_desconto = total_a_pagar - desconto

print(f"\n--- Detalhamento da Conta ---")
print(f"Total a pagar (valor integral): R$ {total_a_pagar:.2f}")
print("-" * 30)
print(f"Valor com 5% de desconto (pagamento em dia): R$ {total_com_desconto:.2f}")
print(f"Economia total: R$ {desconto:.2f}")

# 8. Faça um programa que leia 2 notas de um aluno, calcule a média e imprima aprovado ou reprovado (para ser aprovado a média deve ser no mínimo 6).

# 1. Entrada de dados
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# 2. Cálculo da média
media = (nota1 + nota2) / 2

# 3. Verificação de status
print("-" * 30)
print(f"Sua média foi: {media:.1f}")

if media >= 6:
    print("Resultado: APROVADO! Parabéns!")
else:
    print("Resultado: REPROVADO. Estude mais para a próxima!")
print("-" * 30)

# ou

# 1. Entrada das notas iniciais
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# 2. Cálculo da primeira média
media = (nota1 + nota2) / 2
print(f"\nSua média parcial é: {media:.1f}")

# 3. Verificação de status
if media >= 6:
    print("Resultado: APROVADO! Parabéns!")
else:
    print("Você ficou abaixo da média e precisará fazer a recuperação.")
    nota_recuperacao = float(input("Digite a nota da recuperação: "))
    
    # Nova média (calculada substituindo a menor nota ou média simples, aqui usaremos média simples)
    media_final = (media + nota_recuperacao) / 2
    
    print(f"Sua média final após a recuperação é: {media_final:.1f}")
    
    if media_final >= 6:
        print("Resultado: APROVADO após recuperação!")
    else:
        print("Resultado: REPROVADO. Sinto muito.")

print("-" * 30)

# ou
# 1. Entrada das notas originais
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# 2. Cálculo da média original
media = (nota1 + nota2) / 2
print(f"\nSua média original é: {media:.1f}")

# 3. Verificação de status
if media >= 6:
    print("Resultado: APROVADO! Parabéns!")
else:
    print("Você ficou abaixo da média e precisará fazer a recuperação.")
    nota_rec = float(input("Digite a nota da prova de recuperação: "))
    
    # Lógica de substituição da menor nota
    if nota1 < nota2:
        nota1 = nota_rec
    else:
        nota2 = nota_rec
    
    # Recalculando a média com a nota substituída
    nova_media = (nota1 + nota2) / 2
    
    print(f"Nova média após substituição: {nova_media:.1f}")
    
    if nova_media >= 6:
        print("Resultado: APROVADO após recuperação!")
    else:
        print("Resultado: REPROVADO.")

# ou

# 1. Definindo a quantidade de provas
qtd_provas = int(input("Quantas provas foram feitas no semestre? "))
notas = []

# 2. Coletando todas as notas
for i in range(qtd_provas):
    nota = float(input(f"Digite a nota da {i+1}ª prova: "))
    notas.append(nota)

# 3. Cálculo da média original
media = sum(notas) / len(notas)
print(f"\nSua média original é: {media:.1f}")

# 4. Verificação de status e lógica de substituição
if media >= 6:
    print("Resultado: APROVADO! Parabéns!")
else:
    print("Você está abaixo da média. Vamos calcular com a nota de recuperação.")
    
    # Identifica a pior nota e a substitui
    pior_nota = min(notas)
    nota_rec = float(input(f"Digite a nota da prova de recuperação (que substituirá seu {pior_nota}): "))
    
    # Remove a pior nota e insere a nova
    notas.remove(pior_nota)
    notas.append(nota_rec)
    
    # Recalcula a média
    nova_media = sum(notas) / len(notas)
    
    print(f"\nNova média após substituir a nota {pior_nota} por {nota_rec}: {nova_media:.1f}")
    
    if nova_media >= 6:
        print("Resultado: APROVADO após recuperação!")
    else:
        print("Resultado: REPROVADO.")


# 9. Refaça o exercício 8, identificando o conceito aprovado (média superior ou igual a 6), exame (média maior ou igual a 4 e menor que 6) ou reprovado (média inferior a 4).

# 1. Entrada de dados
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# 2. Cálculo da média
media = (nota1 + nota2) / 2
print(f"\nSua média é: {media:.1f}")

# 3. Verificação de status
if media >= 6:
    print("Resultado: APROVADO!")
elif media >= 4:
    # Como já passamos pelo teste do "if media >= 6", 
    # se o código chegou aqui, significa que a média é < 6.
    # Logo, este bloco cobre o intervalo de 4 a 5.9
    print("Resultado: EM EXAME!")
else:
    # Se não for aprovado nem estiver em exame, está abaixo de 4
    print("Resultado: REPROVADO.")

# OU

# 1. Entrada de dados
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# 2. Cálculo da média
media = (nota1 + nota2) / 2
print(f"\nSua média é: {media:.1f}")

# 3. Verificação de status e cálculo da necessidade
if media >= 6:
    print("Resultado: APROVADO!")
elif media >= 4:
    # Cálculo: para média 6, a soma das duas notas deve ser 12
    necessaria = 12 - media
    print(f"Resultado: EM EXAME.")
    print(f"Você precisa tirar pelo menos {necessaria:.1f} no exame final para ser aprovado.")
else:
    print("Resultado: REPROVADO.")

# ou

# 1. Entrada da média parcial atual
media_parcial = float(input("Digite sua média parcial: "))

if media_parcial >= 6:
    print("Você já está aprovado!")
elif media_parcial < 4:
    print("Sua média é muito baixa, você foi reprovado.")
else:
    print(f"Você está em exame. Sua média é {media_parcial:.1f}.")
    print("--- SIMULADOR DE NOTAS ---")
    print("Digite '-1' a qualquer momento para sair do simulador.")
    
    while True:
        nota_teste = float(input("\nQual nota você acha que tiraria no exame? (0 a 10): "))
        
        if nota_teste == -1:
            print("Saindo do simulador...")
            break
            
        # Cálculo da média final considerando que a parcial e o exame têm o mesmo peso
        media_final = (media_parcial + nota_teste) / 2
        
        if media_final >= 6:
            print(f"Com {nota_teste:.1f}, sua média final seria {media_final:.1f}. ✅ APROVADO!")
        else:
            print(f"Com {nota_teste:.1f}, sua média final seria {media_final:.1f}. ❌ AINDA REPROVADO.")
            necessaria = 12 - media_parcial
            print(f"Você ainda precisa de pelo menos {necessaria:.1f} para passar.")

# OU

import matplotlib.pyplot as plt
import numpy as np

# Dados: Média parcial atual (supondo 4.5 como exemplo)
media_parcial = 4.5
notas_exame = np.linspace(0, 10, 11)  # Notas de 0 a 10
medias_finais = (media_parcial + notas_exame) / 2

# Criando o gráfico
plt.figure(figsize=(8, 5))
plt.plot(notas_exame, medias_finais, marker='o', label='Média Final')
plt.axhline(y=6, color='r', linestyle='--', label='Nota de Aprovação (6.0)')

# Detalhes visuais
plt.title(f'Simulação de Média Final (Parcial: {media_parcial})')
plt.xlabel('Nota no Exame')
plt.ylabel('Média Final')
plt.grid(True)
plt.legend()
plt.show()

# ou 

import matplotlib.pyplot as plt
import numpy as np

# Dados: Lista de matérias e médias atuais
materias = ['Matemática', 'História', 'Física', 'Português', 'Química']
medias_atuais = [4.5, 7.2, 5.0, 6.5, 3.8]
meta = 6.0

# Cálculo da diferença para a meta
diferenca = [meta - m for m in medias_atuais]

# Configuração do Gráfico
x = np.arange(len(materias))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
barras_atuais = ax.bar(x - width/2, medias_atuais, width, label='Média Atual', color='skyblue')
barras_meta = ax.bar(x + width/2, [meta]*len(materias), width, label='Meta (Aprovação)', color='salmon', alpha=0.6)

# Adicionando rótulos
ax.set_ylabel('Notas')
ax.set_title('Dashboard de Desempenho Acadêmico')
ax.set_xticks(x)
ax.set_xticklabels(materias)
ax.legend()

plt.axhline(y=meta, color='gray', linestyle='--', linewidth=0.8)
plt.show()

# ou

import matplotlib.pyplot as plt
import numpy as np

# Dados iniciais
materias = ['Matemática', 'História', 'Física', 'Português', 'Química']
medias = [4.5, 7.2, 3.5, 6.5, 3.8] # Note que Matemática e Química estão abaixo de 4
meta = 6.0

# Lógica de cores: Vermelho se < 4.0, Laranja se < 6.0, Azul se >= 6.0
cores = []
for m in medias:
    if m < 4.0:
        cores.append('red')
        print(f"⚠️ ALERTA: Risco iminente de reprovação em {materias[medias.index(m)]}!")
    elif m < 6.0:
        cores.append('orange')
    else:
        cores.append('skyblue')

# Gerando o gráfico
plt.figure(figsize=(10, 6))
plt.bar(materias, medias, color=cores)
plt.axhline(y=meta, color='green', linestyle='--', label='Meta (Aprovação)')
plt.axhline(y=4.0, color='red', linestyle=':', label='Risco Crítico (<4.0)')

plt.title('Dashboard de Desempenho com Alerta de Risco')
plt.ylabel('Média')
plt.legend()
plt.show()

# ou

# Dados das matérias em risco
materias_risco = ['Matemática', 'Química']
medias = [4.5, 3.8]
dias_para_prova = 10
fator_complexidade = [4, 5] # 1 (fácil) a 5 (difícil)

print(f"--- PLANEJAMENTO DE ESTUDOS (Para {dias_para_prova} dias) ---")

for i in range(len(materias_risco)):
    nota_necessaria = 6.0 - medias[i]
    # Cálculo hipotético: 1 hora de estudo por dia para cada 0.5 ponto necessário, 
    # ajustado pela complexidade
    horas_totais = (nota_necessaria / 0.5) * (fator_complexidade[i] / 2)
    horas_por_dia = horas_totais / dias_para_prova
    
    print(f"\nMatéria: {materias_risco[i]}")
    print(f"  > Nota necessária: {nota_necessaria:.1f}")
    print(f"  > Carga horária recomendada: {horas_por_dia:.2f} horas/dia")

# ou

# Dados iniciais
materia = "Química"
horas_totais_necessarias = 15.0 # Total calculado anteriormente
dias_restantes = 10

def atualizar_progresso(horas_estudadas_hoje, metas_restantes, dias_restantes):
    horas_pendentes = metas_restantes - horas_estudadas_hoje
    dias_restantes -= 1
    
    if dias_restantes > 0:
        nova_meta = horas_pendentes / dias_restantes
        return nova_meta, dias_restantes
    return 0, 0

# Simulação de um dia de estudo
print(f"Meta inicial para {materia}: {horas_totais_necessarias/dias_restantes:.2f} h/dia")
horas_hoje = float(input(f"Quantas horas você estudou {materia} hoje? "))

meta_nova, dias_novos = atualizar_progresso(horas_hoje, horas_totais_necessarias, dias_restantes)

print("-" * 40)
print(f"Progresso atualizado!")
print(f"Meta para os próximos {dias_novos} dias: {meta_nova:.2f} h/dia")
print("-" * 40)

# ou Sistema de Gestão Acadêmica Integrado

def menu():
    print("\n--- SISTEMA DE GESTÃO ACADÊMICA ---")
    print("1. Simulador de Médias e Notas Necessárias")
    print("2. Dashboard de Desempenho com Alertas")
    print("3. Calculadora de Carga Horária e Checklist")
    print("4. Sair")
    return input("Escolha uma opção: ")

# Loop principal do programa
while True:
    opcao = menu()
    
    if opcao == '1':
        # [Chama a lógica de cálculo de média e exame]
        print("Executando Simulador...")
    elif opcao == '2':
        # [Chama o dashboard com alertas de risco]
        print("Gerando Dashboard...")
    elif opcao == '3':
        # [Chama a calculadora de horas e checklist]
        print("Iniciando Checklist...")
    elif opcao == '4':
        print("Saindo do sistema. Bons estudos!")
        break
    else:
        print("Opção inválida!")