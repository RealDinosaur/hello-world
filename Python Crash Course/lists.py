firstNames = ["carleen", "john"]
lastNames = ["boyer", "clark"]
print(firstNames)
print(lastNames)
fullNames = f"{firstNames} {lastNames}"
print(fullNames)

# in python, index using brackets, 0 index
print(firstNames[0])
print(firstNames[-1]) #-1 gets "end"
print(firstNames[-2])
firstNames[0] = "carly"
print(firstNames[0])
firstNames.append("kat")
print(firstNames)
firstNames.insert(0,"zero")
print(firstNames)
#roommate = firstNames.pop()
print(firstNames)
#print(roommate)
# why doesn't this work? no output argumnents from .sort method as it acts on the string object?
print(firstNames.sort()) 
print(firstNames)
# this is the same as firstNames.sort(reverse = true)
firstNames.reverse()
print(firstNames)
print(len(firstNames))