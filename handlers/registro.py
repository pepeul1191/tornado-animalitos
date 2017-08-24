#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import requests
import json
from handlers.base import BaseHandler
from config.helper import *
from config.services import *

class RegistroValidarCorreoRepetidoHandler(BaseHandler):
	def set_default_headers_nuevo(self):
		print 'set_default_headers!!!!!!!!!!!!!!!!!!!!!'
		self.set_header('Access-Control-Allow-Origin', '*')
		self.logueado()
		self.validar_permisos([3,5])

	def post(self):
		correo = self.get_argument('correo')
		url = Services().get('accesos') + 'usuario/correo_repetido?correo=' + str(correo)
		response = requests.post(url)
		self.write(response.text)

class RegistroValidarUsuarioRepetidoHandler(BaseHandler):
	def set_default_headers_nuevo(self):
		print 'set_default_headers!!!!!!!!!!!!!!!!!!!!!'
		self.set_header('Access-Control-Allow-Origin', '*')
		self.logueado()
		self.validar_permisos([3,5])

	def post(self):
		usuario = self.get_argument('nombre')
		url = Services().get('accesos') + 'usuario/nombre_repetido?usuario=' + str(usuario)
		response = requests.post(url)
		self.write(response.text)