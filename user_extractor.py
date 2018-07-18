import sys, os
import re

#Get path of the folder where output script is available
pathname = os.path.abspath(sys.argv[0])
if len(sys.argv) > 1 :
	pathname = os.path.abspath(sys.argv[1])
print(pathname)
#print(sys.argv[1:])

# ================================================== functions for OS Script ================================================== 
# extract AIX_06 block from file
# return string block of AIX_06
def fetch_AIX_06_block(file):
	script_file = open(os.path.join(file),'r')
	script = script_file.read() 
	# search for pattern AIX_06
	aix_06_finder = re.compile('''
			AIX\_06((\s(.*))*?)\s\-+
	''',re.X)
	aix_06_in_script = aix_06_finder.search(script)
	return 	aix_06_in_script.group(1)

# Extract all the OS users from the string
# return list of user	
def fetch_os_users(string):
	username_finder = re.compile('''
	(.+)\:.*\:.*\:.*\:.*\:.*\:.*
	''',re.X)
	return username_finder.findall(string)

# ================================================== End of functions for OS Script ================================================== 

aix06_block = fetch_AIX_06_block(pathname)
username = fetch_os_users(aix06_block)	

print(username)
	