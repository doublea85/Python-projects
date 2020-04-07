import pyqrcode
import pandas as pd

def  createQRCode():
	df = pd.read_csv("/home/arcanum/Téléchargements/TP/Python/CSV/client.csv")
	
	for index, values in df.iterrows():

		idclient = values["idcli"]
		nomclient = values["nomcli"]
		vilclient = values["vilcli"]
		telclient = values["telcli"]

		data = f'''

		ID:{idclient} \n
		Nom: {nomclient} \n
		Ville: {vilclient} \n
		Tel: {telclient}
		'''
		image = pyqrcode.create(data)
		image.svg(f"{idclient}_{vilclient}.svg", scale="5")



createQRCode()