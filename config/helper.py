#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from config.services import *

class Helper:
	def __init__(self):
		services = Services()

		self.diccionario = {
			'BASE_URL': 'http://localhost:8888/',
			'STATICS_URL' : 'http://localhost:8001/dashboard/',
			'accesos' : services.get('accesos'),
			'ambiente': 'desarrollo',
			'nombre_app' : 'Aplicación Python Tornado',
			'cipher_key' : 's53hHaKFQoqXTDU9' 
		}

	def listar_modulos(self):
		url = self.get('accesos') + "modulo/listar"
		response = requests.get(url)
		return response.text

	def listar_menu(self, modulo):
		url = self.get('accesos') + "item/listar/menu/" + modulo
		response = requests.get(url)
		return response.text

	def set(self, key, value):
		self.diccionario[key] = value

	def get(self, key):
		return self.diccionario[key]

	def array_to_json(self, string):
		rpta = []
		temps = json.loads(string)

		for temp in temps:
			rpta.append(json.loads(temp))

		return rpta
