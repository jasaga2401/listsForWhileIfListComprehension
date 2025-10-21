
# display data elements in a list
numbers = [10, 20, 30, 40, 50]

# loop though list(1)
for x in range(0, len(numbers)):

    print(numbers[x], end=' ')

print('')
# loop though list(2)
for item in numbers:

    print(item, end= ' ')

print('')
# searching for a data item
searchItem = 40

if searchItem in numbers:

    print('Found')

# condition such as a WHILE .. IN loop
while 20 in numbers:

    print('It is there!')
    numbers.remove(20)

# setting up a list
import random, string
password = string.ascii_letters + string.digits + string.punctuation

createPassword = [random.choice(password) for x in range(0, 9)]

createPassword = [random.randrange(0, 100) for x in range(0, 10000)]

print(createPassword)














    









