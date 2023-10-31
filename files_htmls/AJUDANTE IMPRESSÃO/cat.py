import os
import glob
import time
import argparse
from PIL import Image



"""parser = argparse.ArgumentParser()
parser.add_argument('-p', '--root-path', help='Full Input Path')
parser.add_argument('-e', '--extensao', help='Extensão alvo')
#parser.add_argument('-w', '--new-width', help='New image width')
args = parser.parse_args()"""

caminho_base = r"""\\Storage-silkart\IMPRESSAO\CLIENTES\BARCHE\06 09 23\IMPRESSÃO\CORRIDOS TEX"""


os.chdir(caminho_base)
arquivos_antigos = []
FLAGS_UTILIZADOS = ("KAMILA VERGNA - ",
	"BARCHE (IMPRESSAO TEX) - ",
	"GILCIMAR-(IMPRESSAO)-",
	"RAMONES GARCIA-(IMPRESSAO)-")
PREFIXO = FLAGS_UTILIZADOS[1]
for arquivo in glob.glob("*.tif"):
	if PREFIXO not in arquivo:
		nome_novo = PREFIXO + arquivo
		os.rename(arquivo,nome_novo.upper())
	else:
		print("Esse arquivo já foi renomeado")

"""
lista_arquivos = [
	arquivos
	for arquivos in glob.glob(os.path.join(caminho_base,"*.jpg"))
]

def converter_pixel_for_cm(pixel,ppi):
	cm = (2.54 * pixel) // ppi
	return cm

for imagens in lista_arquivos:
	img = Image.open(imagens)
	dpi_image = int(max(img.info["dpi"]))
	size = img.size
	largura  = converter_pixel_for_cm(size[0],dpi_image)
	altura  = converter_pixel_for_cm(size[1],dpi_image)
	print(f"Largura: {largura}cm, altura: {altura}cm")


"""


