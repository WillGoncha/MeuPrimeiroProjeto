import os
from colorama import Fore, init
init(autoreset=True)

produtos = {"teclado"  :{"preço: R$":"150",
                         "quantidade:":"5"},
            "mouse"    :{"preço: R$":"90",
                         "quantidade:":"8"},
            "gabinete" :{"preço: R$":"200",
                         "quantidade:":"4"},
}

def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nDigite ENTER para continuar...")

def adicionar_produto():
    novo_produto = input("Digite o nome do produto que deseja adicionar: ")
    limpar_terminal()
    if novo_produto in produtos:
        print(f"{Fore.RED}Produto: {novo_produto} ja existente em nosso estoque!")
    else:
        valor_produto = float(input("Digite o valor do novo produto: "))
        quantidade_produto = input("Digite a quantidade do novo produto: ")
        produtos[novo_produto] = {"preço: R$":valor_produto,
                                "quantidade:":quantidade_produto}
        limpar_terminal()
        print(f"{Fore.GREEN}Produto cadastrado com sucesso!")
        print(f"\nProduto: {Fore.GREEN}{novo_produto}")
        for x, y in produtos[novo_produto].items(): 
            print(f"{x}{Fore.CYAN} {y}")

def atualizar_produto():
    for key in produtos.keys():
        print(f"{Fore.GREEN}{key}")
    nome_produto = input("\nDigite o nome do produto que deseja atualizar: ")
    limpar_terminal()
    if nome_produto in produtos:
        novo_preco = float(input("Digite o novo preço: "))
        nova_quantidade = input("Digite a nova quantidade: ")
        limpar_terminal
        produtos[nome_produto]["preço: R$"] = novo_preco
        produtos[nome_produto]["quantidade:"] = nova_quantidade
        limpar_terminal()
        print(f"{Fore.GREEN}Produto atualizado com sucesso!")
        print(f"\nProduto: {Fore.GREEN}{nome_produto}")
        for x, y in produtos[nome_produto].items(): 
            print(f"{x}{Fore.CYAN} {y}")
    else:
        print(f"{Fore.RED}Produto: {nome_produto} não cadastrado!")  

def deletar_produto():
    for key in produtos.keys():
        print(f"{Fore.RED}{key}")
    nome_produto = input("\nDigite o nome do produto que deseja deletar: ")
    limpar_terminal
    if nome_produto in produtos:
        del produtos[nome_produto]
        limpar_terminal()
        print(f"{Fore.GREEN}Produto: {nome_produto} foi deletado do estoque!")
    else:
        limpar_terminal()
        print(f"{Fore.RED}Produto: {nome_produto} não cadastrado!")             

def ler_estoque():
    limpar_terminal()
    for chave, valores in produtos.items():
        print(f"\nProduto: {Fore.GREEN}{chave}")
        for i, j in valores.items():
            print(f"{i}{Fore.CYAN} {j}")