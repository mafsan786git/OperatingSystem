



process = []

def readinput():
	global n
	mat = []
	n = int(input("enter number of process : "))
	print ("enter arival time for all process ")
	for i in range(n):
		nm = 'P'+str(i+1)
		at = int(input('Enter arrival time {} : '.format(i+1)))
		bt = int(input('Enter burst time {} : '.format(i+1)))
		mat.append(nm)
		mat.append(at)
		mat.append(bt)
		#print(mat)
		process.append(mat)
		mat = []
	print ("enter all process ")
	print('PID\tAT\tBT')
	for i in range(n):
		for j in range(3):
			print(process[i][j],end = '\t')
		print()
		
def waiting():
	rem = [0]*n
	global comp,turn,wait
	comp = [0]*n
	turn = []
	wait = [0]*n
	for i in range(n):
		rem[i] = process[i][2]
	t = 0
	complete = 0
	check = False
	minm = 9999
	short = 0
	
	while(complete !=n):
		for i in range(n):
			if(process[i][1] <=t and rem[i] < minm and rem[i] > 0):
				minm = rem[i]
				short = i
				check = True
		
		if(check == False):
			t = t+1
			continue
		
		rem[short] -=1
		minm = rem[short]
		
		if(minm == 0):
			minm = 9999
		
		if(rem[short] == 0):
			complete +=1
			check = False
			
			finaltime = t+1
			comp[short] = finaltime
			
			wait[short] = (finaltime - process[short][1]-process[short][2])
			if(wait[short] < 0):
				wait[short] = 0
		t = t+1
		


def turnaround():
	for i in range(n):
		turn.append(comp[i]-process[i][1])

def average():
	global sumt,sumw,avgt,avgw
	sumt = sum(turn)
	sumw = sum(wait)
	avgt = sumt/float(n)
	avgw = sumw/float(n)

def Output():
	print('PID\tAT\tBT\tCT\tTAT\tWT')
	for i in range(n):
		for j in range(3):
			print(process[i][j],end = '\t')
		
		print(comp[i],'\t',turn[i],'\t',wait[i])
	print('Average Turn Around Time : ',avgt)
	print('Average Waiting Time : ',avgw)

def main():
	readinput()
	waiting()
	turnaround()
	average()
	Output()
main()
			
	
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
