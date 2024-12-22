list1 = [34, 43, 87, 34, 52, 55]

print(list1[3])

for i in list1:
    print(i)

list1.append(100)
print(list1)

list1.insert(2, 50)
print(list1)

list1.insert(0, 0)
print(list1)

list1.pop()
print(list1)

list1.remove(55)
print(list1)

list1.pop(3)
print(list1)

print(len(list1))

#2D lists

list2 = [34, 564, 433, [432, 53, 645]]
print(list2)

list3 = [[324, 432, 35, 54], [234, 456, 56, 45], [543, 5545, 52, 234]]
print(list3)

print(list3[0][1])
print(list3[2])

#No. of rows in a 2D list
print(len(list3))

#No. of columns in a 2D list
print(len(list3[0]))

print(len(list3) * len(list3[0]))

for i in range(len(list3)):
    for j in range(len(list3[0])):
        print(list3[i][j])