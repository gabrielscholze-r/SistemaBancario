import pickle
from random import *

caracteres = ['´', '^', '~', '`', '@', '#', '$', '_', '-', '&', '*',
              '%', '!', '?', ";", ":", "/","|","(", ")", "<", ">", ".",
              ","] #Caracteres proibidos na senha


def verify(password): # função para validar a senha
    for M in password:
        for H in caracteres:
            if M == H and len(password) > 8 or len(password) < 4:
                print("Senha inválida, tente novamente!")
                return loop()
def loop(): # função "menu"
    print("_"*20)
    print("Interface do Usuário!")
    print("_" * 20)
#enumeração das ações possiveis
    print("O que quer fazer hoje?")
    print("Saque = 1")
    print("Depósito = 2")
    print("Vizualisar saldo = 3")
    print("Simulação de investimento = 4")

    n = int(input("Ação desejada:"))
# definindo o que realizar de acordo com a ação que o usuario introduzir
    if n>4 or n<1:
        print("Número sem ação correspondente, tente novamente!")
        loop()
    elif n == 1:
        saque()
    elif n == 2:
        deposito()
    elif n == 3:
        Saldo()
    elif n == 4:
        invest()
def saque(): #função de saque
    conta = int(input("Digite o número da conta:"))
    senha = input("Digite a sua senha:")
    verify(senha) #verifica a senha
    try:
        file = open(f"{conta}", "rb") # verifica a existencia da conta
    except:
        print("Conta não existe, tente novamente!")
        loop() #caso nao exista, volta ao menu
    x = pickle.load(file) # se existir, da load no da lista em x
    if x[6] == conta: #verifica se a conta é a mesma da lista
        if x[5] == senha: #verifica se a senha esta correta
            if x[7] <= 0: # Caso o saldoseja zero, não é possivel sacar
                print("Saldo insuficiente para saque!")
                loop()
            else:
                print(f"Saldo:R${x[7]}") #printa o saldo e pede o valor, que tem que ser menor que o total e maior que zero
                y = float(input("Valor do saque:R$"))
                if y > x[7]:
                    print("Valor excede o saldo, tente novamente!")
                    loop()
                elif y == 0:
                    print("Nâo é possivel sacar R$0")
                    loop()
                valor = x[7] - y
                x[7] = valor #substitui com o valor atual, sem o valor sacado
                print("Saque realizado com sucesso!")
                file = open(f"{conta}", "wb")
                pickle.dump(x, file) #substitui o arquivo da conta, com o novo saldo
                file.close()
        else:
            print("Senha incorreta")
            loop()
    else:
        print("Número da conta incorreto")
        loop()
def deposito(): #função para deposito
    conta = int(input("Digite o número da conta:"))
    senha = input("Digite a sua senha:")
    verify(senha) #verifica a senha
    try:
        #Verifica se a conta existe
        file = open(f"{conta}", "rb")
    except:
        print("Conta não existe, tente novamente!")
        loop()
        #x recebe a lista do arquivo
    x = pickle.load(file)
    if x[6] == conta: #verifica se a conta inserida esta de acordo
        if x[5] == senha: #verifica se a senha esta certa
            print("SÃO ACEITOS VALORES ENTRE R$0 E R$10.000,00")
            #pede o valor do deposito
            valor = float(input("Qual valor deseja depositar?"))
            if valor < 0 or valor > 10000:
                print("Valor fora dos limites estabelecidos")
                deposito()
            #recebe o novo saldo, somando com o valor do saldo anterior
            novosaldo = valor + x[7]
            print(f"Saldo atualizado:R${novosaldo}")
            #substitui na lista
            x[7] = novosaldo
            file = open(f"{conta}", "wb")
            pickle.dump(x, file) #substitui o arquivo com as alterações de saldo
            file.close()
            loop()
        else:
            print("Senha incorreta")
            loop()
    else:
        print("Número da conta incorreto")
        loop()
def Saldo(): #função de saque
    conta = int(input("Digite o número da conta:"))
    senha = input("Digite a sua senha:")
    verify(senha) #verifica a senha
    try:
        #verifica se a conta existe
        file = open(f"{conta}", "rb")
    except:
        print("Conta não existe, tente novamente!")
        loop()
    #x recebe as informações do arquivo
    x = pickle.load(file)
    if x[6] == conta: #verifica se a conta esta correta
        if x[5] == senha: #verifica se a senha esta correta
            #printa e retorna para o menu
            print(f"Nome do titular:{x[0]}")
            print(f"Número da conta:{x[6]}")
            print(f"Saldo:R${x[7]}")
            loop()
        else:
            print("Senha incorreta")
            loop()
    else:
        print("Número da conta incorreto")
        loop()
def invest(): #função da simulação de investimento
    #pede total de meses de investimento e o valor inicial a ser investido
    n = int(input("Meses de investimento:"))
    c = float(input("Aporte inicial:R$"))
    m = c * ((1.015)**n) #calculo do rendimento total
    #aplicação das taxas de administração, somente aplicadas ao final do investimento
    if n < 60: #caso seja menos de 5 anos de investimento, a taxa cobrada é de 1%
        Total = m - (m*0.01)
        print("O montante acumulado ao longo dos {n} meses foi de R${Total}")
        loop()
    Total = m - (m*0.005) # a partir de 5 anos, a tava passa a ser 0,5%
    print(f"O montante acumulado ao longo dos {n} meses foi de R${Total:.2f}")
    loop()
print(loop())

