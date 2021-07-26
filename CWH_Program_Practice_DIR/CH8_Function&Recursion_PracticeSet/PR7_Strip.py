def remove_and_strip(string, word):
	newStr = string.replace(word, "")
	return newStr.strip()


this = '    bhanu is a good boy   '
print(remove_and_strip(this, 'bhanu'))
# print(this)
# print(this.strip())