#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import requests
import datetime
import json
from handlers.base import BaseHandler
from config.helper import *
from config.services import *

class LoginIndexHandler(BaseHandler):
	def set_default_headers_nuevo(self):
		print 'set_default_headers!!!!!!!!!!!!!!!!!!!!!'
		self.set_header("Access-Control-Allow-Origin", "*")
		self.logueado()
		self.validar_permisos([3,5])

	def get(self):
		#self.set_default_headers_nuevo()
		#self.set_status(400)
		#self.write("<h1>LOGIN</h1>")
		helper = Helper()
		self.render('login/index.html', mensaje = 'false', helper=helper)

class LoginAccederHandler(BaseHandler):
	def post(self):
		services = Services()
		helper = Helper()
		'''
		usuario = self.get_argument('usuario')
		contrasenia =  requests.post(services.get('cipher') + 'encode?key=' + helper.get('cipher_key') + '&texto=' + str(self.get_argument('contrasenia'))).text
		
		url = services.get('accesos') + 'usuario/validar?usuario=' + str(usuario) + '&contrasenia=' + str(contrasenia)
		response = requests.post(url)
		#print response.text
		if str(response.text) == '1':
			temp = requests.get(services.get('token') + 'generar?usuario=' + str(usuario))
			token = json.loads(temp.text)
			rpta = {'token' : token['mensaje'][0], 'existe' : 1}
		else:
			rpta = {'existe' : 0}
		#print json.dumps(rpta)
		self.write(json.dumps(rpta))
		'''
		usuario = self.get_argument('usuario')
		contrasenia = self.get_argument('contrasenia')

		if usuario == 'pepe' and contrasenia == 'kiki123':
			self.redirect(helper.get('BASE_URL'))
		else:
			self.render('login/index.html', mensaje = 'true', helper=helper)