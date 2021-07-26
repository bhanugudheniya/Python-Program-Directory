def percent(marks):
	p = (sum(marks)/400)*100    # p = ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
	return p

# return : Laut chalo iss value ke saath

marks1 = [45, 78, 86, 77]
percentage1 = percent(marks1)

marks2 = [75, 98, 88, 78]
percentage2 = percent(marks2)

print(percentage1, percentage2)