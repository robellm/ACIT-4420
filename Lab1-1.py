#Task 1
print("This is Task 1")
name = input("Hi there!\nWhat's your name? ")
number = int(input("How many cookies would you like to have? "))
cookies = ' cookie ' *number
print(f"Hi {name.title()}, here are your cookies: {cookies}")



#Task 2
print("\nThis is Task 2")
name2 = input("Hi there!\nWhat's your name? ")
number2 = int(input("How many cookies would you like to have? "))
cookies = ' cookie ' *number2
if (1<=number2<10):
    print("Are you sure it's enough?")

elif (10<=number2<20):
    print("I agree cookies are delicious!")

elif (20<=number2<=50):
    print("Be careful, it's getting too much")

elif (number2>50):
    cookies = ' cookie ' *50
    print("No way, it's too much! Max you can get is 50 cookies")

else:
    cookies = ' cookie ' *10
    print("Something must be wrong, I'll give you 10 cookies")

print(f"Hi {name2.title()}, here are your cookies: {cookies}")



#Task 3
print("\nThis is Task 3")
num = int(input('How many numbers do you have? '))
total_sum = 0
number3 = 0
for n in range(num):
    number3 +=1
    numbers = int(input(f'What is the {number3} number: '))
    total_sum += numbers
    avg = total_sum/num
print(f'The average is {avg: .2f}')
