for _ in range (int(input())):
	n = input()
	s = sum(list(map(int,list(n))))
	x = s%10 ;  r = 0
	if x != 0:
		r = 10 -x
	print(n + str(r))
