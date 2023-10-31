import datetime
import os
import glob
import shutil


PATH_ORIGEM = r"C:\Program Files (x86)\SAi\SAi Production Suite Cloud\Jobs and Settings"
PATH_DESTINO = r"\\Storage-silkart\impressao\LOGS DAS MAQUINAS\1604"
NOME_ARQUIVO_BASE = "RIPLOG.HTML"

def copiar_arquivo_base():
	for arquivo_html in glob.glob(os.path.join(PATH_ORIGEM,"*.HTML")):
		if NOME_ARQUIVO_BASE in arquivo_html:
			shutil.copy(arquivo_html,  PATH_DESTINO)

def renomear_arquivo(arquivo):
	data_atual = datetime.date.today()
	novo_nome = f"{data_atual.day -1 } {data_atual.month} {data_atual.year}"
	destino = os.path.join(PATH_DESTINO,novo_nome)
	try:
		os.rename(arquivo,destino)
	except  Exception as e:
		print("Deu ruim",e)
	print(novo_nome)
	#print(datetime.datetime.today().strftime('%d-1 %m %Y'))
renomear_arquivo(os.path.join(PATH_ORIGEM,NOME_ARQUIVO_BASE))