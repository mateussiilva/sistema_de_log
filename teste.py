from pprint import pprint as print
import json
import PySimpleGUI as sg



impressao = {
        "ARQUIVO": "Z:\\das minys\\CORRIDOS VERAO 2023\\ESTAPAS CONFERIDAS\\D201.tif",
        "DIMENS\u00c3O": "150.0 x 100.0cm",
        "PERFIL ICC DE SA\u00cdDA": "GS1904W_HIPRO_BN30GR_360X1800_3P_BZRA.icc",
        "QUANTIDADE DE C\u00d3PIAS": "25",
        "IN\u00cdCIO, DATA E HORA DO RIP": "06:27:34 01/09/2023"
    }

def limpar_nome(texto):
    



def limpar_dimensao(texto):
    return float(texto.replace("cm","").split(" x ")[1])


with open("01 09 23.json","r") as file:
    dados = json.load(file)


def orgnizar_lista(dicionario,env):
    
    for chave,valor in dicionario.items():
        if chave == "DIMENSÃO":
            qtd_copias = int(dicionario["QUANTIDADE DE C\u00d3PIAS"])
            metros = str(qtd_copias * limpar_dimensao(valor))
            env.append(metros)
        elif chave != "QUANTIDADE DE C\u00d3PIAS" and \
            chave != "PERFIL ICC DE SA\u00cdDA":
            env.append(valor)
                
            
    return env



def criar_matrix(dados:dict) -> list[list]:
    matrix = []
    tmp = []
    for _,dado in dados.items():
        tmp = orgnizar_lista(dado,tmp)
        matrix.append(tmp[:])
        tmp.clear()
        
    return matrix

matrix_de_dados= criar_matrix(dados)

print(type(matrix_de_dados))
print(matrix_de_dados)



# headers = ["Arquivo","Dimensao","Perfil ICC","Quantidade de Copias","Data de Impressão"]

layout = [
    [sg.Table(values=matrix_de_dados,
              enable_click_events=True,enable_events=True,
              selected_row_colors="Red on Yellow",justification="center")]
]


window = sg.Window(" ",layout)

while True:
    events,values = window.read()
    
    if events == sg.WIN_CLOSED:
        break
    
# window.close()

    
    


    