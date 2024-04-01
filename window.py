tab_layout1 = [[sg.Button('My first Button!'), sg.Checkbox('My first Checkbox!')],
               [sg.Button('Another Button.')]]
tab_layout2 = [[sg.Button('My third Button!'), sg.Checkbox('My second Checkbox!')]]

layout = [[sg.TabGroup([[sg.Tab("Tab 1", tab_layout1), sg.Tab("Tab 2", tab_layout2)]])]]