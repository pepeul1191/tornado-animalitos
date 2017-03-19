#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import tornado.httputil
import pprint

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class LoginHandler(tornado.web.RequestHandler):
	def prepare(self):
		if 2 == 3:
			self.redirect('/')

	def get(self):
		self.request.headers
		self.write("<h1>LOGIN</h1>")

routes = [
	(r"/", MainHandler),
	(r"/login", LoginHandler)
]