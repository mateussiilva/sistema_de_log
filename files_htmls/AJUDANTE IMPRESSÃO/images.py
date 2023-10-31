from PIL import Image
import os
import glob


PATH = r"\\Storage-silkart\impressao\CLIENTES\IVONE FERREIRA"

cont = 0
os.chdir(PATH)
for files_pngs in glob.glob("*.png"):
	nome = f"imagem {cont}.jpg"
	img = Image.open(files_pngs)
	rgb_im = img.convert('RGB')
	rgb_im.save(nome)

for files_pngs in glob.glob("*.png"):
	os.remove(files_pngs)