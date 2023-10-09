from util.util import maior_dimensao

texto = "110.0 x 230.0cm"
dimensoes = maior_dimensao(texto)


for num in dimensoes:
    print(num)