# import PySimpleGUI as sg



# layout = [
#     [sg.Text("Caminho do arquivo:"),
#      sg.Input(key="-CAMINHO_ARQUIVO_JSON-"),
#      sg.FileBrowse("Selecione o Arquivo",key="-SELECIONAR_ARQUIVO-")
#      ],
    
# ]


# window = sg.Window(" ",layout)

# while True:
#     events,values = window.read(timeout=1000)
#     caminho_arquivo = values["-CAMINHO_ARQUIVO_JSON-"]
    
    
#     if events == sg.WINDOW_CLOSED:
#         break
    
#     if events == "-SELECIONAR_ARQUIVO":
#         tabela = [sg.Table(values=["","",""])]
#         layout.append(tabela)
#         window[""].update(layout)
        
#                 # print(linha)
#     elif events == sg.TIMEOUT_KEY:
#         window.refresh()