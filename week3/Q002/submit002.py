# Uses python3
import sys

def whether_opt(n, reads):
	k_mers = set()
	for re_ad in reads:
		for i in range(0, len(re_ad)-n+1):
			k_mers.add(re_ad[i:i+n])
	prefixes = set()
	suffixes = set()
	for kmer in k_mers:
		prefixes.add(kmer[:-1])
		suffixes.add(kmer[1:])
	return prefixes == suffixes

reads = []
for i in range(1618):
	re_ad = sys.stdin.readline().strip()
	reads.append(re_ad)

for n in range(len(reads[2]), 1, -1):
	if whether_opt(n, reads):
		print(n)
		break