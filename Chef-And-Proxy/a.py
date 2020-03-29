import math
for _ in range (int(input())):
	d = int(input())
	s = input()
	x = s.count("P")
	dmin = math.ceil(0.75*d - x)
	if dmin <=0 :
		print(0)
	if dmin > 0 :
		i = 2 ; c = 0
		while (c<dmin and i<d-2):	
			if s[i] == "A":
				cp = 0 ; ca = 0
				if s[i-2] == "P" or s[i-1] == "P" :
					cp = 1
				if s[i+2] == "P" or s[i+1] == "P" :
					ca = 1
				if cp == 1 and ca == 1:
					c +=1
			i+=1		
		if c >= dmin :
			print(dmin)
		if c<dmin :
			print(-1)
