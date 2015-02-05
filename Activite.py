import json

class Activite : 

	def __init__ (self, ComInsee, ComLib, EquipementId, ActCode) :
		self.ComInsee = ComInsee
		self.ComLib = ComLib
		self.EquipementId = EquipementId
		self.ActCode = ActCode

	def __repr__ (self):
		"{} - {} - {} - {}".format(self.ComInsee, self.ComLib, self.EquipementId, self.ActCode)

	@property
	def getComInsee(self):
		return str(self.ComInsee)

	@property
	def getComLib(self):
		return str(self.ComLib)

	@property
	def getEquipementId(self):
		return str(self.EquipementId)

	@property
	def getActCode(self):
		return str(self.ActCode)