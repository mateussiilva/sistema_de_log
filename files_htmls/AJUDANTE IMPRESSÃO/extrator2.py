import os 
import re 


PATH_BASE = r"\\Storage-silkart\impressao\das minys\PEDIDOS\18 09 23\WhatsApp Unknown 2023-09-22 at 14.26.06"
NOME_ARQUIVO_TXT = "listr_metragem.txt"

path_txt = os.path.join(PATH_BASE,NOME_ARQUIVO_TXT)

with open(path_txt, "r") as txt:
	linhas = txt.readlines()


print(
	sum(
		map(
			lambda l: int(l.strip("\n")),
			linhas
			)
		),
	len(linhas)
)