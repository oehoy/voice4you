#!/usr/bin/env python									#
# -*- coding: utf-8 -*-									#
#														#
#       voice4u.py										#
#       												#
#       Copyright 2014 Oehoy <popov.md5@gmail.com>		#
#														#
#########################################################  
import curses, os 
screen = curses.initscr() 
curses.noecho()
curses.cbreak()
curses.start_color()
screen.keypad(1)
curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE) 
getin = None 
sub1get = None 
sub2get = None 
def topmenu():
  screen.keypad(1)
  curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE)
  pos=1 
  x = None 
  h = curses.color_pair(1) #h 
  n = curses.A_NORMAL #n 
  while x !=ord('\n'):
    screen.clear() 
    screen.border(0)
    screen.addstr(2,2, "\"Voice For You\"", curses.A_STANDOUT) # Title for this menu
    screen.addstr(4,2, "Please select it...", curses.A_BOLD) #Subtitle for this menu
    if pos==1:
      screen.addstr(6,4, "1. Wikipedia", h)
      #os.system("echo \"В+ики\" | festival --tts --language russian")
    else:
      screen.addstr(6,4, "1. Wikipedia", n)
    if pos==2:
      screen.addstr(7,4, "2. Online radio", h)
      #os.system("echo \"Перев+одчик\" | festival --tts --language russian")
    else:
      screen.addstr(7,4, "2. Online radio", n)
    if pos==3:
      screen.addstr(8,4, "3. E-mail", h)
      #os.system("echo \"Р+адио\" | festival --tts --language russian")
    else:
      screen.addstr(8,4, "3. E-mail", n)
    if pos==4:
      screen.addstr(9,4, "4. QIWI Shop", h)
      #os.system("echo \"П+очта\" | festival --tts --language russian")
    else:
      screen.addstr(9,4, "4. QIWI Shop", n)
      #os.system("echo \"Электр+онная почта\" | festival --tts --language russian")
    if pos==5:
      screen.addstr(10,4, "5. Exit", h)
      #os.system("echo \"В+ыход\" | festival --tts --language russian")
    else:
      screen.addstr(10,4, '5. Exit', n)
    screen.refresh()
    x = screen.getch() 
    if x == ord('1'):
      pos = 1
    elif x == ord('2'):
      pos = 2
    elif x == ord('3'):
      pos = 3
    elif x == ord('4'):
      pos = 4
    elif x == ord('5'):
      pos = 5
    elif x == 258:
  
      if pos < 5:
        pos += 1
      else: pos = 1
    elif x == 259:
      if pos > 1:
        pos += -1
      else: pos = 5
    elif x != ord('\n'):
      curses.flash()
  return ord(str(pos))
 
# Main program  
while getin != ord('5'):
  getin = topmenu() # Get the menu item selected on the top menu
  if getin == ord('1'):
	  curses.endwin()
	  os.system('clear && python ./wikipedia/wiki.py')#run    
  elif getin == ord('2'): # Topmenu option 2
	  curses.endwin()
	  os.system('clear && python ./radio/radio.py')
  elif getin == ord('3'): # Topmenu option 3
	  curses.endwin()
	  os.system('clear && python ./email/email.py')
  elif getin == ord('4'): # Topmenu option 
	  curses.endwin()
	  os.system('clear && python ./qiwi/qiwi_shop.py')
	   #run 4
  elif getin == ord('5'): # Topmenu option 4
	  curses.endwin() #VITAL!  This closes out the menu system and returns you to the bash prompt.
    
    
    
