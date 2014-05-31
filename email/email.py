#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
import wikipedia 

def main():
	print "Wikipedia Voice4You v.0.1\n"
	wikipedia.set_lang("ru")
	while 1:
		comand = raw_input("Введите название статьи: ")
		if (comand != "exit"):
			try:
				text = wikipedia.page(comand)
				print text.content
				print "*"*100+"\n\n"
			except:
				print "Статья не найдена"
				print "*"*100+"\n\n"
		elif (comand == "exit") or (comand== "quit") or(comand== "q"):
			break
	
	return 0

if __name__ == '__main__':
	main()

