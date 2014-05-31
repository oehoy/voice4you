#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Topmenu and the submenus are based of the example found at this location http://blog.skeltonnetworks.co…..stom-menu/
# The rest of the work was done by Matthew Bennett and he requests you keep these two mentions when you reuse the code 
import curses, os #curses is the interface for capturing key presses on the menu, os launches the files
screen = curses.initscr() #initializes a new window for capturing key presses
curses.noecho()
curses.cbreak()
curses.start_color() # Lets you use colors when highlighting selected menu option
screen.keypad(1) # Capture input from keypad
# Change this to use different colors when highlighting
curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE) # Sets up color pair #1, it does black text with white background
getin = None #user input on top menu
sub1get = None #user input on sub menu 1
sub2get = None #user input on sub menu 2, I don't use a second submenu, but I've left this here as an example for anyone who wants to use it
# This function controls what is displayed on the top menu (the menu first loaded when script is run)
def topmenu():
#Not sure if the following two lines are needed since I declare it at beginning of program, but here for safety
  screen.keypad(1)
  curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE)
  pos=1 #pos is the position of the hightlighted menu option.  Every time topmenu is calles, position retuns to 1, when topmenu ends the position is returned tell program what option has been selected
  x = None #contol for while loop, let's you scroll through options until return key is pressed then returns pos to program
  h = curses.color_pair(1) #h is the coloring for a highlighted menu option
  n = curses.A_NORMAL #n is the coloring for a non highlighted menu option
  # Loop until return key is pressed
  while x !=ord('\n'):
    screen.clear() #clears previous screen on key press and updates display based on pos
    screen.border(0)
    screen.addstr(2,2, "\"Voice For You\"", curses.A_STANDOUT) # Title for this menu
    screen.addstr(4,2, "Please select it...", curses.A_BOLD) #Subtitle for this menu
    # Detects what is higlighted, every entry will have two lines, a condition if the menu is highlighted and a condition for if the menu is not highlighted
    # to add additional menu options, just add a new if pos==(next available number) and a correspoonding else
    # I keep exit as the last option in this menu, if you do the same make sure to update its position here and the corresponding entry in the main program
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
      screen.addstr(8,4, "3. QIWI Shop", h)
      #os.system("echo \"Р+адио\" | festival --tts --language russian")
    else:
      screen.addstr(8,4, "3. QIWI Shop", n)
    if pos==4:
      screen.addstr(9,4, "4. E-mail", h)
      #os.system("echo \"П+очта\" | festival --tts --language russian")
    else:
      screen.addstr(9,4, "4. E-mail", n)
      #os.system("echo \"Электр+онная почта\" | festival --tts --language russian")
    if pos==5:
      screen.addstr(10,4, "5. Exit", h)
      #os.system("echo \"В+ыход\" | festival --tts --language russian")
    else:
      screen.addstr(10,4, '5. Exit', n)
    screen.refresh()
    x = screen.getch() # Gets user input
    # What is user input? This needs to be updated on changed equal to teh total number of entries in the menu
    # Users can hit a number or use the arrow keys make sure to update this when you add more entries
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
    
    # This needs to be updated on changes to equal the total number of entries in the menu
      if pos < 5:
    # This doesn't need to be changed no matter how many entries you have
        pos += 1
      else: pos = 1
    elif x == 259:
      if pos > 1:
        pos += -1
  # This needs to be updated on changes to equal the total number of entries in the menu
      else: pos = 5
    elif x != ord('\n'):
      curses.flash()
  return ord(str(pos))
 
# Main program  
# This needs to be updated on changes equal to the number you use for exit
while getin != ord('5'): #Loop until the user choses to exit the program
  getin = topmenu() # Get the menu item selected on the top menu
  if getin == ord('1'):
	  os.system('')#run    
  elif getin == ord('2'): # Topmenu option 2
    #os.system('mplayer http://xn--80aefq4abio.xn--p1ai:8000&')#run 2
    os.system('mplayer http://listen.radonline.ru:9000/radioonline192&')
  elif getin == ord('3'): # Topmenu option 3
    os.system('python') #run 3
  elif getin == ord('4'): # Topmenu option 3
    os.system('') #run 4
  elif getin == ord('5'): # Topmenu option 4
    curses.endwin() #VITAL!  This closes out the menu system and returns you to the bash prompt.
    
    
    
