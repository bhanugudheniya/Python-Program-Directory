def getEndingIndex(str1, n, i):
	i += 1
	while (i < n):

		curr = str1[i]
		prev = str1[i - 1]
		if ((curr == 'a' and prev == 'z') or
				(ord(curr) - ord(prev) == 1)):
			i += 1
		else:
			break

	return i - 1

def largestSubstr1(str1, n):
	Len = 0

	i = 0
	while (i < n):
		end = getEndingIndex(str1, n, i)
		Len = max(end - i + 1, Len)
		i = end + 1

	return Len

str1 = input("Enter String: ")
n = len(str1)
print(largestSubstr1(str1, n))
