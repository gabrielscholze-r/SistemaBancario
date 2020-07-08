import pickle
from random import *

try: #verifica a existencia de um arquivo contas ja criadas
    file = open("ContasCriadas", "rb")
    file.close()
except:
    # Caso não existe, cria o arquivo para armazenar as contas
    ContasCriadas = [0]
    file = open("ContasCriadas", "wb")
    pickle.dump(ContasCriadas, file)
    file.close()

caracteres = ['´', '^', '~', '`', '@', '#', '$', '_', '-', '&', '*',
              '%', '!', '?', ";", ":", "/","|","(", ")", "<", ">", ".",
              ","] #Caracteres proibidos na senha de uma conta


def verify(password): #função para verificar se a conta possui algum dos caracteres acima e se esta entre 4 e 8 digitos
    for M in password:
        for H in caracteres:
            if M == H and len(password) > 8 or len(password) < 4:
                print("Senha inválida, tente novamente!")
                return loop()


def loop(): #função "menu": sempre que realizar uma ação, voltará a esse menu
    print("_" * 20)
    print("Interface do Gerente")
    print("_" * 20)

    print("Cadastrar nova conta = 1" "\nPesquisar conta = 2" "\nRedefinir senha = 3")

    n = input("Número da ação:")
# condição que define, de acordo com o numero, o caminho que o gerente seguirá para realizar tal aão
    #if n > 3 or n < 1: #vê se o numero se encaixa nos padroes
     #   print("Numero sem ação correspondente")
      #  loop()
    if n == "1":
        NewAccount()
    elif n == "2":
        search()
    elif n == "3":
        changePass()
    else:
        print("Entrada inválida")
        loop()


def NewAccount(): #função para criar uma nova conta
    print('TEXTO APENAS EM MAIÚSCULO')
    #entrada dos dados da nova conta
    nome = str(input("Nome completo(EM MAIÚSCULO):"))
    job = str(input("Profissão(EM MAIÚSCULO):"))
    money = float(input("Renda mensal:"))
    adress = str(input("Endereço(EM MAIÚSCULO):"))
    phone = int(input("Telefone:"))
    password = input("Insira sua senha(4 A 8 Dígitos!):")
    verify(password) #verificação da senha inserida
    numAccount = randint(10000, 99999) #gera o numero de conta de 5 digitos
    file = open("ContasCriadas", "rb")
    ContasCriadas = pickle.load(file)
    for x in ContasCriadas: #verifica se o numero da conta ja existe
        if x == numAccount:
            numAccount = randint(10000, 99999) # caso exista, gera um novo numero de conta
        continue

    ContasCriadas.append(numAccount) #Adiciona o numero da conta ao registro
    file = open('ContasCriadas', "wb")
    pickle.dump(ContasCriadas, file) # arquiva as contas
    file.close()
    print("Número da conta: ", numAccount)

    name = [numAccount] # define essa lista para nomear cada arquivo de conta com o numero da conta da pessoa
    name2 = [nome] # define uma lista apenas com o nome para facilitar a pesquisa de conta posteriormente
    file = open(f'{name[0]}', 'wb') #abre o arquivo com o nome sendo o numero da conta
    name[0] = [nome, job, money, adress, phone, password, numAccount, 0]
    pickle.dump(name[0], file) #salva o arquivo
    file.close()
    z = [numAccount]
    try: #verifica se o nome da pessoa ja possui uma conta para registrar uma nova ao nome dela
        file = open(f"{name2[0]}", "rb")
    except:
        file = open(f"{name2[0]}", "wb")
        pickle.dump(z, file)
        file.close()
        loop()
    y = pickle.load(file)
    y.append(numAccount)
    file = open(f"{name2[0]}", "wb")
    pickle.dump(y, file)

    return loop() #volta a função inicial


def search(): #fução de pesquisa de conta
    nome = str(input("Insira o nome do titular da conta que procura(EM MAIÚSCULO):"))

    try:
        file = open(f"{nome}", "rb") #verifica se a conta existe com base no nome da pessoa
    except:
        print("Conta não existe, tente novamente!")
        loop()
    x = pickle.load(file) # load na lista com o numero da conta
    for i in x: #laço de repetição para printar todas as contas com o nome do usuario
        f = open(f"{i}", "rb") # abre o arquivo com o nome como o numero da conta
        y = pickle.load(f)
        # printa todos os dados do usuario
        print(f"Nome:{y[0]}")
        print(f"Profissão:{y[1]}")
        print(f"Renda mensal:{y[2]}")
        print(f"Endereço:{y[3]}")
        print(f"Telefone:{y[4]}")
        print(f"Senha:{y[5]}")
        print(f"Número da conta:{y[6]}")
        print(f"Saldo:R${y[7]}")
        print("_"*30)
    loop() # retorna a função "menu"

def changePass(): #função para mudar conta do cliente
    conta = str(input("Insira o número da conta:"))

    try: #Tenta achar a conta, caso não ache
        file = open(f'{conta}', 'rb')
    except:
        print("Nome sem conta registrada! Por favor, tente novamente!")
        loop()
    x = pickle.load(file)
    file.close()
    account = x[6] #account recebe o numero da conta para substituir o arquivo aposa alteração da senha
    y = input("Insira a nova senha:") # solicita nova senha
    verify(y) #verifica se a senha é valida
    x[5] = y #substitui a senha
    Data = x #data recebe os dados para arquivar novamente
    file = open(f'{account}', 'wb')
    pickle.dump(Data, file)
    file.close()
    print("Realizado com sucesso!")
    return loop() #retorna a função "menu"




print(loop())
