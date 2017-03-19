#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class LoginHandler(tornado.web.RequestHandler):
	def prepare(self):
		#self.set_header("Server", "Python")
		if 2 == 3:
			self.redirect('/')

	def get(self):
		self.set_status(400)
		self.write("<h1>LOGIN</h1>")

routes = [
	(r"/", MainHandler),
	(r"/login", LoginHandler)
]