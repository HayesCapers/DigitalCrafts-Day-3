#______counting-between-numbers______
start = raw_input("Start from: ")
end = raw_input("End on: ")

for number in range(int(start), int(end) +1):
	print number


#______Counting-ODD-Numbers_______

for number in range(1, 11, 2):
	print number

#______Print-A-Square______

empty_list = []
rows = 0 

# while (rows <= 5):
	for i in range(0, 5):
		empty_list.append("* ")
	print " ".join(empty_list)
	rows += 1
	del empty_list[:]

#

