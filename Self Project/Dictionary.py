dictionary = {
	"Apple": "सेब",
	"Boy": "लड़का",
	"Cat": "बिल्ली",
	"Dog": "कुत्ता",
	"Elephant": "हाथी",
	"Fish": "मछली",
	"Graphs": "अंगूर"
}

print("Choose Number According to Task\n")
choice = int(input("Press 1 for Search Word in Dictionary\nPress 2 for Input New Words and their meaning in "
                   "Dictionary :"))
if choice == 1:
	print("Words are Reserved in Dictionary are : ", dictionary.keys())
	userInput = input("Enter English Word to find meaning of that... \n")
	print("The meaning of", userInput, "is : ", dictionary.get(userInput))

elif choice == 2:
	userKey = input("Enter English Word :")
	userValue = input("Enter Hindi meaning of that word (कृपया हिन्दी मे ही अंग्रेजी शब्द का मतलब डालें)")

	dictionary.update({userKey: userValue})
	print([dictionary])
else:
	exit(input("Exit"))

