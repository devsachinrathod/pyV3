#python list  
#Lists are used to store multiple items in a single variable.


# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
# myList = ["apple" , "banana" , "cheery" , "mango"];

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:-5])
# print(myList[1 : 3])
# print(myList[0])
# print(myList[0])
# print(len(myList))
# print(type(myList))

# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(len(thislist  ))
print(thislist)

thislist.insert(2, "watermelon")
print(thislist)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)