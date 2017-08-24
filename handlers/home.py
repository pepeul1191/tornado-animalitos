#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import requests
import json
from handlers.base import BaseHandler
from config.helper import *
from config.services import *

class HomeIndexHandler(BaseHandler):
	def set_default_headers_nuevo(self):
		print 'set_default_headers!!!!!!!!!!!!!!!!!!!!!'
		self.set_header("Access-Control-Allow-Origin", "*")
		self.logueado()
		self.validar_permisos([3,5])

	def get(self):
		#self.set_default_headers_nuevo()
		#self.set_status(400)
		#self.write("<h1>LOGIN</h1>")
		menu = [
				 {'url' : '#/', 'nombre' : 'Home'},
             {'url' : '#/buscar', 'nombre' : 'Buscar'},
             {'url' : '#/contacto', 'nombre' : 'Contacto'}
      ]
		data = ''
		self.render('animalitos/index.html', helper = Helper(), data = data, menu = json.dumps(menu))