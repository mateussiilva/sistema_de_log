import PySimpleGUI as sg
from PyUtilites import criar_matrix
from json import load


SIZE = (900,700)
HEADERS = [
    "Nome do Arquivo",
    "Metros",
    "Data da Impressão"]


layout = [
    [sg.Text("Caminho do arquivo json"),sg.Input(key="-PATH_JSON-"),sg.FileBrowse(button_text="Abrir Arquivo")],
        [sg.Table(values=[],
              headings=HEADERS,
              enable_click_events=True,enable_events=True,
              col_widths=100,
              expand_x=True,
              expand_y=True,
              selected_row_colors="Red on Yellow",justification="left",
              auto_size_columns=True,size=(45,32),alternating_row_color="Gray",k="-TABELA-",
              )],
    [
        sg.Button("Gerar Tabela",key="-LOAD_TABLE-"),
        sg.Button("Limpar Tabela",key="-CLEAR_TABLE-"),
        sg.Button("Somar Linhas",key="-SUM_TABLES-")
    ]
    
]



window = sg.Window("Gerenciador de LOG",layout,size=SIZE)

while 1:
    events,values = window.read()
    with open(values["-PATH_JSON-"]) as file:
        valores = criar_matrix(load(file))
    valores = valores
    """ valores = [["Painel redondo","15","22/12/23"],["Painel Quadrado","10","10/15/20"],
               ["Painel Quadrado","5","10/15/20"]]
     """
    if events == "-LOAD_TABLE-":
        window["-TABELA-"].update(values=valores)
        window.refresh()
    elif events == "-CLEAR_TABLE-":
        window["-TABELA-"].update(values=[])
        window.refresh()
    
    elif events == "-SUM_TABLES-":
        print(values["-TABELA-"])
        indices = values["-TABELA-"]
        s = 0
        for indice in indices:
            metros = float(valores[indice][1])
            s += metros
        print(s)
        
    if events == sg.WIN_CLOSED:
        break
    

    # print(values)
    
    
    
window.close()