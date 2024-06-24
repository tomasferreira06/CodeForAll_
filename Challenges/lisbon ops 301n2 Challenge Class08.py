# Script: lisbon-ops-301n2: Challenge Class08.
# Purpose: Create a list and use various commands to manipulate it.
# Why: Know basic commands of Python

#Creating the variable "list" with the 10 elements
list = ["apple","banana","orange","grape","kiwi","melon","peach","plum","pear","strawberry"]

#Prints the fourth element of the list
print("Fourth element of the list:" , list[3])

#Prints the sixth to tenth elements of the list
print("Sixth through tenth elements of the list:" , list[5:10])

#Changes the seventh element of the variable "list"
list[6]= "onion"

#Prints the updated list
print("Changed seventh element of list:" , list)

#Stretch Goals
print("\n")
print("STRETCH GOALS")
print("\n")

#Appending "blueberry" to the list
list.append("blueberry")
print("List after append:", list)
print("\n")

#Clearing the list
list.clear()

#Creating original list again
list = ["apple","banana","orange","grape","kiwi","melon","peach","plum","pear","strawberry"]

#Copying "list" into a new variable called "copied_list"
copied_list = list.copy()
print("Copied list:", copied_list)
print("\n")

#Counts the number of ocurrences of the specified element in the list
pear_count = list.count("pear")
print("Count of 'pear':", pear_count)
print("\n")

#Appends elements from another list to "extension_list", to the end of "list"
extension_list = ["raspberry", "blackberry"]
list.extend(extension_list)
print("List after extend:", list)
print("\n")

#Prints out the index (position) of the element "orange" in the list
orange_index = list.index("orange")
print("Index of 'orange':", orange_index)
print("\n")

#Inserts "cherry" into the second element of the list
list.insert(2, "cherry")
print("List after insert:", list)
print("\n")

#Removes and returns the last element of "list" and saves it into variable called "last_element"
last_element = list.pop()
print("Popped element:", last_element)
print("\n")

#Removes specified element from list (grape)
list.remove("grape")
print("List after remove:", list)
print("\n")

#Reverses the current order of the list
list.reverse()
print("List after reverse:", list)
print("\n")

#Sorting list in alphabetical order
list.sort()
print("List after sort:", list) 
























