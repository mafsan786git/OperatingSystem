#MOHD AFSAN AHMAD
#CSB=55
#12180058
#TWO WAY

import os
import math

r1,w1 = os.pipe()
r2,w2 = os.pipe()

process = os.fork()

if process:
	os.close(r1)
	
	number = input('enter number : ')
	f = os.fdopen(w1,'w')
	f.write(str(number))
	os.close(w2)
	f = os.fdopen(r2)
	num = f.read()
	print(num)
	
else:
	os.close(w1)
	f = os.fdopen(r1)
	num = f.read()
	number = []
	n = map(int,num.split(','))
	#print(type(n))
	ans = ""
	ansflag = False
	for x in n:
		flag = True
		for i in range(2,int(math.sqrt(x))+1):
			if x%i == 0:
				flag = False
				break;
		if flag:
			ans+=str(x)+" "
			ansflag = True
	if ansflag:
		os.close(r2)
		f = os.fdopen(w2,'w')
		f.write(ans)
	
		
'''
enter number : 12,13,11,3,5
13 11 3 5 
enter number : 12,2,3
2 3
'''
	
