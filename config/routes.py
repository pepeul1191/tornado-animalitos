#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
from handlers.home import *

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, world')

routes = [
	#home
	(r'/', HomeIndexHandler),
]