#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
from handlers.login import *
from handlers.accesos.usuario import *
from handlers.accesos.session import *

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, world')

routes = [
	(r'/', MainHandler),
	(r'/login', AccesosLoginIndexHandler),
	(r'/usuario/validar_correo_repetido', AccesosUsuarioValidarCorreoRepetidoHandler),
	(r'/usuario/validar_usuario_repetido', AccesosUsuarioValidarUsuarioRepetidoHandler),
	(r'/session/logueado', AccesosSessionLogueadoHandler),
]