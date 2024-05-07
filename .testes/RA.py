# 1) Escreva um algoritmo em Python para calcular a idade de
# alguém, sabendo-se seu ano de nascimento.

# ano_de_nascimento = int(input('Coloque o ano que você nasceu: '))

# def nascimento(ano):
#     nasceu_esse_ano = input('Você já fez aniversário? [S]im ou [N]ão\n')
    
#     if 's' in nasceu_esse_ano.lower():
#         print(f'Você tem {2024 - ano} anos')
#     elif 'n' in nasceu_esse_ano.lower():
#         print(f'Você tem {2023 - ano} anos')
#     else:
#         print('Você digitou algo errado')

# nascimento(ano_de_nascimento)

# 2) Escreva um algoritmo em Python para calcular o valor, em
# reais, que deve ser pago por um cliente de uma locadora de
# carros. Sabe-se que:
# • O valor de locação de cada carro é 100,00 reais;
# • O cliente pode locar um único carro por vários dias


# tempo_de_carro = int(input('Quantos dias você ficará com o carro: '))

# def locacao(tempo):
#     valor_a_se_pagar = tempo * 100
#     print(f'Você deve R${valor_a_se_pagar}')

# locacao(tempo_de_carro)

# 3) Leia do teclado a temperatura em Celsius e imprima o
# equivalente em Fahrenheit.

# celsius = int(input('Quantos graus celsius está: '))
# fahrenheit = celsius * 1.8 + 32
# print(f'Está {fahrenheit} farenheits')

# 4) Um cinema possui um programa de fidelidade que oferece descontos para os
# clientes mais assíduos. Implemente um programa em Python para calcular quanto
# alguém deve pagar pela entrada do cinema, sabendo-se:
# • Cada cliente pode comprar quantas entradas quiser;
# • O cliente deve apresentar no ato do pagamento sua carteira que informa qual é o seu
# desconto atual (0 a 100%);
# • O cliente poderá também descontar o valor do ticket do estacionamento no ato da
# compra.

# tickets = int(input('Quantos tickets você irá comprar: '))
# porcentagem_desconto = int(input('DIGITE SUA PORCENTAGEM DE DESCONTO: '))
# desconto = porcentagem_desconto / 100
# def pagamento(ticket, desconto):
#     valor_ticket = ((ticket * desconto) * 30)
#     estacionamento = input('Quer pagar o estacionamento: [S]/[N]\n')
#     if estacionamento == 'S'.lower():
#         print(f'O valor a se pagar é R${valor_ticket + 20}')
#     else:
#         print(f'O valor a se pagar é {valor_ticket}')
# pagamento(tickets, desconto)

# 5) Escreva um algoritmo capaz de imprimir na tela o número de minutos
# transcorridos entre duas medidas realizadas em um mesmo dia e lidas pelo teclado
# de acordo com o formato a seguir:

# def conversor_minutos(medida):
#     hora, minuto = map(int, medida.split(':'))
#     return hora * 60 + minuto

# m1 = input('Digite a hora e o minuto 1 (hora:minuto): ')
# m2 = input('Digite a hora e o minuto 2 (hora:minuto): ')

# hora1 = conversor_minutos(m1)
# hora2 = conversor_minutos(m2)

# diferença = hora1 - hora2

# print(f'A diferença é de {abs(diferença)} minutos')
