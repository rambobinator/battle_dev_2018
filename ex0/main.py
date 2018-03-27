import sys
from math import ceil

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

print(ceil(max([sum(map(int, line.split())) / len(line.split()) for line in lines[1:]])))

