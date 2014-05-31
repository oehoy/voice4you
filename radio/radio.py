#!/usr/bin/env python									#
# -*- coding: utf-8 -*-	
#os.system('mplayer http://xn--80aefq4abio.xn--p1ai:8000&')#run 2
#os.system('mplayer http://listen.radonline.ru:9000/radioonline192&')
import  os, random
servers = ["http://188.138.1.7:9000/753aac-fm-dorognoe", "http://rr.fmtuner.ru/", "http://s1.radioheart.ru:8001/yumor-fm"]
def main():
	print "Voice4You Online Radio v.0.1\n"
	while 1:
		comand = raw_input("Введите название радиостанции: ")
		if (comand == ""):
			os.system('killall mplayer')
			os.system('mplayer ' + random.choice(servers))
		if (comand == "vos") or (comand== "ВОС") or (comand== "вос"):
			os.system('mplayer http://xn--80aefq4abio.xn--p1ai:8000')
		elif (comand== "exit") or (comand== "quit") or(comand== "q"):
			os.system('killall mplayer')
			break
		
if __name__ == '__main__':
	main()
			
