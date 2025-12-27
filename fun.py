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

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(len(thislist  ))
# print(thislist)

# thislist.insert(2, "watermelon")
# print(thislist)

# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)


# list1 = ["apple", "banana", "cherry" , "apple"]
# set1 = {"apple", "banana", "cherry" , "apple"}
# tuple1 = ("apple", "banana", "cherry")
# three different data structures with the same values

# dictionary with key-value pairs
# print(type(list1))
# print(type(set1))
# print(type(tuple1))
# print(type(dict1))

# print(list1)
# print(set1)
# print(tuple1)
# num = range(6)
# print(num)
# for n in num:
#   if n  == 3:
#     continue
#     print(n)

# def my_function(*kids):
#   print("The youngest child is " + kids[2])
#   print("The first child is " + kids[0])

# my_function("Emil", "Tobias", "Linus")

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def changecase(func):
  def myinner():
    return func().lower()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())