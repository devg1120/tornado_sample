#!/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import tornado.ioloop
import tornado.web

import json
import time

import random

import tornado.websocket


class SendWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print ('Session Opened. IP:' + self.request.remote_ip)
        self.ioloop = tornado.ioloop.IOLoop.instance()
        self.send_websocket()

    def on_close(self):
        print("Session closed")

    def check_origin(self, origin):
        return True

    def send_websocket(self):
        self.ioloop.add_timeout(time.time() + 0.1, self.send_websocket)
        if self.ws_connection:
            message = json.dumps({
                'data1': random.randint(0, 100),
                'data2': random.randint(0, 100),
                })
            self.write_message(message)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

ap = tornado.web.Application([
     (r"/", MainHandler)
    ],
    template_path=os.path.join(os.getcwd(),  "templates"),
    static_path=os.path.join(os.getcwd(),  "static"),
)

ws = tornado.web.Application([
     (r"/ws/display", SendWebSocket)
    ]
)

if __name__ == "__main__":
    ap.listen(8888)
    ws.listen(8889)
    print("Server is up ...")
    tornado.ioloop.IOLoop.instance().start()


