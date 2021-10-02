# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 19:12:51 2021

@author: danie
"""

#Import libraries
from optparse import OptionParser
from socket_classes import Send, Receive

#Define options for script
parser = OptionParser()
parser.add_option("--Host", dest="host", type="string", help="Host IP address")
parser.add_option("--Port", dest="port", type="int", help="Port to listen")
options, args = parser.parse_args()

#Define mandatory options
mandatory = ["host", "port"]
for m in mandatory:
    if options.__dict__[m] is None:
        parser.print_help()
        parser.error('Option "{}" is mandatory'.format(m))

#Run server
if __name__ == '__main__':
    s = Send(options.host, options.port)
    r = Receive(options.host, options.port)
    r.receive_data()