from sys import stdin , stdout
facts = [];
facts.append(2) 
i = 3 
while(i <= 1000002):
	facts.append((facts[-1]*i)%1000000007)
	i += 1
t = int(stdin.readline())
for j in range (t):
	n = int(stdin.readline())
	print(facts[n-1]-1)
