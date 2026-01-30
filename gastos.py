#BIBLIOTECAS
import os

#*DEFINIÇÕES
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def confirmar():
    nd = input()
    limpar()

#*CONFERE A EXISTÊNCIA DO TXT (BANCO)
try:
    with open("extrato.txt", "r") as extrato:
        pass
except FileNotFoundError:
    with open("extrato.txt", "w") as extrato:
        pass

while True:
    limpar()
    print("EXTRATO BANCÁRIO\n")
    print("[1] Ver extrato")
    print("[2] Adicionar Gasto")
    print("[3] Remover Gasto")
    print("[4] Sair")
    resposta = input("\nResposta: ")

    #? VER EXTRATO
    if resposta == "1": 
        limpar()
        with open("extrato.txt", "r") as extrato:
            conteudo = extrato.readlines() #* Uma lista é criada, cada linha do .txt vira um elemento/palavra

        valorTotal = 0
        for char in conteudo: #* Cada iteração pega um elemento da lista de conteúdo AKA cada linha do .txt
            casa = char.split(";") #* Cria uma sub lista, casa, que a cada ";" cria um novo elemento
            print(f"{casa[0]} -- R${float(casa[1])}")
            valorLocal = float(casa[1]) #* Transforma o segundo elemento de casa (o preço) em float
            valorTotal += valorLocal

        print(f"\nValor Total: R${float(valorTotal)}")
        confirmar()

    #? ADICIONAR GASTO
    elif resposta == "2":
        limpar()
        with open("extrato.txt", "a") as extrato:
            termoUm = input("Qual o nome do Gasto? ")
            termoDois = input("Qual o valor do Gasto? ")
            termoGeral = termoUm + " ; " + termoDois
            extrato.write(termoGeral + "\n")
        print(f"{termoUm} adicionado com sucesso")

    #?Remover Gasto
    elif resposta == "3":
        limpar()
        valorTotal = 0
        indice = 1

        with open("extrato.txt", "r") as extrato:
            conteudo = extrato.readlines() 

        for char in conteudo:
            print(f"{indice}.", end="")
            indice += 1


            casa = char.split(";")
            print(f"{casa[0]} -- {float(casa[1])}")
            valorLocal = float(casa[1])
            valorTotal += valorLocal
        print(f"\nValor Total: {float(valorTotal)}")
        resposta = int(input("\nQual deseja excluir? ")) - 1

        exclusao = conteudo.pop(resposta)
        nome_exc = exclusao.split(";")
        limpar()
        print(f"{nome_exc[0].strip()} excluído com sucesso")
        confirmar()

        with open("extrato.txt", "w") as extrato:
            for num in conteudo:
                extrato.write(num)

    #?Sair
    elif resposta == "4":
        limpar()
        break