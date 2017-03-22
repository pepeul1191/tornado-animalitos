#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import requests
from config.helper import *
from config.services import *

class AccesosSessionLogueadoHandler(tornado.web.RequestHandler):
	def set_default_headers(self):
		self.set_header('Access-Control-Allow-Origin', '*')
		self.set_header("Access-Control-Allow-Headers", "x-requested-with")
		self.set_header('Access-Control-Allow-Methods', 'GET')

	def get(self):
		rpta = self.get_secure_cookie('usuario')
		self.write(str(rpta))