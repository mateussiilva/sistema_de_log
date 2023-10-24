import os
import backend as back

import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED,Window,Input,Button,FolderBrowse,popup_error
from pprint import pprint as print
# CONSTANTES DO SISTEMA
SIZE_WINDOW =700,850
PLOTTERS = {
    "mutoh":"1604",
    "prismajet":"1602",
    "prismatex":"1904"
    }

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
        sg.Text("Selecione a maquina:",),
        sg.InputCombo(values=["Mutoh","PrismaJet","PrismaTex"],key="-MAQUINA-",default_value="Mutoh"),
        ],           
    [
        sg.Multiline(disabled=True,size=(90,45),key="-OUTPUT-")
    ],
    [Button("Gerar json",key="-CREATE_JSON_FILES"),Button("Carregar Arquivo txt",key="-LOAD_FILE_TXT-")]]
)

tab2 = sg.Tab("",[
    
])



layout_main = [
    [sg.TabGroup(
        [[tab1]])]
]


def get_plotter(plotter) -> str:
    for plotter,value in PLOTTERS.items():
        if plotter == plotter:
            return value



window = Window("Gerenciador de LOG",layout_main,size=SIZE_WINDOW,relative_location=(800,0),resizable=True)
while 1:
    events,values = window.read()
    
    if events == "-CREATE_JSON_FILES":
        MAQUINA = get_plotter(values["-MAQUINA-"])
        FOLDER_FILES_HTMLS = values.get("-INP_HTMLS-")
        FOLDER_FILES_JSONS = values.get("-INP_JSONS-")
        
        if FOLDER_FILES_HTMLS is not None and FOLDER_FILES_JSONS:
            back.main(
                path_origem=FOLDER_FILES_HTMLS,
                path_destino=FOLDER_FILES_JSONS,
                plotter=MAQUINA
            )

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