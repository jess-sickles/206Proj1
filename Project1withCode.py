import os
import filecmp
import csv
from collections import Counter
from datetime import datetime
import collections
#worked with Jess vu

def getData(file):

#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.
	reader = csv.DictReader(open(file))
	dlist = []
	for row in reader:
		dlist.append(row)
	return dlist

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:
	pass

#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	newlist = sorted(data, key=lambda x: x[col]) 
	answer = newlist[0].get('First')
	answer1= newlist[0].get('Last')
	result = answer + " " + answer1
	return result


	pass

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	frosh = 0
	soph = 0
	jun = 0
	senior = 0 
	for dic in data:
		if dic.get('Class') == "Freshman":
			frosh += 1
		if dic.get('Class') == "Sophomore":
			soph +=1
		if dic.get('Class') == "Junior":
			jun +=1
		elif dic.get('Class') == "Senior":
			senior +=1
	tuplist = [("Freshman",frosh), ("Sophomore",soph), ("Junior", jun), ("Senior", senior)]
	newlist = sorted(tuplist, key = lambda x: x[1] ,reverse = True )
	return newlist

	#Your code here:
	pass



# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB
	daylist = []
	for dic in a:
		daylist.append(dic.get("DOB"))
	days = []
	for word in daylist:
			days.append(word.split('/')[1])
	countinglist = Counter(days)
	most = countinglist.most_common(1)[0][0]
	return int(most)
	





	#Your code here:



# Find the average age (rounded) of the Students
def findAge(a):

# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest 
# integer.  You will need to work with the DOB to find their current age.
	doblist = []
	agelist = []
	dob = ""
	summ = 0
	daydiff=0
	today = datetime.today()
	for dic in a:
		doblist.append(dic.get("DOB"))
	for date in doblist:
		dob = datetime.strptime(date, "%m/%d/%Y")
		daydiff = today - dob
		agelist.append(daydiff.days/365)
	average = sum(agelist)/len(agelist)
	return int(average)
	pass

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None
	
	# not getting full points because of extra space 
	newlist = sorted(a, key=lambda x: x[col])
	f = str(fileName) 
	keys = a[0].keys()
	with open(f, 'w') as endcsv:
		dict_writer = csv.DictWriter(endcsv,keys)
		for line in newlist:
			dict_writer.writerow({'First':(line['First'] + ','),'Last':(line['Last'] + ','),'Email':(line['Email']) })

	pass



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
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

