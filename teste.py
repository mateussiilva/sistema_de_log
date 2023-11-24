from pprint import pprint as print
import json
import PySimpleGUI as sg



def limpar_nome(texto):
    lista_texto = texto.split("\\")
    return lista_texto[len(lista_texto) -1]


def limpar_dimensao(texto):
    return float(texto.replace("cm","").split(" x ")[1])


def orgnizar_lista(dicionario,env):
    
    for chave,valor in dicionario.items():
        if chave == "DIMENSÃO":
            qtd_copias = int(dicionario["QUANTIDADE DE C\u00d3PIAS"])
            metros = str(round(qtd_copias * limpar_dimensao(valor))/100)
            env.append(metros)
        elif chave == "ARQUIVO":
            nome_limpo = limpar_nome(valor)
            env.append(nome_limpo)
        elif chave != "QUANTIDADE DE C\u00d3PIAS" and \
            chave != "PERFIL ICC DE SA\u00cdDA":
            env.append(valor)

    return env


def criar_matrix(dados:dict):
    matrix = []
    tmp = []
    for _,dado in dados.items():
        tmp = orgnizar_lista(dado,tmp)
        matrix.append(tmp[:])
        tmp.clear()   
    return matrix

def carregar_dados(caminho_arquivo):
    with open(caminho_arquivo,"r") as file:
        dados = json.load(file)
        
    return dados

def pegar_arquivo_json():
    return sg.popup_get_file("Selecione o arquivo",initial_folder="/media/mateussiilva/D395-E345/arquivos_json")


# caminho_arquivo = pegar_arquivo_json()
headers = ["Nome do Arquivo","Quantide(metros)","Data e Hora da Impressão"]

# # layout = [
#     [sg.Table(values=[],
#               max_col_width=48,
#               headings=headers,
#               enable_click_events=True,enable_events=True,
#               col_widths=100,
#               expand_x=False,
#               expand_y=True,
#               selected_row_colors="Red on Yellow",justification="center",
#               auto_size_columns=True,size=(None,50),alternating_row_color="Gray",k="-TABELA-")]
# # ]


layout = [
    [sg.Text("Caminho arquivo Json:"),sg.Input(key="-CAMINHO_ARQUIVO_JSON-")],
    [sg.Button("Gerar Tabela",key="-GERAR_TABELA-"),sg.Button("Somar Linhas",key="-SOMAR_LINHAS-")],
    [sg.Table(
            visible=False,values=[],
              max_col_width=48,
              headings=headers,
              display_row_numbers=True,
              enable_click_events=True,enable_events=True,
              col_widths=100,
              expand_x=False,
              expand_y=True,
              selected_row_colors="Red on Yellow",justification="center",
              auto_size_columns=True,size=(None,50),alternating_row_color="Gray",k="-TABELA-")],
    [sg.Text(k="RESULTADO",visible=False)]
]


def gerar_tabela(caminho_arquivo):
    pass

window = sg.Window(" ",layout)

caminho_arquivo_json = pegar_arquivo_json()
while True:
    events,values = window.read()
    
    
    if events == "-GERAR_TABELA-":
        nome_arquivo = caminho_arquivo_json
        dados = carregar_dados(nome_arquivo)
        matrix = criar_matrix(dados)
        total  = sum(list(map(lambda lista: float(lista[1]),matrix)))
        window["-TABELA-"].update(values=matrix,visible=True)
        print(total)
        
    if '+CLICKED+' in events:
        dados = carregar_dados(nome_arquivo)
        matrix = criar_matrix(dados)

        # linha = events[2][0]
        # print(matrix[linha][1])

    if events == "-SOMAR_LINHAS-":
        pass

    
    if events == sg.WIN_CLOSED:
        break
    
window.close()

    
    


    