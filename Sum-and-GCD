import math
from itertools import combinations
def gcd(l):
	if len(l) == 1 :
		return l[0]
	if len(l) == 2 :
		return(math.gcd(l[0],l[1]))
	if len(l)>2 :
		res = math.gcd(l[0],l[1])
		for i in range (2,len(l)):
			res = math.gcd(res,l[i])
		return res

for _ in range (int(input())):
	n = int(input())
	arr = list(map(int,input().split()))
	if n<=20:
		temp = [] ; maxv = 0
		for i in range (1,n//2 +1):
			temp += list(combinations(arr,i))
		for i in range (len(temp)):
			x = temp[i]
			cop = arr.copy()
			for j in x:
				cop.remove(j)
			x = list(x)
			v = gcd(x) + gcd(cop)
			if v>maxv:
				maxv =v
		print(maxv)
	if n>20:
		if len(arr) ==2:
			print(l[0] + l[1])
		if len(arr) >2 :
			m1 = max(arr)
			arr = list(filter(lambda a: a != m1, arr))
			if len(arr) == 0:
				print(2*m1)
			if len(arr)>=1:
				m2 = max(arr)
				arr = list(filter(lambda a: a != m2, arr))
				if len(arr)==0:
					print(m1+ m2)
				else:			
					g1 = gcd(arr)
					gm1 = math.gcd(g1,m1)
					gm2 = math.gcd(g1,m2)
					v1 = gm1 + m2
					v2 = gm2 + m1
					print(max(v1,v2))

