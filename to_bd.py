import sqlite3
import json
from Installation import Installation

def parseJSon(FileName):
	#On charge le fichier JSON
	traffic = json.load(open(FileName))
	traffic["data"]
	tab = []

	#Afficher le premier element
	#print(traffic["data"][0])

	#On parcourt le fichier JSON à l'aide d'une boucle
	for item in traffic["data"]:
		tab.append(
			Installation(item["InsNumeroInstall"],
					     item["ComLib"],
					     item["ComInsee"],
					     item["InsCodePostal"])
		)
	
	return tab


def init_bd_install(self):

	conn = sqlite3.connect('installations.db')
	c = conn.cursor()

	c.execute("DROP TABLE IF EXISTS installations")
	c.execute('''CREATE TABLE installations
	             (InsNumeroInstall integer, ComLib text, ComInsee text, InsCodePostal integer)''')

	conn.commit()
	conn.close()



def write_bd(self):

	conn = sqlite3.connect('installations.db')
	c = conn.cursor()








"""
def parseJSon (FileName) : 
traffic= json.load(open(FileName)) 
traffic["data"] 
installations = [] 
for item in traffic["data"]:
 #print(item["Insnom"]) 
 #Un item en particulier #print (item) 
 # toute la ligne
installations.append(Installation(item['InsNumeroInstall'],item['ComLib'],item['ComInsee'],item['InsCodePostal'])) 
return installations
 	"""