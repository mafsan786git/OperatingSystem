#MOHD AFSAN AHMAD
#CSB=55
#12180058
#ROUND ROBIN



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
	#process[i][1] <=t and
	i=0
	while(complete !=n):
		
		temp = rem[i%n]
		if(temp <= 0):
			i=i+1
			continue
			
		rem[i%n]-=5
		
		if(rem[i%n] > 0):
			t = t+5
			i=i+1
			continue
		
		t = t+temp
		#minm = rem[short]
		
		complete +=1
		
		finaltime = t
		comp[i%n] = finaltime
		
		wait[i%n] = (finaltime-process[i%n][2])
		if(wait[i%n] < 0):
			wait[i%n] = 0
		i = i+1
		


def turnaround():
	for i in range(n):
		turn.append(comp[i])

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
			
	
#OUTPUT

'''
enter number of process : 4
enter arival time for all process 
Enter arrival time 1 : 0
Enter burst time 1 : 21
Enter arrival time 2 : 0
Enter burst time 2 : 3
Enter arrival time 3 : 0
Enter burst time 3 : 6
Enter arrival time 4 : 0
Enter burst time 4 : 2
enter all process 
PID	AT	BT
P1	0	21	
P2	0	3	
P3	0	6	
P4	0	2	
PID	AT	BT	CT	TAT	WT
P1	0	21	32 	 32 	 11
P2	0	3	8 	 8 	 5
P3	0	6	21 	 21 	 15
P4	0	2	15 	 15 	 13
Average Turn Around Time :  19.0
Average Waiting Time :  11.0

'''	 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
