























'''

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


parseJSon("installations.json")




"""
traffic = json.load(open(installations.json))
traffic["data"]


columms = ['Insnom', 'InsNumeroInstall', 'ComLib', 'ComInsee', 'InsCodePostal']
for timestamp, data in traffic.iteritems():
	inst = Installation(data[1], data[2], data
	print inst


traffic = json.load(open("installations.json"))
traffic["data"]

for item in traffic["data"]:
	print(item["ComInsee"])
	
"""
"""
traffic = json.load(open("installations.json"))
traffic["data"]

for item in traffic["data"]:
	inst = Installation(item["InsNumeroInstall"], item["ComLib"], item["ComInsee"], item["InsCodePostal"])
	print (inst)
	
"""

"""
conn = sqlite3.connect('installations.db')

c = conn.cursor()

c.execute("DROP TABLE IF EXISTS installations")


conn.commit()
conn.close()
"""
