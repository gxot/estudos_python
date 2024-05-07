def decibin(num):
    if num >= 1:
        decibin(num // 2)
    print(num % 2, end = '')


def decihexa(num):
    tabela_numeros = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}
    if num >= 16:
        decihexa(num//16)
    print(tabela_numeros[num % 16], end='')


def bindeci(num):
    resultado = 0
    iter = str(num)
    for i, numero in (enumerate(reversed(iter))):
        desiter = int(numero)
        resultado += desiter * 2**i
    print(resultado)


def binhexa(num):
    bintohex = {"0000": "0","0001": "1","0010": "2","0011": "3","0100": "4",
                "0101": "5","0110": "6","0111": "7","1000": "8","1001": "9",
                "1010": "A","1011": "B","1100": "C","1101": "D","1110": "E",
                "1111": "F"}
    
    num_str = str(num)

    zeros_a_adicionar = (4 - len(num_str) % 4)
    final = num_str.zfill(len(num_str) + zeros_a_adicionar)

    grupos_4 = [final[i:i+4] for i in range(0, len(final), 4)]
    grupos_str = "".join(map(str, grupos_4))

    resultado = ''
    contador = 0
    contador_grupo = 0
    guardar = ''
    while True:
        for i in grupos_str:
            resultado += i
            contador += 1
            if contador == 4:
                guardar += bintohex[resultado]
                resultado = ''
                contador = 0
                contador_grupo += 1
                if contador_grupo == len(grupos_4):
                    print(guardar)
                    exit()
                continue
            

def hexadeci(num):   
    hextodeci = {
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
    "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "A": 10, "B": 11, "C": 12, "D": 13, "E": 14,
    "F": 15}

    resultado = 0
    iter = str(num)
    for i, hexa in (enumerate(reversed(iter))):
        simbolo = hextodeci[hexa]
        resultado += simbolo * 16**i
    print(resultado)


def hexabin(num):
    hextobin = {
    "0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100",
    "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001",
    "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110",
    "F": "1111"}
    resultado = ''
    for i in num:
        resultado += hextobin[i]
    print(resultado)    
    

def menu():
    print('1. Decimal -> Binário')
    print('2. Decimal -> Hexadecimal')
    print('3. Binário -> Decimal')
    print('4. Binário -> Hexadecimal')
    print('5. Hexadecimal -> Decimal')
    print('6. Hexadecimal -> Binário')
    escolha = int(input('Qual você escolhe? '))

    if escolha == 1:
        decibin(int(input('\nQual número deseja transformar em Binário? ')))
    if escolha == 2:
        decihexa(int(input('\nQual número deseja transformar em Hexadecimal? ')))
    if escolha == 3:
        bindeci(int(input('\nQual número deseja transformar em Decimal? ')))
    if escolha == 4:
        binhexa(int(input('\nQual número deseja transformar em Hexadecimal? ')))
    if escolha == 5:
        hexadeci(input('\nQual número deseja transformar em Decimal? '))
    if escolha == 6:
        hexabin(input('\nQual número deseja transformar em Binário? '))

menu()