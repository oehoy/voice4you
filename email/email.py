#!/usr/bin/env python									#
# -*- coding: utf-8 -*-		
def main():
	print "EMAILS v.0.1\n"
	while 1:
		comand = raw_input("Введите логин: ")
		if (comand == "find"):
			print "find"
		elif  (comand== "clear") or (comand== "cls"):
			print "cls"
		elif (comand == "delete"):
			print "delete"
		elif  (comand== "help") or (comand== "h"):
			print "delete"
		elif (comand== "exit") or (comand== "quit") or(comand== "q"):
			break
		
if __name__ == '__main__':
	main()
			
