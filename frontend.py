import PySimpleGUI as sg
from PyUtilites import criar_matrix
from PySimpleGUI import popup_ok
from PyJson import PyJson


SIZE = (900, 700)
HEADERS_TABLE = [
    "Nome do Arquivo",
    "Metros",
    "Data da Impressão"]
layout = [
    [sg.Text("Caminho do arquivo json"),sg.Input(key="-PATH_JSON-"),
     sg.FileBrowse(button_text="Abrir Arquivo",
                   initial_folder="/media/mateus/D395-E345/ProjetctFiles/arquivos_json/arquivos_antigos/")],
    [sg.Table(values=[],
              headings=HEADERS_TABLE,
              enable_click_events=True,enable_events=True,
              col_widths=100,
              expand_x=True,
              expand_y=True,
              selected_row_colors="Red on Yellow",justification="left",
              auto_size_columns=True,size=(45,32),alternating_row_color="Gray",k="-TABELA-",
              )
    ],
    [
        sg.Button("Gerar Tabela",key="-LOAD_TABLE-"),
        sg.Button("Limpar Tabela",key="-CLEAR_TABLE-"),
        sg.Button("Somar Linhas",key="-SUM_TABLES-")
    ]
    
]



# sg.theme("DarkBlue")
window = sg.Window("Gerenciador de LOG",layout,size=SIZE)


while 1:
    events,values = window.read()
    # py_json = PyJson(values["-PATH_JSON-"])
    # valores = criar_matrix(py_json.ler_json())

    # if events == "-LOAD_TABLE-":
    #     window["-TABELA-"].update(values=valores)
    #     window.refresh()
    # elif events == "-CLEAR_TABLE-":
    #     window["-TABELA-"].update(values=[])
    #     window.refresh()
    
    # elif events == "-SUM_TABLES-":
    #     indices = values["-TABELA-"]
    #     s = 0
    #     for indice in indices:
    #         metros = float(valores[indice][1])
    #         s += metros
    #     msg = f"{s:.2f}"
    #     popup_ok(msg)

        
    if events == sg.WIN_CLOSED:
        break
    

    # print(values)
    
    
    
window.close()