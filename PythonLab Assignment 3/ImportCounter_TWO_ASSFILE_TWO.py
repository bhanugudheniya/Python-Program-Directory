from collections import Counter

def winner(input):
	votes = Counter(input)

	dict = {}

	for value in votes.values():
		dict[value] = []

	for (key, value) in votes.items():
		dict[value].append(key)

	maxVote = sorted(dict.keys(), reverse=True)[0]

	if len(dict[maxVote]) > 1:
		print(sorted(dict[maxVote])[0])
	else:
		print(dict[maxVote][0])


if __name__ == "__main__":
	input = ['Bhanu', 'Rohit', 'Ramfal', 'Abhishek',
	         'Bhanu', 'Bhanu', 'Ramfal', 'Abhishek',
	         'Abhishek', 'Bhanu', 'Bhanu', 'Bhanu',
	         'Rohit']
	winner(input)
