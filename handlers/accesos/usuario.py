#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import requests
from config.helper import *
from config.services import *

class AccesosUsuarioValidarCorreoRepetidoHandler(tornado.web.RequestHandler):
	def prepare(self):
		self.set_header('Access-Control-Allow-Origin', '*')
		self.set_header('Access-Control-Allow-Methods', 'POST')

	def post(self):
		services = Services()
		helper = Helper()

		correo = self.get_argument('correo')

		url = services.get('accesos') + 'usuario/validar_correo_repetido?correo=' + correo
		response = requests.post(url)

		return response.text

class AccesosUsuarioValidarUsuarioRepetidoHandler(tornado.web.RequestHandler):
    def post(self):
		services = Services()
		helper = Helper()

		usuario = self.get_argument('usuario')

		url = services.get('accesos') + 'usuario/validar_usuario_repetido?usuario=' + usuario
		response = requests.post(url)

		return response.text