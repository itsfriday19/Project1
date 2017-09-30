import os
import datetime
from datetime import datetime, timedelta
import filecmp

# Note: any comments are me rubber-ducky-ing to myself to help me figure out the code

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:
	fh = open(file, "r")
	fh = fh.read()
	sfh = fh.split()
	#print (fh)
	#print ("\n **********", sfh)

	lst = []
	keys = sfh[0].split(",") #list of strings because I split it

	for l in sfh[1:]:
		fdict = {}
		for w in l.split(","): #gives back student info on word-level
			indx = l.split(",").index(w) #indexed with their position, returns a number
			fdict[keys[indx]] = w 
		lst.append(fdict)
	return lst



#Sort based on key/column
def mySort(data,col): #data is a list, col is a string "First", "Last" "Email"
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName
	new_d = {}
	#Your code here:
	for d in data:
		name = d["First"] + " " + d["Last"]
		new_d[name] = d[col]
	sorted_dict = sorted(new_d.keys(), key = lambda x: new_d[x])
	return sorted_dict[0]
 

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	# print ("\n********HERE********", data)
	counts = {}
	# I'm trying to take the value of Class and make it a key in counts, where the value 
	# is the number of times that value in Class occurs. So like, for loop. 
	for d in data:
		if d["Class"] not in counts:
			counts[d["Class"]] = 1
		else:
			counts[d["Class"]] += 1
	
	class_sort = sorted(counts.items(), key = lambda x:x[1], reverse = True)
	return class_sort





# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	counts = {}

	for d in a:
		if (d["DOB"].split("/")[1]) not in counts:
			counts[d["DOB"].split("/")[1]] = 1
		else:
			counts[d["DOB"].split("/")[1]] += 1
	dom_sort = sorted(counts.keys(), key = lambda x: counts[x], reverse = True)
	return int(dom_sort[0])


# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest 
# integer. You will need to work with the DOB to find their current age.


	#Your code here:
	 lst = []
	 for d in a:
	 	dob = d["DOB"]
	 	dt = datetime.strptime(dob, '%m/%d/%Y')
	 	dt2 = datetime.today()
	 	timedelta = dt2 - dt
	 	strTime = timedelta.__str__()
	 	splitD = strTime.split()
	 	d = (int(splitD[0]))
	 	d = d/365
	 	d = round(d)
	 	lst.append(d)
	
	 aa = sum(lst)/len(lst)
	 aa = round(aa)
	 return aa
	

# Similar to mySort, but instead of returning single
# Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName): #a = list of dicts, col = Last, fileName = results.csv
# Input: list of dictionaries, key to sort by and output file name
# Output: None

	#Your code here:
	# I need to take the list of dicts a, iterate through and grab
	# just First, Last, and Email. 
	
	lst = []
	for d in a:
		lst.append((d['First'], d['Last'], d['Email']))
	sorted_tup = sorted(lst, key = lambda x: x[1])

	outfile = open(fileName, "w")
	for student in sorted_tup: 
		outfile.write("{},{},{},\n".format(*student))

	outfile.close()



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),40,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

