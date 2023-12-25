from PySimpleGUI import Window,WIN_CLOSED,Print,Text



print("Hello World")
layout = [
    [Text("Caminho:")],
    [Print()]
    
]



window = Window(" ",layout)

while True:
    events,values = window.read()
    
    
    if events == WIN_CLOSED:
        break
    
    
window.close()