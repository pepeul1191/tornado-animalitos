#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import tornado
import tornado.template
import os
from tornado.options import define, options

tornado.options.parse_command_line()

define("port", default=8888, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")
define("debug", default=False, help="debug mode")

path = lambda root,*a: os.path.join(root, *a)

ROOT = os.path.dirname(os.path.abspath(__file__ + "/.."))
MEDIA_ROOT = path(ROOT, 'media')
TEMPLATE_ROOT = path(ROOT, 'templates')

settings = {}
settings['debug'] = True
settings['static_path'] = MEDIA_ROOT
settings['cookie_secret'] = "your-cookie-secret"
settings['xsrf_cookies'] = False
settings['template_loader'] = tornado.template.Loader(TEMPLATE_ROOT)


if options.config:
    tornado.options.parse_config_file(options.config)