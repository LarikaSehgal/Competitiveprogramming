from itertools import combinations
def minans(arr,n):
	minv = 10**12
	for i in range(n-1): 
		if arr[i+1] - arr[i] < minv: 
			minv = arr[i+1] - arr[i]
	return minv 


t = int(input())
for i in range (t):
	n = int(input())
	l1 = [] ;l2 = []; 
	for j in range(n):
		s = input().split(" ")
		x = int(s[0])
		y = int(s[1])
		t1 = (x-y)/2 ; t2 = (x+y)/2 ;
		l1.append(t1)
		l2.append(t2)
	l1 = sorted(l1)
	l2 = sorted(l2)
	minv = min(minans(l1,n),minans(l2,n))		
	if (minv.is_integer()):
		print(int(minv))
	else:
		print(minv)
