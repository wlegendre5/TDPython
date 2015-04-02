#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Installation as install
import Equipement as equip
import Activite as activ
import database as bd
import time
import json

#On commence par extraire les donnees des fichiers json

installations = install.parseJson("Installations.json")
equipements = equip.parseJson("Equipements.json")
activites = activ.parseJson("Activites.json")

#Creation de la base de donnees

mabdeyy = bd.Database("BD/M4105C.db")

#On effectue des insertions dans la base

#Pour les installations
mabdeyy.create_new("installation", installations[0])
mabdeyy.insert(installations)
mabdeyy.select_all("installation")

#Pour les activites
mabdeyy.create_new("activite", activites[0])
mabdeyy.insert(activites)
mabdeyy.select_all("activite")

#Pour les equipements
mabdeyy.create_new("equipement", equipements[0])
mabdeyy.insert(equipements)




#Affichage de la base dans le terminal

mabdeyy.select_all("installation")

mabdeyy.close()
