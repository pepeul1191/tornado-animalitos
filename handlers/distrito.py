#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import requests
import json
from handlers.base import BaseHandler
from config.helper import *
from config.services import *

class DistritoBuscarHandler(BaseHandler):
	def get(self):
		nombre = self.get_argument('nombre')
		url = Services().get('backend') + 'distrito/buscar?nombre=' + str(nombre)
		response = requests.get(url)
		self.write(response.text)