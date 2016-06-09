#!/usr/bin/env python2
def parse_lines(filename):
	lines = [line.rstrip('\n') for line in open(filename)]
	return lines

def generate_torrc(output):
	f = open(output, "w")
	for tport in range(ports):
		f.write("SocksPort " + parse_lines("ports")[tport] + "\n")
		tports.append(parse_lines("ports")[tport])
	f.close()
	for tport in tports:
		print(tport)
	print("Output written successfully.")
	f = open("torstart.sh", "w")
	f.write("#!/bin/bash\ntor -f " + output)
	f.close()

tports = []
ports = int(raw_input("Amount of ports: "))
generate_torrc("torrc")
