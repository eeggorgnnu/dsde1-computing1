max_num = int(100)

i = 1

for i in range(max_num + 1):
    

    if (i % 3 )== 0 and (i % 5) == 0:
        print("Fizz-Buzz")

    elif (i % 3 )== 0:
        print("fizz")

    elif (i % 5) == 0:
        print("buzz")

    else:
        print(str(i))