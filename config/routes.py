#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
from handlers.home import *
from handlers.registro import *
from handlers.distrito import *
from handlers.correo import *

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, world')

routes = [
	#home
	(r'/', HomeIndexHandler),
	(r'/distrito/buscar', DistritoBuscarHandler),
	(r'/registro/validar_correo_repetido', RegistroValidarCorreoRepetidoHandler),
	(r'/registro/validar_usuario_repetido', RegistroValidarUsuarioRepetidoHandler),
	(r'/registro/guardar_usuario', GuardarUsuarioHandler),
	(r'/correo/mandar', CorreoMandarHandler),
]