import random

cpu_numb = random.randint(1,1)
user_numb = int(input("pick a number:"))

answer = bool(cpu_numb == user_numb)

print (answer)