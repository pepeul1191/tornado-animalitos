#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import tornado.httpserver
from config.settings import settings

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world??")

if __name__ == "__main__":
	application = tornado.web.Application([
		(r"/", MainHandler),
	])
		
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(8888)
	tornado.ioloop.IOLoop.current().start()