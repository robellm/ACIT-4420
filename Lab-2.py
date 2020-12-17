# Task 1
import idx as idx

print("\nWelcome to TASK 1 from Lab 2!\n")

week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
meeting_table = [[''] * 24 for i in range(7)]

# Set an initial value for choice other than the value for 'quit'.
choice = ''

# Start a loop that runs until the user enters the value for 'quit'.
while choice != 'x' and choice != 'l':
    # Give all the choices in a series of print statements.
    print('''   [1] Enter 's' to store program.
                [2] Enter 'l' to list the program.
                [3] Enter 'x' to quit.''')

    # Ask for the user's choice.
    choice = input("\nWhat would you like to do? ")
    
    # Respond to the user's choice.
    if choice == 's':
        day = input("Which day? ")
        idx = week.index(day)
        time = int(input("What time? "))
        program = input("What is the program? ")
        meeting_table[idx][time] = program
        
    elif choice == 'l':
       day = input(f"Which day?: ")
       idx = week.index(day)
       for i in range(24):
           print(str(i) + ':00', meeting_table[idx][i])

    elif choice == 'x':
        print("\nYou've exited.\n")

    else:
        print("\nI don't understand that choice, something went wrong! Please try again.\n")

# Print a message that we are all finished.
print("That was it for Task 1, bye for now.")





# TASK 2
file = open("python.txt", "rt")
content = file.readlines()

di = dict()

for i in content:
    i = i.replace(",", "").replace(".", "").replace("'", "").replace("()", "").replace('"', "").replace("\n", "").replace("(", "").replace(")", "")
    print(i)

    wds = i.split()
    for w in wds:        #(di[w] = di.get(w, 0) + 1)
        if w in di:
            di[w] = di[w]+1
        else:
            di[w] = 1
        #print(w,di[w])


#print(di)
for k, v in di.items():
    if v > 3:
        print(f"{k}: {v}")
