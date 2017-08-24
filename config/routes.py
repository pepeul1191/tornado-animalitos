#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
from handlers.home import *
from handlers.registro import *

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, world')

routes = [
	#home
	(r'/', HomeIndexHandler),
	(r'/registro/validar_correo_repetido', RegistroValidarCorreoRepetidoHandler),
	(r'/registro/validar_usuario_repetido', RegistroValidarUsuarioRepetidoHandler)
]