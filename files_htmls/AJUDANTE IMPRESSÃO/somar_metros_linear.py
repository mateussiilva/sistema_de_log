import os
import glob
import sys
from PIL import Image
Image.MAX_IMAGE_PIXELS = None


caminho = r"\\Storage-silkart\IMPRESSAO\09 10 2023"
os.chdir(caminho)

soma_altrua_px = 0
metros_malha = 0
metros_tactel = 0
for arquivo in glob.glob("*tif"):
	#print(arquivo)
	if "malha" in arquivo.lower():
		img = Image.open(arquivo)
		dpi = img.info["dpi"]
		size = img.size[1] * (2.54/100)
		metros_malha += size

	if "tactel" in arquivo.lower():
		img = Image.open(arquivo)
		dpi = img.info["dpi"]
		size = img.size[1] * (2.54/100)
		metros_tactel += size


print(f"""
	\n {metros_malha/100}m de malha\n{metros_tactel/100} de tactel""")