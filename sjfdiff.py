

global name,arrival,burst,comp,turn,wait
name = []
arrival=[]
burst = []
comp = []
turn = []
wait = []

'''
>>> from operator import itemgetter
>>> L=[[0, 1, 'f'], [4, 2, 't'], [9, 4, 'afsd']]
>>> sorted(L, key=itemgetter(2))
[[9, 4, 'afsd'], [0, 1, 'f'], [4, 2, 't']]
'''

#arrival = list(map(int,input("\nEnter the arrival time for all : ").strip().split()))[:n]
#burst = list(map(int,input("\nEnter the burst time for all : ").strip().split()))[:n]

def readinput():
	global n
	n = int(input("enter number of process : "))
	print ("enter arival time for all process ")
	for i in range(n):
		nm = 'P'+str(i+1)
		name.append(nm) 
		arrival.append(int(input()))
	print ("enter burst time for all process ")
	for i in range(n):
		burst.append(int(input()))

def complete():
	burst.sort()
	comp.append(burst[0])
	for i in range(1,n):
		#print(i)
		comp.append(comp[i-1]+burst[i])
	
def turnaround():
	for i in range(n):
		turn.append(comp[i]-arrival[i])
def waiting():
	for i in range(n):
		wait.append(turn[i]-burst[i])
def average():
	global sumt,sumw,avgt,avgw
	sumt = sum(turn)
	sumw = sum(wait)
	avgt = sumt/float(n)
	avgw = sumw/float(n)

def Output():
	print('PID\tAT\tBT\tCT\tTAT\tWT')
	for i in range(n):
		print(name[i],'\t',arrival[i],'\t',burst[i],'\t',comp[i],'\t',turn[i],'\t',wait[i],'\t',)
	print('Average Turn Around Time : ',avgt)
	print('Average Waiting Time : ',avgw)
	
def main():
	readinput()
	complete()
	turnaround()
	waiting()
	average()
	Output()
main()
	
#OUTPUT
'''
enter number of process : 5
enter arival time for all process 
1
2
3
4
5
enter burst time for all process 
2
3
5
4
6
PID	AT	BT	CT	TAT	WT
P1 	 1 	 2 	 3 	 2 	 0 	
P2 	 2 	 3 	 6 	 4 	 1 	
P3 	 3 	 5 	 11 	 8 	 3 	
P4 	 4 	 4 	 15 	 11 	 7 	
P5 	 5 	 6 	 21 	 16 	 10 	
Average Turn Around Time :  8.2
Average Waiting Time :  4.2
'''	

