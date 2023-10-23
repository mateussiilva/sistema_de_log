import os


import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED,Window,Input,Button,FolderBrowse,popup_error

# CONSTANTES DO SISTEMA
SIZE_WINDOW =700,850

# sg.theme("Dark")

tab1 = sg.Tab("",    
    [[sg.Frame("Manipulação de Arquivos",
            layout=[
                [   
                    sg.Text("Selecione a pasta de origem"),
                    Input(key="-INP_HTMLS-"),
                    FolderBrowse("Pasta de Origem",key="-PATH_SOURCE_HTMLS-")
                ],
                [
                    sg.Text("Selecione a pasta de destino"),
                    Input(key="-INP_JSONS-"),
                    FolderBrowse("Pasta de Origem",key="-PATH_DESTINO_JSONS-")
                ]])],
    [
        sg.Radio("Mutoh",group_id=0),
        sg.Radio("PrismaJet",group_id=0),
        sg.Radio("PrismaTex",group_id=0),
        ],           
    [
        sg.Multiline(disabled=True,size=(90,45),key="-OUTPUT-")
    ],
    [Button("Gerar json",key="-CREATE_JSON_FILES"),Button("Carregar Arquivo txt",key="-LOAD_FILE_TXT-")]]
)

tab2 = sg.Tab("",[
    []
])



layout_main = [
    [sg.TabGroup(
        [[tab1]])]
]


window = Window("Gerenciador de LOG",layout_main,size=SIZE_WINDOW,relative_location=(800,0),resizable=True)
while 1:
    events,values = window.read()
    print(values)
    
    if events == "-CREATE_JSON_FILES":
        FOLDER_FILES_HTMLS = values.get("-INP_HTMLS-")
        FOLDER_FILES_JSONS = values.get("-INP_JSONS-")
        if FOLDER_FILES_HTMLS is not None and FOLDER_FILES_JSONS:
            for arquivos in os.listdir(FOLDER_FILES_HTMLS):
                print(arquivos)
            # window.close()
        else:
            popup_error(
                "Selecione as pastas de ORIGEM e de DESTINO",title="ERROR AO SELECIONAR AS PASTAS")
            break
        
    if events == "-LOAD_FILE_TXT-":
        arquivo = "arquivo_.txt"
        with open(arquivo,"r") as file:
            window["-OUTPUT-"].update(file.read())
    if events == WIN_CLOSED:
        break
    
    
window.close()    