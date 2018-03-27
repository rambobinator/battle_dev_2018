import sys
from collections import OrderedDict
from math import ceil

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

coupons = OrderedDict([
	(0, 1.0),
	(4, 0.9),
	(6, 0.8),
	(10, 0.7),
])

turnover = 0
price = int(lines[0])
for line in lines[2:]:
	client_nbr = int(line)
	table_price = price
	for k, v in coupons.items():
		if client_nbr >= k:
			table_price = price * v
	table_turnover = client_nbr * table_price
	turnover += table_turnover
print(ceil(turnover))
