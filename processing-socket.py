#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  
'''
FARHAT Oussama
'''
import socketio
import cv2
import base64
import threading 
import time

from socketIO_client import SocketIO, LoggingNamespace
# def on_aaa_response(self, *args):
#     print('on_aaa_response', args)
#     self.emit('bbb')

def on_connect():
    print('connect')

# socketIO.emit('streamEvent')
# socketIO.wait(seconds=1)

# def send_frame(index) : 
#     vid = cv2.VideoCapture(index)
#     while True : 
#         ret, frame = vid.read()
#         retval, buffer = cv2.imencode('.jpg', frame)
#         jpg_as_text = base64.b64encode(buffer)
#         socketIO.emit('streamEvent', {'frame':"test"})
#         time.sleep(5)

if __name__ == "__main__":
    print("test")
    socketIO = SocketIO('http://localhost',5000,wait_for_connection=False)
    socketIO.on('connect', on_connect)
    print("test")
        #socketIO.wait_for_callbacks(seconds=1)
    #socketio
    #socket

    # t1 = threading.Thread(target=send_frame, args=(0,))
    # t1.start()


  

  
