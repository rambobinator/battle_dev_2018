import sys
from math import floor

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

my_notes = list(map(int, lines[0].split()))
best_friend_nbr = int(lines[2])
friends = [list(map(int, line.split())) for line in lines[3:]]
friends_scores = {}
for i, friend in enumerate(friends):
	score = abs(sum([a-b if (a > b) else (b - a)
		for a, b in zip(my_notes, friend)]))
	friends_scores.update({score: i})
print(floor(sum([friends[friends_scores[k]][5]
	for k in sorted(friends_scores.keys())[:best_friend_nbr]]) / best_friend_nbr))
