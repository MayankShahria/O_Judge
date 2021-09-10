import os

def run_file(f):
	with open('online_judge/files/program.cpp', 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)
	if os.system("g++ online_judge/files/program.cpp -o online_judge/files/program.exe") == 0:
		if os.system("timeout --preserve-status 1 ./out < online_judge/files/TESTinput.txt > output.txt") != 0:
			print("TLE")
		else:
			if os.system("diff output.txt TESToutput.txt") == 0:
				print("AC")
			else:
				print("WA")
	else:
		print("CE")
