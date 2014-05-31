#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wikipedia 

def main():
	wikipedia.set_lang("ru")
	text = wikipedia.page("Глагол")
	print text.content
	return 0

if __name__ == '__main__':
	main()

