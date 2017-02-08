# -*- coding: utf-8 -*-

import os
import sys
#from tkinter import *

if __name__ == "__main__":
	# if len(sys.argv) < 3:
		# sys.stderr.write('Not enough arguments')
		# sys.exit()
	
	# try:
		# with open(sys.argv[1], 'rb') as file:
			# lines = file.readlines()
	# except IOError as error:
		# print(error)
		
	# try:
		# with open(sys.argv[2], 'rb') as file:
			# carre = file.readlines()
	# except IOError as error:
		# print(error)
		
	try:
		with open('source.txt', 'rb') as file:
			lines = file.readlines()
	except IOError as error:
		print(error)
	
	carre = input(u'Enter x,y left bottom and x,y right top (example: 1,2,4,5):')
	step = int(input(u'Enter step diagonal (example: 2):'))
	
	carre = carre.split(',')
	points = []
	in_carre = []
	on_carre = []
	on_diagonal_45 = []
	on_diagonal_135 = []
	vertical = []
	horizontal = []
	#x_max = 0
	#y_max = 0
	# canvas = Canvas(width=800, height=600, bg='white')
	# canvas.pack(expand=YES, fill=BOTH)
	
	for line in lines:
		in_range = False
		x, y = line.decode('utf8').strip().split(":")
		#x_max = max(x_max, int(x))
		#y_max = max(y_max, int(y))
		
		# canvas.create_line(x, y, x, y)
		
		if int(x) > int(carre[0]) and int(y) > int(carre[1]) and int(x) < int(carre[2]) and int(y) < int(carre[3]):
			in_carre.append((x, y))
			in_range = True
		elif ((int(x) == int(carre[0]) or int(x) == int(carre[2])) and int(y) >= int(carre[1]) and int(y) <= int(carre[3])) or ((int(y) == int(carre[1]) or int(y) == int(carre[3])) and int(x) >= int(carre[0]) and int(x) <= int(carre[2])):
			on_carre.append((x, y))
			in_range = True
		
		for y0 in range(int(carre[1]), int(carre[3]), step):
			if (int(y) - y0) == (int(x) - int(carre[0])) and in_range:
				on_diagonal_45.append((x, y))
				
		for x0 in range(int(carre[0]) + step, int(carre[2]), step):
			if (int(y) - int(carre[1])) == (int(x) - x0) and in_range:
				on_diagonal_45.append((x, y))
				
		for y0 in range(int(carre[1]), int(carre[3]), step):
			if (int(y) - y0) == -1 * (int(x) - int(carre[0])) and in_range:
				on_diagonal_135.append((x, y))
				
		for x0 in range(int(carre[0]), int(carre[2]), step):
			if (int(y) - int(carre[3])) == -1 * (int(x) - x0) and in_range:
				on_diagonal_135.append((x, y))
				
		for y0 in range(int(carre[1]), int(carre[3]), step):
			if int(y) == y0 and in_range:
				horizontal.append((x, y))
				
		for x0 in range(int(carre[0]), int(carre[2]), step):
			if int(x) == x0 and in_range:
				vertical.append((x, y))
	
	# canvas.create_line(10, 10 + y_max, x_max, 10 + y_max)
	# canvas.create_line(10, 10, 10, y_max)
	
	print("In carre: %s" % in_carre)
	print("Count: %d" % len(in_carre))
	print("----------------------------------------------------------")
	print("On carre: %s" % on_carre)
	print("Count: %d" % len(on_carre))
	print("----------------------------------------------------------")
	print("On diagonal 45: %s" % on_diagonal_45)
	print("Count: %d" % len(on_diagonal_45))
	print("----------------------------------------------------------")
	print("On diagonal 135: %s" % on_diagonal_135)
	print("Count: %d" % len(on_diagonal_135))
	print("----------------------------------------------------------")
	print("On horizontal: %s" % horizontal)
	print("Count: %d" % len(horizontal))
	print("----------------------------------------------------------")
	print("On vertical: %s" % vertical)
	print("Count: %d" % len(vertical))
	input("\nPress the enter key to exit.")
