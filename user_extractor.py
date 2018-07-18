import sys, os


#Get path of the folder where output script is available
pathname = os.path.abspath(sys.argv[0])
if len(sys.argv) > 1 :
	pathname = os.path.abspath(sys.argv[1])
#print(pathname)