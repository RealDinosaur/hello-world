# chapter 5
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

if 'audi' in cars:
	print('Damn you got an audi?')
elif 'toyota' in cars:
	print('Basic')
else:
	print('k')

users = ['admin','john','carly','kat','zero','daniel']
# users = []
if len(users) == 0:
	print("find Users!")
for user in users:
	if user == 'admin':
		messageEnd = "would you like to see a status report?"
	else:
		messageEnd = "welcome"
	fullMessage = f"Hello {user}, {messageEnd}"
	print(fullMessage)