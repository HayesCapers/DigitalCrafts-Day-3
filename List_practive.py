number_list = [1,2,7,3,5,2,2,8,]

while len(number_list) > 1:
	if (number_list[0] >= number_list[1]):
		number_list.remove(number_list[1])
	else:
		number_list.remove(number_list[0])
print number_list


while len(number_list) > 1:
	if (number_list[0] >= number_list[1]):
		number_list.remove(number_list[0])
	else:
		number_list.remove(number_list[1])
print number_list

for number in number_list:
	if (number % 2 == 0):
		print (number)


for number in number_list:
	if (number > 0):
		print (number)


# Multiply a list
factor = 3
Multiplied_list = []
for number in number_list:
	result = number * factor
	Multiplied_list.append(result)
print Multiplied_list


# Multiply Vectors
vector_list1 = [2, 4, 5]
vector_list2 = [2, 3, 6]
vector_list3 = []
position = 0

for number in vector_list1:
	vector_list3.append(vector_list1[position] * vector_list2[position])
	position += 1
print vector_list3






























