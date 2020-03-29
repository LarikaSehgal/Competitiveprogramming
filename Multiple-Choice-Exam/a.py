for _ in range (int(input())):
	n = int(input())
	s1 = input()
	s2 = input()
	count = 0 ; i=0
	while i <n:
		a = s1[i] ; b = s2[i]
		if (i == n-1):
			if (a == b):
				count+=1
		else:
			if (a == b):
				count+=1
			if (a != b and b!= "N"):
				i+=1
		i +=1
	print(count)
