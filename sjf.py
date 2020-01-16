#MOHD AFSAN AHMAD
#CSB=55
#12180058
#SHORTEST JOB FIRST

global comp,turn,wait,process
comp = []
turn = []
wait = []
process = []


def readinput():
	global n
	mat = []
	n = int(input("enter number of process : "))
	print ("enter arival time for all process ")
	for i in range(n):
		nm = 'P'+str(i+1)
		at = int(input('Enter arrival time : '))
		bt = int(input('Enter arrival time : '))
		mat.append(nm)
		mat.append(at)
		mat.append(bt)
		#print(mat)
		process.append(mat)
		mat = []
	print ("enter all process ")
	print('PID\tAT\tBT\tCT\tTAT\tWT')
	for i in range(n):
		for j in range(n):
			print(process[i][j],end = '\t')
		print()

def sortInput():
	
	for i in range(n):
		for j in range(0,n-i-1):
			if(process[j][2] > process[j+1][2]):
				temp = process[j]
				process[j] = process[j+1]
				process[j+1] = temp	

def complete():
	comp.append(process[0][2])
	for i in range(1,n):
		#print(i)
		comp.append(comp[i-1]+process[i][2])
	
def turnaround():
	for i in range(n):
		turn.append(comp[i]-process[i][1])
def waiting():
	for i in range(n):
		wait.append(turn[i]-process[i][2])
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
	sortInput()
	complete()
	turnaround()
	waiting()
	average()
	Output()
main()

#OUTPUT

'''
enter number of process : 3
enter arival time for all process 
Enter arrival time : 0
Enter arrival time : 6
Enter arrival time : 0
Enter arrival time : 5
Enter arrival time : 0
Enter arrival time : 9
enter all process 
PID	AT	BT	CT	TAT	WT
P1	0	6	
P2	0	5	
P3	0	9	
PID	AT	BT	CT	TAT	WT
P2	0	5	5 	 5 	 0
P1	0	6	11 	 11 	 5
P3	0	9	20 	 20 	 11
Average Turn Around Time :  12.0
Average Waiting Time :  5.333333333333333
'''
	

