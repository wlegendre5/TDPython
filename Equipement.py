import json

class Equipement :

	def __init__ (self, ComInsee,ComLib,InsNumeroInstall,EquipementId,EquNom):
		self.ComInsee = ComInsee
		self.ComLib = ComLib
		self.InsNumeroInstall = InsNumeroInstall
		self.EquipementId = EquipementId
		self.EquNom = EquNom

	def __repr__ (self):
		"{} - {} - {} - {} - {}". format(self.ComInsee, self.ComLib, self.InsNumeroInstall, self.EquipementId, self.EquNom)

	@property
	def getComInsee(self):
		return str(ComInsee)

	@property
	def getComInsee(self):
		return str(ComLib)

	@property
	def getComInsee(self):
		return str(InsNumeroInstall)

	@property
	def getComInsee(self):
		return str(EquipementId)

	@property
	def getComInsee(self):
		return str(EquNom)