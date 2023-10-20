import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED,Window,Input,Button,FolderBrowse




layout = [
    [FolderBrowse("Pasta de Origem")]
]


window = Window("Gerenciador de LOG",layout)

while 1:
    events,values = window.read()
    
    if events == WIN_CLOSED:
        break
    
    
    
window.close()    