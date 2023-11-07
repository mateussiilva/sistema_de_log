# print("\033[1;32mArquivo criado com sucesso\033[m")


def title(msg):
    print(f"\033[1;32;42m{msg}\033[m")


def messagem(msg,error=False):
    if error:
        print(f"\033[1;31m{msg}\033[m")
    
    print(f"\033[1;32m{msg}\033[m")
    

def show_menu(opcoes:dict):
    for codigo,nome in opcoes.items():
        print(f"{codigo} == {nome}")
    
    
def menu():
    print("[0] == GERAR JSONS")
    print("[1] == SAIR")
PLOTTERS = {
    "mutoh":"1604",
    "prismajet":"1602",
    "prismatex":"1904"
    }

while 1:
    title("SISTEMA DE LOG")
    menu()
    
    opcao = int(input("Qual opção: "))
    if opcao > 1:
        messagem("OPÇÃO INVALIDA",True)
    elif opcao == 1:
        messagem("OPÇÃO VALIDA")
    elif opcao == 0:
        messagem("SAINDO DO SISTEMA")
        break