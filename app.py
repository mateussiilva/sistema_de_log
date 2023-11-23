
from os.path import splitext,split

def limpar_nome(texto):
    lista_texto = texto.split("\\")
    return lista_texto[len(lista_texto) -1]


print(limpar_nome("Z:\\das minys\\CORRIDOS VERAO 2023\\ESTAPAS CONFERIDAS\\D201.tif")) 
