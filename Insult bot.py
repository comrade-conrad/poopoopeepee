
import random
user_response = ""



print("hello how are you?")
user_response == input()
if user_response == "good" or user_response == "Good":
    file = open("Insult.txt")
    line = file.readline()
    print(line)
    