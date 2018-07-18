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
	script_file = open(file,'r')
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

#aix06_block = fetch_AIX_06_block(pathname)
#username = fetch_os_users(aix06_block)	

#print(username)

# ================================================== functions for DB Script ================================================== 
# Extract ORA_U11g_05_STARTS block
def fetch_ORA_U11g_05_block(file):
	startWith = "ORA_U11g_05_STARTS"
	endWith = "ORA_U11g_05_ENDS"
	script_file = open(file,'r')
	script = script_file.read() 
	#print(script)
	# required string extraction
	return script[ script.find(startWith): (script.find(startWith)+script.find(endWith))]
	
def fetch_db_user(string):
	username_finder = re.compile('''
		(.+)\s*\|(EXPIRED|LOCKED|OPEN)
	''',re.X)
	username_list = username_finder.findall(string)
	usernames = []
	for index in range(len(username_list)):
		usernames.append(username_list[index][0].strip())
	return usernames
# ================================================== End of functions for DB Script ================================================== 

ora_block = fetch_ORA_U11g_05_block(pathname)
usernames = fetch_db_user(ora_block)

print(usernames)	