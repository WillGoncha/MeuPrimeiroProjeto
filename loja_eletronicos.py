from produtos import *
from colorama import Fore, init
init(autoreset=True)


def exibir_menu():
    print(f"{Fore.MAGENTA} ><==>< MENU ><==><")
    print(f"\n1. {Fore.GREEN}Adicionar Produto")
    print(f"2. {Fore.YELLOW}Atualizar Produto")
    print(f"3. {Fore.RED}Deletar Produto")
    print(f"4. {Fore.BLUE}Visualizar Estoque")
    print("5. Sair do Sistema")

def processar_opcao(opcao):
    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        atualizar_produto()
    elif opcao == "3": 
        deletar_produto()
    elif opcao == "4":
        ler_estoque()
    elif opcao == "5":
        print(f"{Fore.RED}Saindo do sistema...")
        exit(0)
    else:
        print(f"{Fore.RED}Opção inválida. Tente novamente")

def executar_sistema():
    limpar_terminal()
    exibir_menu()
    opcao = input("\nDigite alguma opção...")
    limpar_terminal()
    processar_opcao(opcao)
    pausar()
    limpar_terminal()
    executar_sistema()

executar_sistema()