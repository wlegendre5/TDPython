#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cherrypy
import Installation
import Equipement 
import Activite
import database as bd


class WebManager(object):

	@cherrypy.expose
	def index(self):
		return '''
		<html><body>
		<h1> Installations sportives des Pays de la loire </h1>
		<input type="button" name="Installations" value="Afficher les installations" onclick="self.location.href='display_Installations'">
		<input type="button" name="Activites" value="Afficher les activites" onclick="self.location.href='display_Activites'">
		<input type="button" name="Installations" value="Afficher les equipements" onclick="self.location.href='display_Equipements'">
		</body></html>
		'''

	@cherrypy.expose
	def display_Installations(self):
		html=""
		database = bd.Database('BD/M4105C.db')
		insts = database.read_Installations()
		html += '''<h2>Tableau des installations</h2>
			 <table>
			 	<tr>
			 		<th>Numéro</th>
			 		<th>ComLib</th>
			 		<th>ComInsee</th>
			 	</tr>\n'''
		for i in insts:
			html += '''<tr>\n
					<td>''' + str(i.InsNumeroInstall) + '''</td>
					<td>''' + i.ComLib + '''</td>
					<td>''' + str(i.ComInsee) + '''</td>
				</tr>'''
		html += '''</table>'''
		return html

	@cherrypy.expose
	def display_Activites(self):
		html = ""
		database = bd.Database('BD/M4105C.db')
		insts = database.read_Activites()
		html += '''<h2>Tableau des activites</h2>
			 <table>
			 	<tr>
			 		<th>ComInsee</th>
			 		<th>EquipementId</th>
			 		<th>ActCode</th>
			 	</tr>\n'''
		for i in insts:
			html += '''<tr>\n
					<td>''' + str(i.ComInsee) + '''</td>
					<td>''' + str(i.EquipementId) + '''</td>
					<td>''' + str(i.ActCode) + '''</td>
				</tr>'''
		html += '''</table>'''
		return html


cherrypy.quickstart(WebManager())