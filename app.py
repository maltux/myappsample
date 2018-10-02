#Tic Tac Toe game

import os
import time
import random

#define the board
board =[" "," "," "," "," "," "," "," "," "," "]
#
#login
#print the header

def print_header():
    print"""

    _______   _   ____      ______     ___     ____       ______    _____    _______
   /__   __\ / \ /  ___\   /__  __\   / _ \   /  __\     /__  __\  /  _  \  /  ____/
      | |    | | | |          | |    / /_\ \  | |          | |     | | | |  | |__
      | |    | | | |     -    | |    |  _  |  | |     -    | |     | | | |  |  __|
      | |    | | | |___       | |    | | | |  | |___       | |     | |_| |  | |____
      |_|    |_| \____/       |_|    |_| |_|  \____/       |_|     \_____/  |______/


                                    1 | 2 | 3
                                   --- --- ---
                                    4 | 5 | 6
                                   --- --- ---
                                    7 | 8 | 9



      """

#Define the header board
def print_board():
    print "    |   |   "
    print " "+board[1]+"  | "+board[2]+" |  "+board[3]+"  "
    print "    |   |   "
    print " ---|---|---   "
    print "    |   |   "
    print " "+board[4]+"  | "+board[5]+" |  "+board[6]+"  "
    print "    |   |    "
    print " ---|---|---"
    print "    |   |   "
    print " "+board[7]+"  | "+board[8]+" |  "+board[9]+"  "
    print "    |   |   "


#Main loop
1

while True:
    os.system("clear")
    print_header()
    print_board()


    choice = raw_input("Please choose an empty space for X. ")
    choice = int(choice)


    #check to see if space is empty
    if board[choice] == " ":
        board[choice] = "X"
    else:
        print "Sorry that space is not empty"
        time.sleep(1)
