#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Services:
	def __init__(self):
		self.diccionario = {
			'accesos' : 'http://127.0.0.1:5001/',
			'maestros' : 'http://127.0.0.1:3001/',
			'gestion' : 'http://127.0.0.1:3002/',
			'cipher' : 'http://127.0.0.1:5000/',
		}

	def get(self, key):
		return self.diccionario[key]