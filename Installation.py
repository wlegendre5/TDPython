import json
import sqlite3

class Installation :

	def __init__ (self, Insnom, InsNumeroInstall, ComLib, ComInsee, InsCodePostal):
		self.Insnom = Insnom
		self.InsNumeroInstall = InsNumeroInstall
		self.ComLib = ComLib
		self.ComInsee = ComInsee
		self.InsCodePostal = InsCodePostal

	def __repr__ (self):
		"{} - {} - {} - {} - {}".format(self.Insnom, self.InsNumeroInstall, self.ComLib, self.ComInsee, self.InsCodePostal)

	@property
	def getInsnom(self):
		return str(self.Insnom)

	@property
	def getInsNumeroInstall(self):
		return str(self.InsNumeroInstall)
	
	@property
	def getComLib(self):
		return str(self.ComLib)

	@property
	def getComInsee(self):
		return str(self.ComInsee)

	@property
	def getInsCodePostal(self):
		return str(self.InsCodePostal)


conn = sqlite3.connect('installations.db')

c = conn.cursor()

c.execute("DROP TABLE IF EXISTS installations")
c.execute('''CREATE TABLE installations
             (Insnom text, InsNumeroInstall text, ComLib text, ComInsee text, InsCodePostal text)''')

conn.commit()
conn.close()

