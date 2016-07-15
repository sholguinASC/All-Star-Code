from random import *
from time import sleep

list1 = ["Sophia", "Angela", "Emily", "Olivia", "Isabella", "Stephanie", "Wendy"]

#list2 = ["janitor", "Street Sweeper", ""]

list3 = ["stick to a metro card", "buy a scooter", "just walk","buy a horse"]

list4 = ["mansion","apartment","house","none, just go and live under the bridge", "cardboard box"]

print("Welcome to MASH up!")
wife = raw_input("What would you like your wife's name to be?")
job = raw_input("What is your dream job?")
car = raw_input("What type of car would you like to buy IF you had money?")
home = raw_input("What type of home would you like to live in?")

print("Creating MASH up")
for i in range(5):	
	sleep(.3)
	print(i)

print("Your Wife's name will be " + choice(list1) + ". Your dream job is going to be working at "+ job + ". You can't afford that car either way so " + choice(list3) + ". And the type of home that you deserve is a " + choice(list4) + ".")
