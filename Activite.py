#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import codecs

class Activite : 

	def __init__ (self, ComInsee, EquipementId, ActCode) :
		self.ComInsee = ComInsee
		self.EquipementId = EquipementId
		self.ActCode = ActCode

	def __repr__ (self):
		"{} - {} - {} - {}".format(self.ComInsee, self.EquipementId, self.ActCode)

	@property
	def getComInsee(self):
		return str(self.ComInsee)

	@property
	def getEquipementId(self):
		return str(self.EquipementId)

	@property
	def getActCode(self):
		return str(self.ActCode)

	def SQLcreate(self):
		return "CREATE TABLE activite (ComInsee integer, EquipementId integer, ActCode integer)"

	def SQLinsert(self):
		if self.ActCode == None:
			self.ActCode = 0
		return "INSERT INTO activite VALUES({}, {}, {})".format(self.ComInsee, self.EquipementId, self.ActCode)

def parseJson(json_file):
		activites = []
		json_data = codecs.open(json_file, encoding="utf-8").read()
		data = json.loads(json_data)
		for item in data["data"]:
			activites.append(Activite(item["ComInsee"], item["EquipementId"], item["ActCode"]))
		return activites

