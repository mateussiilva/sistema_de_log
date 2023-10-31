import pandas as pd
file = r"C:\Users\Usuario\Downloads\PEDIDO INVERNO 2024.xlsx" # File name
# The header is the 2nd row
df = pd.read_excel(file, sheet_name=0)

coluna_seda = df["SEDA"]
for seda in coluna_seda:
	if isinstance(seda, str):
		num = 
		print(seda)
