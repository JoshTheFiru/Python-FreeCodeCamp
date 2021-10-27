friends = ["Kevin", "Karen", "Jim", "Oscar", "Tango", "John"] #strings list
things = ["Person", 2, True] #multiple types list
friends[4] = "Mike"

print(things[2])
print(friends[-2]) #with negative values starts counting from the back
print(friends[1:]) #print the list minus the first element
print(friends[1:3]) #prints from 1 to 3 of the list not including the values

#using functions with lists
lucky_numbers = [4, 8, 15, 16, 23, 42]

friends.extend(lucky_numbers) #append one list to another
print(friends)

friends.append("Creed") #append one item
print(friends)

friends.insert(1, "Kelly") #inserts one item to the index position specified
print(friends)

friends.remove("Jim") #removes an item from the list
print(friends)

#friends.clear() #removes the list

friends.pop() #removes the last item of the list
print(friends)

print(friends.index("Mike")) #returns the index of the element

print(friends.count("Jim")) #counts the number of times an element appears in the list

lucky_numbers.sort() #orders the list
print(lucky_numbers)

lucky_numbers.reverse() #orders reverse the list
print(lucky_numbers)

friends2 = friends.copy() #copy the list into a new one
print(friends2)