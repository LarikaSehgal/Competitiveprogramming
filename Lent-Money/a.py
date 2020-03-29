for _ in range (int(input())):
	n = int(input())
	l = list(map(int,input().split(" ")))
	k = int(input())
	x = int(input())
	s = sum(l)
	ldiff = []
	
	if(n==k):
		xorarr=[]
		for i in range(0,len(l)):
			xorarr.append(l[i]^x)
		sum1=sum(xorarr)
		if(sum1>s):
			print(sum1)
		else:
			print(s)
	

	else:
		count=0
		for i in l:
			p = i^x
			if(p-i>0):
				s=s+(p-i)
				count+=1
			ldiff.append(abs(p-i))

		if(k%2==0 and count%2 !=0):
			print(s-min(ldiff))
		else:
			print(s)
