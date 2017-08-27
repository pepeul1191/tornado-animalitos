#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import requests
import json
from handlers.base import BaseHandler
from config.helper import *
from config.services import *

class CorreoMandarHandler(BaseHandler):
	def post(self):
		correo = self.get_argument('correo')
		url = Services().get('backend') + 'correo/mandar?correo=' + correo
		response = requests.post(url)
		self.write(response.text)