### IMPORTS ###
import random

#### SUBALGORITMOS ####

def menu_captcha():
    print("=" * 40)
    print('     CAPTCHA     ')
    print()
    print('0 - ENCERRAR O PROGRAMA ')
    print('1 - Captcha de 10 caracteres')
    print('2 - Captcha com quantidade maxima de caracteres')
    print('3 - Captcha com quantidade maxima e tipo de caracteres')
    print('4 - Criar lista com 10 captchas com quantidade maxima e tipo de caracteres')
    print('5 - Escrever 20 captchas num arquivo de texto')

def menu_caracteres():
    print("Tipos de caracteres:")
    print("(L)etras maiúsculas")
    print("(l)etras minúsculas")
    print("(n)úmeros")
    print("(e)speciais")

def gerarCaptcha(c, n):
    print()
    captcha = "".join([random.choice(c) for _ in range(n)])
    if n < 5:
        captcha = "".join([random.choice(c) for _ in range(5)])
    return captcha

def escolherCaracNum(l_e, n):
    carac = ''
    for i in range(0, len(l_e)):
        if l_e[i] == 'L':
            carac += alfa_mai
        elif l_e[i] == 'l':
            carac += alfa_min
        elif l_e[i] == 'n':
            carac += numeros
        elif l_e[i] == 'e':
            carac += carac_especial
    return gerarCaptcha(carac, n)

##### PROGRAMA PRINCIPAL #####

alfa_min = 'abcdefghijklmnopqrstuvwxyz'
alfa_mai = ('abcdefghijklmnopqrstuvwxyz').upper()
numeros = '0123456789'
carac_especial = '"!@#$%¨&*()_+-=<>,.^~{}[]´`'

todos_carac = alfa_min + alfa_mai + numeros + carac_especial

while True:
    print()
    menu_captcha()
    opcao_captcha = int(input("Digite a opcao desejada: "))
    if opcao_captcha == 0:
        print("PROGRAMA ENCERRADO")
        break
    else:
        if opcao_captcha == 1:
            print(f"CAPTCHA gerado: {gerarCaptcha(todos_carac, 10)}")
        elif opcao_captcha == 2:
            qtd = int(input("Captcha com quantos caracteres?: "))
            print(f"CAPTCHA gerado: {gerarCaptcha(todos_carac, qtd)}")
        elif opcao_captcha == 3:
            menu_caracteres()
            qtd = int(input("Captcha com quantos caracteres?: "))
            lista_escolha = [item for item in str(input("Escolha(separando com o espaço entre as letras): ")).split()]
            print(escolherCaracNum(lista_escolha, qtd))
            lista_escolha.clear()
        elif opcao_captcha == 4:
            menu_caracteres()
            qtd = int(input("Captcha com quantos caracteres?: "))
            lista_escolha = [item for item in str(input("Escolha(separando com o espaço entre as letras): ")).split()]
            lista_captcha = []
            for i in range(0, 10):
                lista_captcha.append(escolherCaracNum(lista_escolha, qtd))
            print("Lista dos 10 captchas gerados:")
            print(lista_captcha)
            lista_escolha.clear()
        elif opcao_captcha == 5:
            menu_caracteres()
            qtd = int(input("Captcha com quantos caracteres?: "))
            lista_escolha = [item for item in str(input("Escolha(separando com o espaço entre as letras): ")).split()]
            arquivo = open("texto.txt", "w")
            for i in range(0, 20):
                arquivo.writelines(f"\n{escolherCaracNum(lista_escolha, qtd)}")
            arquivo.close()
            print("20 CAPTCHAS foram armazenados com sucesso!")