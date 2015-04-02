#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import codecs

class Equipement :

	def __init__ (self,InsNumeroInstall,EquipementId,ComInsee,EquNom):

		self.InsNumeroInstall = InsNumeroInstall
		self.EquipementId = EquipementId
		self.ComInsee = ComInsee
		self.EquNom = EquNom

	def __repr__ (self):
		"{} - {} - {} - {}". format(self.InsNumeroInstall, self.EquipementId, self.ComInsee, self.EquNom)

	@property
	def getComInsee(self):
		return str(ComInsee)

	@property
	def getInsNumeroInstall(self):
		return str(InsNumeroInstall)

	@property
	def getEquipementId(self):
		return str(EquipementId)

	@property
	def getEquNom(self):
		return str(EquNom)

	def SQLcreate(self):
		return "CREATE TABLE equipement (InsNumeroInstall integer, EquipementId integer, ComInsee integer, EquNom varchar)"
		
	def SQLinsert(self):
		return "INSERT INTO equipement VALUES({}, {}, {}, {})".format(self.InsNumeroInstall, self.EquipementId, self.ComInsee, "\'"+self.EquNom+"\'"	)

def parseJson(json_file):
	equipments = []
	json_data = codecs.open(json_file, encoding="utf-8").read()
	data = json.loads(json_data)
	for item in data["data"]:
		equipments.append(Equipement(item["InsNumeroInstall"], item["EquipementId"], item["ComInsee"], item["EquNom"]))
	return equipments	