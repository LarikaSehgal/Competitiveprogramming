class Node:
	def __init__(self, d,v): 
		self.d = d 
		self.v = v
for _ in range (int(input())):
	n , m = map(int,input().split(" "))
	l = [] ; m1 = Node(0,0) ; m2 = Node(0,0)
	for j in range (n):
		d,v = map(int,input().split(" "))
		op = Node(d,v)
		if v>m1.v:
			m1 = op
		l.append(op)
	for j in l:
		if j.v>m2.v and j != m1 and j.d != m1.d :
			m2 = j
	print(m1.v+m2.v)
