import os
import cv2
import pytesseract
from PIL import Image
import os
import glob

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

PATH_BASE = r"\\Storage-silkart\impressao\das minys\PEDIDOS\18 09 23\WhatsApp Unknown 2023-09-22 at 14.26.06"
imagem = "WhatsApp Image 2023-09-18 at 13.16.54 (1).jpeg"
imagem_cinza = "teste_cinza.jpg"
path_image= os.path.join(PATH_BASE,imagem)

def converter_imagem_para_cinza(origem,destino="CONVERTIDAS"):
    os.chdir(origem)
    for imagens in glob.glob("*.jpeg"):
        _img = Image.open(imagens)
        _gra_img = _img.convert("L")
        _gra_img.save(os.path.join(destino,imagens))
        print(imagens)


#
def extrair_texto(image):
    dados_img = []
    texto = pytesseract.image_to_string(img)
    lista_texto = texto.split()
    for linha in lista_texto:
        if "D9" in linha:
            dados_img.append(linha)
    return dados_img

os.chdir(os.path.join(PATH_BASE,"CONVERTIDAS"))
for imagens in glob.glob("*.jpeg"):
    img = Image.open(imagens)
    print(
    extrair_texto(img))


"""
img = Image.open(path_image)
img_cinza = img.convert("L")
img_cinza.save(os.path.join(PATH_BASE,imagem_cinza))

img = Image.open(path_image_gray)
text = pytesseract.image_to_string(img)
print(text)

lista_metros = []
os.chdir(PATH_BASE)
for imagens in glob.glob("*.jpeg"):
    img = Image.open(imagens)
    text = pytesseract.image_to_string(img)
    lista_text = list(filter(lambda t:"metros" in t.lower(),text.split("\n\n")))
    if len(lista_text) > 0:
        metragem = int(lista_text[0].split(" ")[0])
        lista_metros.append(metragem)
        print(len(lista_text),lista_text)
    else:
        print(imagens)
    #lista_metros.append(lista_text)
print(lista_metros)
with open("listr_metragem.txt","w+") as file_txt:
    for metros in lista_metros:
        linha = f'{metros}'
        file_txt.write(linha)
"""