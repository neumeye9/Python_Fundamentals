# Create a function that takes in two lists and creates a single dictionary where the first list contains keys and the second values. Assume the lists will be of equal length.
#Your first function will take in two lists containing some strings. Here are two example lists:


name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
lastname = ["Brown", "Smith", "Roberts", "Jenkins", "Sharp", "Gates"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def makeDict(arr1,arr2):
  newdict = zip(arr1,arr2)
  print newdict

makeDict(name,favorite_animal)

# If the lists are of unequal length, the longer list should be used for the keys and the shorter for the values

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
lastname = ["Brown", "Smith", "Roberts", "Jenkins", "Sharp", "Gates"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

print cmp(name,lastname)

newlist = zip(name,lastname)
print newlist