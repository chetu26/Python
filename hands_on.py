print("-----Program for Student Information-----")

D = dict()

n = int(input('How many student record you want to store?? '))

for i in range(0,n):
	x, y = input("Enter the complete name (First and last name) of student: ").split()
	z = input("Enter contact number: ")
	m = input('Enter Marks: ')
	D[x, y] = (z, m)
	

def sort():
	ls = list()
	# fetch key and value using
	# items() method
	for sname,details in D.items():
	
		# store key parts as an tuple
		tup = (sname[0],sname[1])
		
		# add tuple to the list
		ls.append(tup)
		
	# sort the final list of tuples
	ls = sorted(ls)
	for i in ls:
	
		# print first name and second name
		print(i[0],i[1])
	return


def minmarks():
	ls = list()
	# fetch key and value using
	# items() methods
	for sname,details in D.items():
		# add details second element
		# (marks) to the list
		ls.append(details[1])
	
	# sort the list elements
	ls = sorted(ls)
	print("Minimum marks: ", min(ls))
	
	return


def searchdetail(fname):
	ls = list()
	
	for sname,details in D.items():
	
		tup=(sname,details)
		ls.append(tup)
		
	for i in ls:
		if i[0][0] == fname:
			print(i[1][0])
	return

sort()
minmarks()
s=input('enter first name to be searched')
searchdetail(s)

	