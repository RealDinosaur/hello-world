message = "fuck fuck fuck"
firstName1, firstName2 = "carleen", "john"
lastName1, lastName2 = "boyer", "clark"
print(message.upper())
print(message.lower())
print(message.title())

fullName = f"{firstName1} {lastName1}"
print(fullName)
message2 = f"Hello, {fullName.title()}! "
print(message2)
print(message2.strip()) # strip only removes spaces from ends of strings
print('invalid syntax')
square = 3_000.1**2
print(square)
favNum = 28
print(f"My Favorite Number is: {favNum}")