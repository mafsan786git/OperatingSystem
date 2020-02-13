#MOHD AFSAN AHMAD
#CSB=55
#12180058
#ONE WAY

import os,sys
r,w = os.pipe()

processId = os.fork()

#st = input('enter string\n')
if processId:

	os.close(r)
	f = os.fdopen(w,'w')
	h,m = map(int,input('enter time : ').split(':'))
	#print()
	#print('PID = ',os.getpid(),'started writing ..')
	f.write(str(h))
	#print('PID = ',os.getpid(),'writing completed ..')
	
else:
	os.close(w)
	f = os.fdopen(r)
	l = f.read()
	h = int(l)
	
	if h<12:
		print('Good Morning...')
	elif h<16:
		print('Good Afternoon...')
	elif h<20:
		print('Good Evening...')
	elif h > 24:
		print('Invalid time...')
	else:
		print('Good Night...')
		
		
'''
enter time : 15:56
Good Afternoon...
enter time : 16:00
Good Evening...
enter time : 11:59
Good Morning...
enter time : 23:59
Good Night...
'''
