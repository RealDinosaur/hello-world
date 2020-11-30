# magicians.py
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)
print(magician)
# can we do the same with indexing
for value in range(0,len(magicians)):
	print(magicians[value])
print(len(magicians))

for value in range(1,21):
	print(value)

mil = range(1,1_000_001)
print(len(mil))

print(sum(mil))
odds = range(1,21,2)
for odd in odds:
	print(odd)

threes = range(3,31,3)
for three in threes:
	print(three)

cubes = []
for value in range(11):
	cubes.append(value**3)
	print(cubes[value])

cubes2 = [value**3 for value in range(11)]
print(cubes2)