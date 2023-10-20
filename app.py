import os


import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED,Window,Input,Button,FolderBrowse,popup_error

# CONSTANTES DO SISTEMA
SIZE_WINDOW =760,480


layout = [
    [sg.Frame("",layout=[
        [   
            sg.Text("Selecione a pasta de origem"),
            Input(key="-INP_HTMLS-"),
            FolderBrowse("Pasta de Origem",key="-PATH_SOURCE_HTMLS-")
        ],[
            sg.Text("Selecione a pasta de destino"),
            Input(key="-INP_JSONS-"),
            FolderBrowse("Pasta de Origem",key="-PATH_DESTINO_JSONS-")
            ]
        ],
    )],
    [Button("Gerar json",key="-CREATE_JSON_FILES")]
]


window = Window("Gerenciador de LOG",layout,size=SIZE_WINDOW,relative_location=(800,0))

while 1:
    events,values = window.read()
    FOLDER_FILES_HTMLS = values.get("-INP_HTMLS-")
    FOLDER_FILES_JSONS = values.get("-INP_JSONS-")
    if events == "-CREATE_JSON_FILES":
        if FOLDER_FILES_HTMLS is not None and FOLDER_FILES_JSONS:
            for arquivos in os.listdir(FOLDER_FILES_HTMLS):
                print(arquivos)
            window.close()
        else:
            popup_error(
                "Selecione as pastas de ORIGEM e de DESTINO",title="ERROR AO SELECIONAR AS PASTAS")
            break
    
    if events == WIN_CLOSED:
        break
    
    
    
window.close()    