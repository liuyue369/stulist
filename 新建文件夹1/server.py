# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import os

import reqs
home_path = os.path.dirname(__file__)

settings = {
    "static_path": os.path.join(home_path, "static"),
    "debug": "true"
}

handlers = [
    (r"/", reqs.MainHandler),
    (r"/list", reqs.StudentListHandler),
    (r"/create", reqs.StudentCreateHandler),
    (r"/drop", reqs.StudentDropHandler),
    (r"/change", reqs.StudentChangeHandler),
]
application = tornado.web.Application(handlers, **settings )
application.listen(8888)

if __name__ == '__main__':

    import ioloop
    ioloop.run() # 服务主调度
 
