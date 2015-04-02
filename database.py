#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
from Installation import Installation
from Activite import Activite

class Database:

	def __init__(self, path):
		self.conn = sqlite3.connect(path)
		self.path = path

	def create_new(self, name, item):
		c = self.conn.cursor()
		c.execute("DROP TABLE IF EXISTS " + name)
		c.execute(item.SQLcreate())
		self.conn.commit()

	def insert(self, items):
		c = self.conn.cursor()
		for item in items:
			c.execute(item.SQLinsert())
		self.conn.commit()

	def select_all(self, name):
		c = self.conn.cursor()
		for row in c.execute("SELECT * FROM " + name):
			print (row)

	def close(self):
		self.conn.close()

	def read_Installations(self):
		c = self.conn.cursor()
		c.execute('SELECT * FROM installation')
		result = c.fetchall()
		installations = []

		for i in result:
			installations.append(Installation(i[0], i[1], i[2]))
		return installations

	def read_Activites(self):
		c = self.conn.cursor()
		c.execute('SELECT * FROM activite')
		result = c.fetchall()
		activites = []

		for i in result:
			activites.append(Activite(i[0], i[1], i[2]))
		return activites





	
