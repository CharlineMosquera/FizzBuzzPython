for i in range(1, 1001):
    if (i % 3 == 0 and i % 5 == 0):
        print ("Fizzbuzz")
    elif (i % 3 == 0):
        print ("Fizz")
    elif ( i % 5 == 0):
        print ("Buzz")
    else:
        print (i)

num = 1
while num <= 1000:
    if (num % 3 == 0 and num % 5 == 0):
        print ("Fizzbuzz")
    elif (num % 3 == 0):
        print ("Fizz")
    elif (num % 5 == 0):
        print ("Buzz")
    else:
        print (num)
    num += 1