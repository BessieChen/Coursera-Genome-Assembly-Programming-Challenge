#Uses python3

from collections import defaultdict
import itertools

in_binary= int(input())
position = in_binary-1

last ='1'*in_binary
bin_integer = int(last, 2)

last_before = "1"+('0'*position)
first = '0'*in_binary
nodes = defaultdict(list)
for i in range(0,bin_integer+1):
		aa = (bin(i)[2:].zfill(in_binary))
		if (aa!=last_before and aa!=first):
			string = aa[0:position]
			edge = aa[1:in_binary]
			nodes[string].append(edge)
			nodes[edge].append(string)

start = '0'*(in_binary-1)
tour = [start]
current = start
while(len(nodes[current])>0):
	suffix = current[1:]
	next_Char = "1" if suffix+"1" in nodes[current] else "0"
	tour.append(suffix+next_Char)
	nodes[current].remove(suffix+next_Char)
	nodes[suffix+next_Char].remove(current)
	current = suffix+next_Char

res ='0'
for i,d in enumerate(tour):res+=d[0]
print(res)