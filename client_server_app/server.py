# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 23:15:59 2021

@author: danie
"""

import socket
from datetime import datetime

def log(logs):
    now = datetime.now().strftime("%H:%M:%S")
    print("{} || {}".format(now, logs))

class Server:
    
    def __init__(self, host="127.0.0.1", port=65432):
        self.host = host
        self.port = port
    
    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            received = None
            log('Receiving logs...')
            while received != b'close':
                s.listen()
                conn, addr = s.accept()
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)
    
    def receive_data(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            log('Starting...')
            while True:
                s.listen()
                conn, addr = s.accept()
                data = conn.recv(1024)
                data = data.decode("utf-8")
                log(data)
    
if __name__ == '__main__':
    server = Server()
    server.receive_data()