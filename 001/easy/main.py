from datetime import datetime
from pathlib import Path

print("Please, enter your information:")

name = input("Name: ")

while True:
	try:
		age = int(input("Age: "))
		break
	except ValueError as e:
		print("Age must be an integer number, please try again:")

username = input("Username: ")

print(f"your name is {name}, you are {age} years old, and your username is {username}.")

dir = Path("./logs")
dir.mkdir(parents=True, exist_ok=True)
with open(f"{dir}/{datetime.now().strftime("%Y-%m-%d_%H-%M-%S.log")}", "w", encoding="utf-8") as log:
	log.write(f"name : {name}\nage : {age}\nusername : {username}")