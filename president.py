president = {}  #empty dictionary
fh = open("presidents.txt", "r")   #open the file for reading
data = fh.readline()   #read a line
presdata = data.split(",")   #split on the commas, create a list
president['lastname'] = presdata[0]  #the first value--index 0-- is last name
president['firstname'] = presdata[1]  #the second value--index 1-- is first name
president['height'] = presdata[2]  #the third value--index 2-- is height in cm
president['weight'] = presdata[3]  #the fourth value--index 3-- is weight in pounds