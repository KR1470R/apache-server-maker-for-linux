import os
import sys
get_var = os.environ['SERVER_LINK']
get_var2 = []
for i in get_var:
	get_var2.append(i)
try:
	if get_var2[0] == 'w' and get_var2[1] == 'w' and get_var2[2] == 'w' and get_var2[3] == '.':
		print('True')
	else:
		print('err')
except:
	print('err')
