#coding=utf-8
import json

with open( 'TOP250','r') as f:
	x=1
	for line in f.readlines():
		if x < 10:
			print(line)
			x = x+1
		else:
			break
