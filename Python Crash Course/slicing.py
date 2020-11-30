#slicing
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # same as MATLAB
# same as 
print(players[:3])
print(players[3:4]) # 4 - 3 = 1 so it returns 1 entry (remember it's not inclusive)

# get all with colon operator, returns full list
playersCopy = players[:]

# immutable list is a tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# produces error
# dimensions[0] = 201
# fine
dimensions = (201, 50)
print(dimensions[0])