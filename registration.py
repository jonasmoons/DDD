#define variables
name_first = input("Whats your name?")
name_last = input("Whats your last name?")
myname_last = "kleine"
currentyear = int(2018)
advertiser_value = 0

print("Welcome " + name_first + " Welcome to my program.")

name_last = name_last.lower()
if myname_last == name_last:
	print("You're a family member!")

age = int(input("Whats your date of birth? ex. 2001: "))
if (2018-age) >= 18:
	print("Your old enough to continue!")
else:
	print("You shall not pass!")
	exit()

#give value based on age
if (2018-age) > 65:
	advertiser_value += 1
elif (2018-age) < 65 and (2018-age) > 30:
	advertiser_value += 5
else:
	advertiser_value += 10

#check gender
gender = input("Whats your gender? ")
if gender == "male":
	advertiser_value += 5
else:
	advertiser_value += 1
print(advertiser_value)

#check which sports person likes
sports = input("which sport do you like? ")
if sports == "soccer" or sports == "football":
	advertiser_value += 10
elif sports == "hockey" or sports == "basketball":
	advertiser_value += 5
elif sports == "none" or sports == "curling":
	advertiser_value -= 1
elif sports == ("chess"):
	print("Come on... thats not a sport.")
else:
	advertiser_value += 1


checkscore = input("Would you like to know your advertising value? y/n: ")

if checkscore == "y":
	if advertiser_value > 20:
		print("You're advertising value is high.")
		quit()
	elif advertiser_value <20 and advertiser_value >10:
		print("Your advertising value is average.")
		quit()
	else:
		print("Your advertising value is low. Lucky you.")
		quit()
else:
	print("Alright, see you later!")
	quit()



